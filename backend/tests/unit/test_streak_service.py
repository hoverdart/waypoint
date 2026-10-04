from datetime import datetime, timedelta, timezone

from app.models.practice import PracticeSession
from app.services.xp.streak_service import get_current_streak
from tests.factories import make_subject_with_units_topics, make_user


def _make_subject(db):
    subject, _ = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=1)
    return subject.id


def _completed_session(db, user_id, subject_id, completed_at):
    session = PracticeSession(
        user_id=user_id, subject_id=subject_id, session_type="mcq", total_questions=1, completed_at=completed_at
    )
    db.add(session)
    db.flush()
    return session


def test_get_current_streak_counts_consecutive_days(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    now = datetime.now(timezone.utc)
    _completed_session(db_session, user.id, subject_id, now)
    _completed_session(db_session, user.id, subject_id, now - timedelta(days=1))
    _completed_session(db_session, user.id, subject_id, now - timedelta(days=2))
    db_session.flush()

    assert get_current_streak(db_session, user.id, as_of=now.date()) == 3


def test_get_current_streak_zero_with_no_sessions(db_session):
    user = make_user(db_session)
    assert get_current_streak(db_session, user.id) == 0


def test_get_current_streak_ignores_sessions_outside_lookback(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    now = datetime.now(timezone.utc)
    _completed_session(db_session, user.id, subject_id, now - timedelta(days=200))
    db_session.flush()

    assert get_current_streak(db_session, user.id, as_of=now.date(), lookback_days=90) == 0


def test_default_streak_day_matches_utc_completion_dates_when_host_day_differs(db_session, monkeypatch):
    from datetime import date
    from app.services.xp import streak_service
    fixed = datetime(2026, 10, 4, 0, 5, tzinfo=timezone.utc)
    class Clock(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed if tz else fixed.replace(tzinfo=None)
    class LocalDate(date):
        @classmethod
        def today(cls):
            return date(2026, 10, 3)
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    for days in (0, 1, 2):
        _completed_session(db_session, user.id, subject_id, fixed - timedelta(days=days))
    monkeypatch.setattr(streak_service, 'datetime', Clock)
    monkeypatch.setattr(streak_service, 'date', LocalDate)
    assert get_current_streak(db_session, user.id) == 3


def test_streak_normalizes_database_timezone_before_grouping_days(db_session):
    user = make_user(db_session)
    subject_id = _make_subject(db_session)
    eastern = timezone(timedelta(hours=-4))
    fixed = datetime(2026, 10, 4, 0, 5, tzinfo=timezone.utc)
    sessions = [
        _completed_session(db_session, user.id, subject_id, (fixed - timedelta(days=days)).astimezone(eastern))
        for days in (0, 1, 2)
    ]
    assert all(session.completed_at.hour == 20 for session in sessions)
    assert get_current_streak(db_session, user.id, as_of=fixed.date()) == 3
    db_session.expire_all()
    assert get_current_streak(db_session, user.id, as_of=fixed.date()) == 3
