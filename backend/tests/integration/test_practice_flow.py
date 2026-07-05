from datetime import date

from sqlmodel import select

from app.models.mastery import SubjectMastery, TopicMastery, UnitMastery
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.gamification import XPEvent
from app.services.practice.session_service import (
    get_results,
    start_practice_session,
    submit_practice_session,
)
from app.services.practice.types import AnswerSubmission
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


def test_start_practice_session_filters_by_topic(db_session):
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=2)
    (unit, topics) = units[0]
    make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    make_mcq_question(db_session, subject.id, unit.id, topics[1].id)
    db_session.flush()

    user = make_user(db_session)
    session, questions = start_practice_session(
        db_session, user_id=user.id, subject_id=subject.id, topic_id=topics[0].id, session_type="mcq"
    )
    assert all(q.topic_id == topics[0].id for q in questions)


def test_submit_practice_session_updates_mastery_and_awards_xp(db_session):
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.flush()

    user = make_user(db_session)
    session, _ = start_practice_session(
        db_session, user_id=user.id, subject_id=subject.id, topic_id=topics[0].id, question_count=1
    )

    answers = [AnswerSubmission(question_id=question.id, selected_option_id=options["A"].id, time_seconds=45)]
    submit_practice_session(db_session, session.id, answers)
    db_session.flush()

    tm = db_session.get(TopicMastery, (user.id, topics[0].id))
    assert tm is not None
    assert tm.attempts_count == 1
    assert tm.correct_count == 1

    um = db_session.get(UnitMastery, (user.id, unit.id))
    assert um is not None

    sm = db_session.get(SubjectMastery, (user.id, subject.id))
    assert sm is not None
    assert 1 <= sm.predicted_ap_score <= 5

    xp_events = db_session.exec(
        __import__("sqlmodel").select(XPEvent).where(XPEvent.user_id == user.id)
    ).all()
    assert len(xp_events) == 1


def test_submit_practice_session_marks_daily_plan_item_completed(db_session):
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    user = make_user(db_session)

    plan = DailyPlan(user_id=user.id, plan_date=__import__("datetime").date(2026, 1, 1), point_budget=50)
    db_session.add(plan)
    db_session.flush()
    item = DailyPlanItem(
        daily_plan_id=plan.id,
        subject_id=subject.id,
        unit_id=unit.id,
        topic_id=topics[0].id,
        item_type="review",
        point_cost=25,
        priority_score=1.0,
        reason="Your mastery dropped",
    )
    db_session.add(item)
    db_session.flush()

    session, _ = start_practice_session(
        db_session, user_id=user.id, subject_id=subject.id, topic_id=topics[0].id, question_count=1
    )
    answers = [AnswerSubmission(question_id=question.id, selected_option_id=options["A"].id)]
    submit_practice_session(db_session, session.id, answers, daily_plan_item_id=item.id)
    db_session.flush()

    db_session.refresh(item)
    assert item.status == "completed"


def test_get_results_returns_completed_session(db_session):
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    user = make_user(db_session)

    session, _ = start_practice_session(
        db_session, user_id=user.id, subject_id=subject.id, topic_id=topics[0].id, question_count=1
    )
    submit_practice_session(
        db_session, session.id, [AnswerSubmission(question_id=question.id, selected_option_id=options["A"].id)]
    )

    result = get_results(db_session, session.id)
    assert result.completed_at is not None
    assert result.correct_count == 1
