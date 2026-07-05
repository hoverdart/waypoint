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
