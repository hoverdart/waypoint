from datetime import date, timedelta

from app.models.subject import UserSubject
from app.services.coach.weekly_report_service import build_weekly_report, last_monday
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


def test_last_monday_is_always_a_monday():
    for offset in range(7):
        day = date(2026, 1, 5) + timedelta(days=offset)  # Jan 5 2026 is a Monday
        assert last_monday(day).weekday() == 0


def test_build_weekly_report_reflects_this_weeks_activity(db_session):
    user = make_user(db_session)
    subject, units = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.add(UserSubject(user_id=user.id, subject_id=subject.id))
    db_session.flush()

    session, _ = start_practice_session(
        db_session, user_id=user.id, subject_id=subject.id, topic_id=topics[0].id, question_count=1
    )
    submit_practice_session(
        db_session, session.id, [AnswerSubmission(question_id=question.id, selected_option_id=options["A"].id)]
    )
    db_session.flush()

    week_start = last_monday()
    report = build_weekly_report(db_session, user.id, week_start)

    assert report.week_start == week_start
    assert "1 practice session" in report.summary
    assert report.biggest_win is not None


def test_build_weekly_report_is_idempotent_per_week(db_session):
    user = make_user(db_session)
    week_start = last_monday()

    first = build_weekly_report(db_session, user.id, week_start)
    db_session.flush()
    first_id = first.id

    second = build_weekly_report(db_session, user.id, week_start)
    db_session.flush()

    assert second.id == first_id


def test_internal_trigger_requires_correct_secret(client, monkeypatch):
    from app.config import get_settings

    monkeypatch.setattr(get_settings(), "jobs_trigger_secret", "correct-secret")

    resp = client.post("/internal/jobs/weekly-coach-report", headers={"x-jobs-secret": "wrong"})
    assert resp.status_code == 401

    resp_ok = client.post("/internal/jobs/weekly-coach-report", headers={"x-jobs-secret": "correct-secret"})
    assert resp_ok.status_code == 200
    assert "succeeded" in resp_ok.json()
