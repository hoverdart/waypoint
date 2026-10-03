import pytest
from sqlmodel import select

from app.core.exceptions import ConflictError, DomainError
from app.models.gamification import XPEvent
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user
from tests.conftest import auth_header


@pytest.fixture
def practice(db_session):
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    unit, topics = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    user = make_user(db_session)
    session, _ = start_practice_session(db_session, user.id, subject.id, question_count=1)
    answer = AnswerSubmission(question_id=question.id, selected_option_id=options['A'].id)
    return user, session, answer, question


def test_replay_cannot_award_xp_twice(db_session, practice):
    user, session, answer, _ = practice
    submit_practice_session(db_session, session.id, [answer])
    with pytest.raises(ConflictError):
        submit_practice_session(db_session, session.id, [answer])
    assert len(db_session.exec(select(XPEvent).where(XPEvent.user_id == user.id)).all()) == 1


@pytest.mark.parametrize('kind', ['duplicate', 'missing', 'foreign'])
def test_invalid_question_sets_are_rejected_before_rewards(db_session, practice, kind):
    user, session, answer, _ = practice
    answers = {'duplicate': [answer, answer], 'missing': [],
               'foreign': [AnswerSubmission(question_id=999999)]}[kind]
    with pytest.raises(DomainError):
        submit_practice_session(db_session, session.id, answers)
    assert session.completed_at is None
    assert not db_session.exec(select(XPEvent).where(XPEvent.user_id == user.id)).all()


def test_option_from_another_question_is_rejected(db_session, practice):
    _, session, answer, question = practice
    _, options = make_mcq_question(db_session, question.subject_id, question.unit_id, question.topic_id)
    answer.selected_option_id = options['A'].id
    with pytest.raises(DomainError, match='option'):
        submit_practice_session(db_session, session.id, [answer])


def test_diagnostic_endpoint_rejects_another_users_session(client, db_session, practice):
    _, session, answer, _ = practice
    other = make_user(db_session, auth_provider_id='other_student', email='other@example.com')
    response = client.post(f'/diagnostic/{session.id}/submit',
        headers=auth_header(other.auth_provider_id),
        json={'answers': [{'question_id': answer.question_id}]})
    assert response.status_code == 404
    assert session.completed_at is None


@pytest.mark.parametrize('payload', [
    {'question_count': 0}, {'question_count': -1}, {'question_count': 10000},
    {'session_type': 'diagnostic'},
])
def test_practice_input_bounds(client, practice, payload):
    user, session, _, _ = practice
    response = client.post('/practice/start', headers=auth_header(user.auth_provider_id),
                           json={'subject_id': session.subject_id, **payload})
    assert response.status_code == 422


def test_cannot_complete_another_users_plan(db_session, practice):
    from datetime import date
    from app.core.exceptions import NotFoundError
    from app.models.planner import DailyPlan, DailyPlanItem
    _, session, answer, question = practice
    other = make_user(db_session, auth_provider_id='plan_owner', email='owner@example.com')
    plan = DailyPlan(user_id=other.id, plan_date=date.today(), point_budget=20)
    db_session.add(plan)
    db_session.flush()
    item = DailyPlanItem(daily_plan_id=plan.id, subject_id=question.subject_id,
                        unit_id=question.unit_id, topic_id=question.topic_id,
                        item_type='review', point_cost=10, priority_score=1, reason='Review')
    db_session.add(item)
    db_session.flush()
    with pytest.raises(NotFoundError):
        submit_practice_session(db_session, session.id, [answer], daily_plan_item_id=item.id)
    assert item.status == 'pending'
    assert session.completed_at is None
