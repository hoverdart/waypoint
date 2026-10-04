"""One locked state machine per exam. Timers and section membership are server-owned.

A draft is a versioned snapshot of the current section. Finishing uses only saved
answers, and fills unanswered questions with blanks. Expired sections reject edits
but remain finishable. Later sections do not open until explicitly started. The
final transition invokes the existing transactional scorer once for all sections.
"""
from copy import deepcopy
from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select

from app.core.exceptions import ConflictError, DomainError, NotFoundError
from app.models.practice import PracticeSession
from app.models.question import Question
from app.models.subject import Subject, Unit
from app.schemas.exams import ExamDraftRequest, ExamFormRead, ExamSectionSummary, ExamSessionRead
from app.services.exams.blueprints import BLUEPRINTS, ExamBlueprint
from app.services.practice.question_presentation import questions_to_reads
from app.services.practice.scope import validate_practice_scope
from app.services.practice.session_service import submit_practice_session
from app.services.practice.types import AnswerSubmission
from app.services.practice.validation import validate_submission


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _resolve_items(db: Session, subject_id: int, blueprint: ExamBlueprint) -> dict[str, Question]:
    required = {key for section in blueprint.sections for key in section.item_keys}
    found = {}
    duplicates = set()
    for question in db.exec(select(Question).join(Unit, Question.unit_id == Unit.id).where(
        Question.subject_id == subject_id, Question.is_active == True,
        Question.validation_status == 'approved', Unit.is_active == True,
    )).all():
        for tag in question.skill_tags:
            if tag.startswith('item:') and tag[5:] in required:
                key = tag[5:]
                if key in found:
                    duplicates.add(key)
                found[key] = question
    # Fail closed if an admin change duplicates/removes an exam item or alters type.
    if duplicates or set(found) != required:
        return {}
    for index, section in enumerate(blueprint.sections):
        expected_type = 'mcq' if index == 0 else 'frq'
        if any(found[key].type != expected_type for key in section.item_keys):
            return {}
    if len({q.id for q in found.values()}) != len(required):
        return {}
    return found


def list_forms(db: Session, subject_id: int) -> list[ExamFormRead]:
    validate_practice_scope(db, subject_id)
    subject = db.get(Subject, subject_id)
    return [ExamFormRead(form_id=b.form_id, title=b.title, source_url=b.source_url,
        sections=[ExamSectionSummary(title=s.title, duration_seconds=s.seconds,
            question_count=len(s.item_keys), score_weight=s.weight, instructions=s.instructions) for s in b.sections],
        available=bool(_resolve_items(db, subject_id, b)))
        for b in BLUEPRINTS.values() if b.subject_code == subject.ap_exam_code]


def start_exam(db: Session, user_id: int, subject_id: int, form_id: str, multiplier: float) -> PracticeSession:
    validate_practice_scope(db, subject_id)
    blueprint = BLUEPRINTS.get(form_id)
    subject = db.get(Subject, subject_id)
    if blueprint is None or blueprint.subject_code != subject.ap_exam_code:
        raise NotFoundError('Exam form not found for this course')
    if multiplier not in (1.0, 1.5, 2.0):
        raise DomainError('Choose a supported practice time allowance')
    items = _resolve_items(db, subject_id, blueprint)
    if not items:
        raise ConflictError('This form is unavailable while its content is being updated')
    now = utc_now()
    sections = []
    for index, section in enumerate(blueprint.sections):
        seconds = int(section.seconds * multiplier)
        sections.append({'title': section.title, 'duration_seconds': seconds,
            'score_weight': section.weight, 'instructions': section.instructions,
            'question_ids': [items[key].id for key in section.item_keys],
            'started_at': now.isoformat() if index == 0 else None,
            'deadline': (now + timedelta(seconds=seconds)).isoformat() if index == 0 else None,
            'finished_at': None, 'answers': [], 'current_index': 0, 'revision': 0})
    question_ids = [qid for section in sections for qid in section['question_ids']]
    session = PracticeSession(user_id=user_id, subject_id=subject_id, session_type='timed',
        total_questions=len(question_ids), session_metadata={'question_ids': question_ids,
            'exam': {'form_id': form_id, 'title': blueprint.title, 'source_url': blueprint.source_url,
                     'time_multiplier': multiplier, 'current_section': 0, 'sections': sections}})
    db.add(session)
    db.flush()
    return session


def owned_exam(db: Session, user_id: int, session_id: int, *, lock=False) -> PracticeSession:
    query = select(PracticeSession).where(PracticeSession.id == session_id, PracticeSession.user_id == user_id)
    if lock:
        query = query.with_for_update().execution_options(populate_existing=True)
    session = db.exec(query).first()
    if session is None or 'exam' not in session.session_metadata:
        raise NotFoundError('Exam session not found')
    return session


def _section_status(section: dict, now: datetime) -> str:
    if section['finished_at']:
        return 'finished'
    if section['started_at'] is None:
        return 'ready'
    return 'expired' if now >= datetime.fromisoformat(section['deadline']) else 'active'


def read_exam(db: Session, session: PracticeSession) -> ExamSessionRead:
    now = utc_now()
    exam = session.session_metadata['exam']
    current = exam['sections'][exam['current_section']]
    # No preview of unopened or closed sections; complete results have their own API.
    visible = session.completed_at is None and _section_status(current, now) == 'active'
    ids = current['question_ids'] if visible else []
    by_id = {q.id: q for q in db.exec(select(Question).where(Question.id.in_(ids))).all()} if ids else {}
    return ExamSessionRead(session_id=session.id, subject_id=session.subject_id,
        title=exam['title'], form_id=exam['form_id'], time_multiplier=exam['time_multiplier'],
        server_time=now, current_section=exam['current_section'], completed=session.completed_at is not None,
        sections=[dict(index=i, title=s['title'], duration_seconds=s['duration_seconds'],
            score_weight=s['score_weight'], instructions=s['instructions'], question_count=len(s['question_ids']),
            started_at=s['started_at'], deadline=s['deadline'], finished_at=s['finished_at'],
            status=_section_status(s, now)) for i, s in enumerate(exam['sections'])],
        questions=questions_to_reads(db, [by_id[qid] for qid in ids]),
        answers=current['answers'] if visible else [], current_index=current['current_index'], revision=current['revision'])


def _current_exam(db: Session, user_id: int, session_id: int, index: int):
    session = owned_exam(db, user_id, session_id, lock=True)
    exam = deepcopy(session.session_metadata['exam'])
    if session.completed_at is not None or index != exam['current_section']:
        raise ConflictError('This section is already closed or is not the current section')
    return session, exam, exam['sections'][index]


def _persist(db: Session, session: PracticeSession, exam: dict):
    session.session_metadata = {**session.session_metadata, 'exam': exam}
    db.add(session)
    db.flush()


def save_draft(db: Session, user_id: int, session_id: int, index: int, payload: ExamDraftRequest):
    session, exam, section = _current_exam(db, user_id, session_id, index)
    if _section_status(section, utc_now()) != 'active':
        raise ConflictError('The section is not open for editing; refresh to continue')
    if payload.expected_revision != section['revision']:
        raise ConflictError('A newer draft was saved elsewhere; reload before making changes')
    allowed = set(section['question_ids'])
    if payload.current_index >= len(allowed) or any(a.question_id not in allowed for a in payload.answers):
        raise DomainError('Draft contains a question or position outside this section')
    validate_submission(db, session.id, [AnswerSubmission(**a.model_dump()) for a in payload.answers],
                        diagnostic=False, partial=True, allow_exam=True)
    section['answers'] = [a.model_dump() for a in payload.answers]
    section['current_index'] = payload.current_index
    section['revision'] += 1
    _persist(db, session, exam)
    return session


def begin_section(db: Session, user_id: int, session_id: int, index: int):
    session, exam, section = _current_exam(db, user_id, session_id, index)
    if _section_status(section, utc_now()) != 'ready':
        raise ConflictError('This section has already started')
    now = utc_now()
    section['started_at'] = now.isoformat()
    section['deadline'] = (now + timedelta(seconds=section['duration_seconds'])).isoformat()
    _persist(db, session, exam)
    return session


def finish_section(db: Session, user_id: int, session_id: int, index: int):
    session, exam, section = _current_exam(db, user_id, session_id, index)
    now = utc_now()
    state = _section_status(section, now)
    if state not in ('active', 'expired'):
        raise ConflictError('Start this section before finishing it')
    section['finished_at'] = min(now, datetime.fromisoformat(section['deadline'])).isoformat()
    if index + 1 < len(exam['sections']):
        exam['current_section'] += 1
        _persist(db, session, exam)
        return session
    _persist(db, session, exam)
    stored = {a['question_id']: a for s in exam['sections'] for a in s['answers']}
    answers = [AnswerSubmission(**stored.get(qid, {'question_id': qid})) for qid in session.session_metadata['question_ids']]
    return submit_practice_session(db, session.id, answers, now=now, allow_exam=True)
