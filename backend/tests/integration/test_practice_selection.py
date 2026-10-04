from datetime import datetime, timedelta
import random

from app.models.practice import PracticeSession, QuestionAttempt
from app.services.practice.session_service import start_practice_session
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


def record(db, user, subject, question, correct, day, completed=True):
    session = PracticeSession(user_id=user.id, subject_id=subject.id, session_type='mcq',
                              completed_at=datetime(2026, 1, 1) + timedelta(days=day) if completed else None)
    db.add(session)
    db.flush()
    db.add(QuestionAttempt(user_id=user.id, session_id=session.id, question_id=question.id, is_correct=correct))
    db.flush()


def test_practice_prioritizes_latest_mistakes_then_unseen_then_old_successes(db_session):
    db = db_session
    subject, units = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=1)
    unit, topics = units[0]
    questions = [make_mcq_question(db, subject.id, unit.id, topics[0].id)[0] for _ in range(5)]
    wrong, unseen, corrected, old_success, new_wrong = questions
    user = make_user(db)
    record(db, user, subject, wrong, False, 1)
    record(db, user, subject, corrected, False, 0)
    record(db, user, subject, corrected, True, 4)
    record(db, user, subject, old_success, True, 2)
    record(db, user, subject, new_wrong, True, 0)
    record(db, user, subject, new_wrong, False, 3)
    session, selected = start_practice_session(db, user.id, subject.id, question_count=5, rng=random.Random(4))
    assert [q.id for q in selected] == [q.id for q in [wrong, new_wrong, unseen, old_success, corrected]]
    assert session.session_metadata['question_ids'] == [q.id for q in selected]
    _, shorter = start_practice_session(db, user.id, subject.id, question_count=2)
    assert [q.id for q in shorter] == [wrong.id, new_wrong.id]


def test_selection_ignores_other_users_and_unfinished_attempts(db_session):
    db = db_session
    subject, units = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=1)
    unit, topics = units[0]
    questions = [make_mcq_question(db, subject.id, unit.id, topics[0].id)[0] for _ in range(3)]
    user = make_user(db)
    other = make_user(db, 'other', 'other@example.com')
    record(db, other, subject, questions[0], False, 1)
    record(db, user, subject, questions[1], False, 2, completed=False)
    baseline = list(questions)
    random.Random(12).shuffle(baseline)
    _, selected = start_practice_session(db, user.id, subject.id, rng=random.Random(12))
    assert [q.id for q in selected] == [q.id for q in baseline]


def test_skill_filter_is_exact_scoped_and_persisted(client, db_session):
    from tests.conftest import auth_header
    db = db_session
    subject, units = make_subject_with_units_topics(db, n_units=2, n_topics_per_unit=1)
    user = make_user(db)
    unit, topics = units[0]
    matching, _ = make_mcq_question(db, subject.id, unit.id, topics[0].id)
    unrelated, _ = make_mcq_question(db, subject.id, unit.id, topics[0].id)
    draft, _ = make_mcq_question(db, subject.id, unit.id, topics[0].id, validation_status='draft')
    elsewhere, _ = make_mcq_question(db, subject.id, units[1][0].id, units[1][1][0].id)
    for question in [matching, draft, elsewhere]:
        question.skill_tags = ['sourcing']
        db.add(question)
    unrelated.skill_tags = ['sourcing-other']
    db.add(unrelated)
    db.commit()
    headers = auth_header(user.auth_provider_id)
    payload = {'subject_id': subject.id, 'unit_id': unit.id, 'topic_id': topics[0].id,
               'skill_tag': 'sourcing', 'session_type': 'mcq', 'question_count': 10}
    response = client.post('/practice/start', headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert [q['id'] for q in data['questions']] == [matching.id]
    session = db.get(PracticeSession, data['session_id'])
    assert session.session_metadata == {'question_ids': [matching.id], 'skill_tag': 'sourcing'}
    empty = client.post('/practice/start', headers=headers, json={**payload, 'skill_tag': 'absent'})
    assert empty.status_code == 400
    assert 'No approved questions' in empty.text
    for invalid in ['', 'x' * 101, 'sourcing OR 1=1', ['sourcing']]:
        assert client.post('/practice/start', headers=headers, json={**payload, 'skill_tag': invalid}).status_code == 422
