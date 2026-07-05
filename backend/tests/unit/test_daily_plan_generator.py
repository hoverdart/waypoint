import random
from datetime import date

from app.models.mastery import TopicMastery
from app.models.planner import DailyPlanItem
from app.models.subject import Subject, Topic, Unit, UserSubject
from app.models.user import User
from app.services.planner.daily_plan_generator import (
    TopicCandidate,
    determine_item_type,
    generate_daily_plan,
    select_plan_items,
)
from app.services.planner.point_budget import ACTIVITY_COSTS


def _candidate(topic_id, mastery=0.5, confidence=0.5, retention=0.5, timer=1.0, ap_weight=10.0, **kw):
    return TopicCandidate(
        topic_id=topic_id,
        unit_id=1,
        subject_id=1,
        mastery_score=mastery,
        confidence_score=confidence,
        retention_score=retention,
        topic_timer=timer,
        ap_weight_midpoint_percent=ap_weight,
        **kw,
    )


def test_select_plan_items_never_exceeds_budget():
    candidates = [_candidate(i, mastery=random.random(), timer=random.uniform(0, 30)) for i in range(20)]
    rng = random.Random(1)
    selected = select_plan_items(candidates, point_budget=100, rng=rng)
    assert sum(item.point_cost for item in selected) <= 100


def test_select_plan_items_picks_highest_priority_first_when_budget_is_tight():
    weak_and_overdue = _candidate(1, mastery=0.05, timer=25.0)
    strong_and_fresh = _candidate(2, mastery=0.95, timer=0.5)
    rng = random.Random(1)
    # budget only fits one normal_topic item
    selected = select_plan_items(
        [weak_and_overdue, strong_and_fresh], point_budget=ACTIVITY_COSTS["normal_topic"], rng=rng
    )
    assert len(selected) == 1
    assert selected[0].topic_id == 1


def test_select_plan_items_empty_when_no_candidates():
    assert select_plan_items([], point_budget=100) == []


def test_determine_item_type_low_mastery_is_weakness():
    rng = random.Random(0)
    assert determine_item_type(_candidate(1, mastery=0.1), rng) == "weakness"


def test_determine_item_type_mid_mastery_is_review():
    rng = random.Random(0)
    assert determine_item_type(_candidate(1, mastery=0.45), rng) == "review"


def test_determine_item_type_high_mastery_high_ap_weight_is_challenge():
    rng = random.Random(0)
    assert (
        determine_item_type(_candidate(1, mastery=0.9, ap_weight=20.0), rng) == "challenge"
    )


def test_generate_daily_plan_end_to_end(db_session):
    user = User(auth_provider_id="planner-u1", email="planner1@example.com")
    subject = Subject(name="AP Biology", ap_exam_code="biology")
    db_session.add(user)
    db_session.add(subject)
    db_session.flush()

    unit = Unit(subject_id=subject.id, name="Cell Structure", ap_weight_min=8, ap_weight_max=11)
    db_session.add(unit)
    db_session.flush()

    topics = [Topic(unit_id=unit.id, name=f"Topic {i}") for i in range(5)]
    db_session.add_all(topics)
    db_session.flush()

    # One topic is already well-known; the rest are untouched.
    db_session.add(
        TopicMastery(
            user_id=user.id,
            topic_id=topics[0].id,
            mastery_score=0.95,
            confidence_score=0.9,
            retention_score=0.95,
            topic_timer=0.5,
        )
    )
    db_session.add(UserSubject(user_id=user.id, subject_id=subject.id, study_minutes_per_day=20))
    db_session.flush()

    plan = generate_daily_plan(
        db_session, user_id=user.id, subject_id=subject.id, plan_date=date(2026, 1, 1), rng=random.Random(7)
    )
    db_session.flush()

    assert plan.point_budget == 50  # 20 minutes -> 50 points per spec anchor

    from sqlmodel import select

    items = db_session.exec(select(DailyPlanItem).where(DailyPlanItem.daily_plan_id == plan.id)).all()
    assert len(items) > 0
    assert sum(i.point_cost for i in items) <= plan.point_budget
    for item in items:
        assert item.reason
