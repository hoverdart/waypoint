"""Pure day-walk streak calculation, shared by the weekly coach report and
live badge/dashboard queries so the two never drift apart."""

from datetime import date, datetime, timedelta

from sqlmodel import Session, select

from app.models.practice import PracticeSession

DEFAULT_STREAK_LOOKBACK_DAYS = 90


def compute_streak_days(session_dates: set[date], as_of: date) -> int:
    """Consecutive days with >=1 completed session, ending at `as_of` (or the
    day before, if nothing has happened yet today)."""
    cursor = as_of if as_of in session_dates else as_of - timedelta(days=1)
    streak = 0
    while cursor in session_dates:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def get_current_streak(
    db: Session, user_id: int, as_of: date | None = None, lookback_days: int = DEFAULT_STREAK_LOOKBACK_DAYS
) -> int:
    as_of = as_of or date.today()
    lookback_start = datetime(as_of.year, as_of.month, as_of.day) - timedelta(days=lookback_days)
    sessions = db.exec(
        select(PracticeSession).where(
            PracticeSession.user_id == user_id,
            PracticeSession.completed_at.is_not(None),
            PracticeSession.completed_at >= lookback_start,
        )
    ).all()
    session_dates = {s.completed_at.date() for s in sessions}
    return compute_streak_days(session_dates, as_of)
