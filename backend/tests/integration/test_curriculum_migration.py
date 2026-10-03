import importlib

import pytest
from sqlmodel import select

from app.models.mastery import TopicMastery, UnitMastery
from app.models.practice import QuestionAttempt
from app.models.question import Question
from app.models.subject import Topic, Unit
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from scripts.seed import seed_subject, upsert_subject, upsert_unit, upsert_topic, upsert_question
from scripts.seed_data.subjects import SUBJECTS
from tests.conftest import auth_header
from tests.factories import make_user, make_mcq_question


@pytest.mark.parametrize('code,module', [('psychology', 'psychology'), ('computer-science-a', 'computer_science_a')])
def test_reseeding_legacy_curriculum_preserves_attempts_and_topic_mastery(client, db_session, code, module):
    curriculum = importlib.import_module(f'scripts.seed_data.units_topics.{module}')
    questions = importlib.import_module(f'scripts.seed_data.questions.{module}_questions').QUESTIONS
    subject_data = next(s for s in SUBJECTS if s['ap_exam_code'] == code)
    subject = upsert_subject(db_session, subject_data)
    old_topics = {}
    for data in curriculum.LEGACY_UNITS:
        unit = upsert_unit(db_session, subject.id, {k: v for k, v in data.items() if k != 'topics'})
        for topic in data['topics']:
            old_topics[topic['name']] = (unit, upsert_topic(db_session, unit.id, topic))
    # Use an existing question in a topic that changes parent units.
    data = next(q for q in questions if q['topic_name'] in old_topics
                and old_topics[q['topic_name']][0].name != q['unit_name'])
    old_unit, topic = old_topics[data['topic_name']]
    question = upsert_question(db_session, subject.id, old_unit.id, topic.id, data)
    user = make_user(db_session)
    session, _ = start_practice_session(db_session, user.id, subject.id, topic_id=topic.id, question_count=1)
    submit_practice_session(db_session, session.id, [AnswerSubmission(question_id=question.id)])
    db_session.flush()
    attempt = db_session.exec(select(QuestionAttempt).where(QuestionAttempt.session_id == session.id)).one()
    attempt_id, question_id, topic_id = attempt.id, question.id, topic.id
    before = db_session.get(TopicMastery, (user.id, topic_id)).model_dump()

    seed_subject(db_session, subject_data)
    db_session.flush()
    db_session.refresh(topic)
    db_session.refresh(question)
    assert topic.id == topic_id
    assert topic.unit_id != old_unit.id
    assert question.id == question_id
    assert question.unit_id == topic.unit_id
    assert db_session.get(QuestionAttempt, attempt_id).question_id == question_id
    after = db_session.get(TopicMastery, (user.id, topic_id))
    assert after.attempts_count == before['attempts_count']
    assert after.mastery_score == before['mastery_score']
    assert db_session.get(UnitMastery, (user.id, topic.unit_id)) is not None
    visible = client.get(f'/subjects/{subject.id}').json()['units']
    assert len(visible) == len(curriculum.UNITS)
    assert {unit['name'] for unit in visible} == {unit['name'] for unit in curriculum.UNITS}
    result = client.get(f'/practice/{session.id}/results', headers=auth_header(user.auth_provider_id))
    assert result.status_code == 200
    assert result.json()['breakdown'][0]['question_id'] == question_id
    seed_subject(db_session, subject_data)
    assert db_session.get(Topic, topic_id).unit_id == question.unit_id


def test_archived_unit_questions_are_excluded_from_new_practice_but_history_survives(client, db_session):
    subject_data = next(s for s in SUBJECTS if s['ap_exam_code'] == 'computer-science-a')
    subject = upsert_subject(db_session, subject_data)
    unit = upsert_unit(db_session, subject.id, {'name': 'Inheritance', 'ap_weight_min': 5, 'ap_weight_max': 10})
    topic = upsert_topic(db_session, unit.id, {'name': 'Creating Superclasses and Subclasses'})
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topic.id)
    user = make_user(db_session)
    old_session, _ = start_practice_session(db_session, user.id, subject.id)
    seed_subject(db_session, subject_data)
    db_session.flush()
    db_session.refresh(unit)
    assert not unit.is_active
    _, new_questions = start_practice_session(db_session, user.id, subject.id, question_count=60)
    assert question.id not in {q.id for q in new_questions}
    # A student can still finish an already-started historical session.
    submit_practice_session(db_session, old_session.id, [AnswerSubmission(question_id=question.id)])
    assert db_session.get(Question, question.id) is not None
    mastery = client.get(f'/mastery/subject/{subject.id}', headers=auth_header(user.auth_provider_id)).json()
    assert len(mastery['units']) == 4
    assert all(u['unit_name'] != 'Inheritance' for u in mastery['units'])
