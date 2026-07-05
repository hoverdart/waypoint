"""Awards XP for completed activity. XP is always recorded regardless of the
user's mode - the frontend decides whether to surface XP UI based on
`users.mode`, so this service stays mode-agnostic.
"""

from sqlmodel import Session, func, select

from app.models.gamification import XPEvent


def award_xp(db: Session, user_id: int, source: str, amount: int, metadata: dict | None = None) -> XPEvent:
    event = XPEvent(user_id=user_id, source=source, amount=amount, event_metadata=metadata or {})
    db.add(event)
    return event


def get_total_xp(db: Session, user_id: int) -> int:
    total = db.exec(select(func.coalesce(func.sum(XPEvent.amount), 0)).where(XPEvent.user_id == user_id)).one()
    return int(total)
