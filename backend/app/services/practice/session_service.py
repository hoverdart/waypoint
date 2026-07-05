"""Regular (non-diagnostic) MCQ/FRQ/timed practice sessions. Mastery only
updates once the whole session is submitted, grouped by topic - never per
question - mirroring the diagnostic scorer's approach via the shared
mastery_sync helper.
"""

import random
from datetime import datetime, timezone

from sqlmodel import Session, select

from app.models.planner import DailyPlanItem
from app.models.practice import PracticeSession, QuestionAttempt
from app.models.question import Question
from app.services.practice.mastery_sync import apply_session_attempts_to_mastery
from app.services.practice.scoring import score_frq_attempt, score_mcq_attempt
from app.services.practice.types import AnswerSubmission
from app.services.mastery.topic_mastery import AttemptSignal
from app.services.xp.badge_service import evaluate_and_award_badges
from app.services.xp.xp_service import award_xp

DEFAULT_QUESTION_COUNT = 12
XP_BASE_AWARD = 10
XP_PER_CORRECT_ANSWER = 2


def start_practice_session(
    db: Session,
    user_id: int,
    subject_id: int,
    unit_id: int | None = None,
    topic_id: int | None = None,
    session_type: str = "mcq",
    question_count: int = DEFAULT_QUESTION_COUNT,
    rng: random.Random | None = None,
) -> tuple[PracticeSession, list[Question]]:
    rng = rng or random.Random()

    query = select(Question).where(
        Question.subject_id == subject_id,
        Question.is_active == True,  # noqa: E712
        Question.validation_status == "approved",
    )
    if unit_id is not None:
        query = query.where(Question.unit_id == unit_id)
    if topic_id is not None:
        query = query.where(Question.topic_id == topic_id)
    if session_type in ("mcq", "frq"):
        query = query.where(Question.type == session_type)

    candidates = list(db.exec(query).all())
    rng.shuffle(candidates)
    selected = candidates[:question_count]

    session = PracticeSession(
        user_id=user_id,
        subject_id=subject_id,
        unit_id=unit_id,
        topic_id=topic_id,
        session_type=session_type,
        total_questions=len(selected),
        # The selected question set is otherwise never persisted anywhere -
        # without this, reloading /practice/session/[id] (a fresh page load,
        # so no client-side state survives) would have no way to know which
        # questions belong to this session.
        session_metadata={"question_ids": [q.id for q in selected]},
    )
    db.add(session)
    db.flush()
    return session, selected


def get_session_questions(db: Session, session: PracticeSession) -> list[Question]:
    question_ids = session.session_metadata.get("question_ids", [])
    questions_by_id = {q.id: q for q in db.exec(select(Question).where(Question.id.in_(question_ids))).all()}
    return [questions_by_id[qid] for qid in question_ids if qid in questions_by_id]


def submit_practice_session(
    db: Session,
    session_id: int,
    answers: list[AnswerSubmission],
    daily_plan_item_id: int | None = None,
    now: datetime | None = None,
) -> PracticeSession:
    now = now or datetime.now(timezone.utc)
    session = db.get(PracticeSession, session_id)

    attempts_by_topic: dict[int, list[AttemptSignal]] = {}
    correct_count = 0

    for ans in answers:
        question = db.get(Question, ans.question_id)
        if question.type == "mcq":
            is_correct, score, max_score = score_mcq_attempt(db, question, ans.selected_option_id)
        else:
            is_correct, score, max_score = score_frq_attempt(question, ans.free_response_text)

        db.add(
            QuestionAttempt(
                user_id=session.user_id,
                session_id=session.id,
                question_id=question.id,
                selected_option_id=ans.selected_option_id,
                free_response_text=ans.free_response_text,
                is_correct=is_correct,
                score=score,
                max_score=max_score,
                time_seconds=ans.time_seconds,
                hints_used=ans.hints_used,
                explanation_opened=ans.explanation_opened,
                confidence_rating=ans.confidence_rating,
            )
        )
        if is_correct:
            correct_count += 1
        attempts_by_topic.setdefault(question.topic_id, []).append(
            AttemptSignal(
                is_correct=is_correct,
                difficulty=question.difficulty,
                hints_used=ans.hints_used,
                time_seconds=ans.time_seconds,
            )
        )

    session.completed_at = now
    session.correct_count = correct_count
    session.score = correct_count / session.total_questions if session.total_questions else 0.0
    db.add(session)
    db.flush()

    apply_session_attempts_to_mastery(db, session.user_id, session.subject_id, attempts_by_topic, now)

    xp_earned = XP_BASE_AWARD + correct_count * XP_PER_CORRECT_ANSWER
    award_xp(
        db,
        session.user_id,
        source="practice_session",
        amount=xp_earned,
        metadata={"session_id": session.id},
    )
    db.flush()

    newly_earned_badges = evaluate_and_award_badges(db, session.user_id, session=session)
    session.session_metadata = {
        **session.session_metadata,
        "xp_earned": xp_earned,
        "newly_earned_badge_ids": [b.id for b in newly_earned_badges],
    }
    db.add(session)

    if daily_plan_item_id is not None:
        item = db.get(DailyPlanItem, daily_plan_item_id)
        if item is not None:
            item.status = "completed"
            db.add(item)

    return session


def get_results(db: Session, session_id: int) -> PracticeSession | None:
    return db.get(PracticeSession, session_id)
