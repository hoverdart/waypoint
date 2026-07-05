"""Weekly (Mon-Sun UTC) AI usage tracking and cap enforcement. The cap check
itself is pure and DB-free so it's trivially unit-testable without a real
Anthropic call. `max_allowed` is snapshotted onto the row at period-creation
time so later config changes never retroactively alter a past period's cap.
"""

from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select

from app.models.ai import AIUsage

WEEK_LENGTH_DAYS = 7


def period_bounds(now: datetime) -> tuple[datetime, datetime]:
    """Monday 00:00 UTC through the following Monday 00:00 UTC."""
    start_of_week = (now - timedelta(days=now.weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    return start_of_week, start_of_week + timedelta(days=WEEK_LENGTH_DAYS)


def get_or_create_current_period(
    db: Session, user_id: int, max_allowed: int, now: datetime | None = None
) -> AIUsage:
    now = now or datetime.now(timezone.utc)
    period_start, period_end = period_bounds(now)

    usage = db.exec(
        select(AIUsage).where(
            AIUsage.user_id == user_id,
            AIUsage.period_start == period_start,
            AIUsage.period_end == period_end,
        )
    ).first()
    if usage is None:
        usage = AIUsage(
            user_id=user_id, period_start=period_start, period_end=period_end, max_allowed=max_allowed
        )
        db.add(usage)
        db.flush()
    return usage


def would_exceed_cap(usage: AIUsage, is_premium: bool) -> bool:
    used = usage.premium_used if is_premium else usage.free_used
    return used >= usage.max_allowed


def record_usage(db: Session, usage: AIUsage, is_premium: bool) -> AIUsage:
    if is_premium:
        usage.premium_used += 1
    else:
        usage.free_used += 1
    db.add(usage)
    return usage
