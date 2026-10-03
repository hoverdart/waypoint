from datetime import date

from sqlmodel import select

from app.models.planner import DailyPlan, DailyPlanItem
from app.services.planner.daily_plan_generator import generate_daily_plan
from tests.factories import make_user, make_subject_with_units_topics, make_mcq_question, make_frq_question
from tests.conftest import auth_header


def setup_course(db):
    user = make_user(db)
    subject, units = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=6)
    unit, topics = units[0]
    for topic in topics[:4]:
        make_mcq_question(db, subject.id, unit.id, topic.id)
    make_mcq_question(db, subject.id, unit.id, topics[4].id, validation_status='draft')
    return user, subject, unit, topics


def test_generation_is_idempotent_and_excludes_unavailable_topics(db_session):
    user, subject, _, topics = setup_course(db_session)
    first = generate_daily_plan(db_session, user.id, subject.id, date.today())
    second = generate_daily_plan(db_session, user.id, subject.id, date.today())
    assert first.id == second.id
    assert len(db_session.exec(select(DailyPlan)).all()) == 1
    items = db_session.exec(select(DailyPlanItem)).all()
    assert items
    assert not {topics[4].id, topics[5].id} & {item.topic_id for item in items}


def test_shorter_plan_preserves_completed_work_and_item_ids(db_session):
    user, subject, _, _ = setup_course(db_session)
    plan = generate_daily_plan(db_session, user.id, subject.id, date.today(), study_minutes=60)
    items = db_session.exec(select(DailyPlanItem)).all()
    first = items[0]
    first.status = 'completed'
    db_session.add(first)
    db_session.flush()
    original_ids = {item.id for item in items}
    updated = generate_daily_plan(db_session, user.id, subject.id, date.today(), study_minutes=5)
    assert updated.id == plan.id
    db_session.refresh(first)
    assert first.status == 'completed'
    after = db_session.exec(select(DailyPlanItem)).all()
    assert {item.id for item in after} == original_ids
    assert all(item.status != 'pending' for item in after)
    assert updated.status == 'completed'
    assert sum(item.point_cost for item in after if item.status != 'skipped') <= updated.point_budget


def test_five_minute_plan_can_choose_short_review(db_session):
    user, subject, _, _ = setup_course(db_session)
    plan = generate_daily_plan(db_session, user.id, subject.id, date.today(), study_minutes=5)
    items = db_session.exec(select(DailyPlanItem)).all()
    assert len(items) == 1
    assert items[0].item_type == 'review'
    assert items[0].point_cost <= plan.point_budget


def test_frq_only_topic_gets_frq_activity(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    unit, topics = units[0]
    make_frq_question(db_session, subject.id, unit.id, topics[0].id,
                      [{'point': 'Explain', 'keywords': ['test'], 'points': 1}])
    generate_daily_plan(db_session, user.id, subject.id, date.today(), study_minutes=20)
    items = db_session.exec(select(DailyPlanItem)).all()
    assert len(items) == 1
    assert items[0].item_type == 'frq'


def test_time_budget_api_validates_input_and_returns_course(client, db_session):
    user, subject, _, _ = setup_course(db_session)
    headers = auth_header(user.auth_provider_id)
    for minutes in [-1, 0, 181]:
        assert client.post('/daily-plan/generate', headers=headers,
                           json={'subject_id': subject.id, 'study_minutes': minutes}).status_code == 422
    response = client.post('/daily-plan/generate', headers=headers,
                           json={'subject_id': subject.id, 'study_minutes': 10})
    assert response.status_code == 200
    assert response.json()['subject_id'] == subject.id
    assert response.json()['point_budget'] == 25
    assert client.post('/daily-plan/generate', headers=headers, json={'subject_id': 999999}).status_code == 404
