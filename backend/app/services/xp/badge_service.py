"""Evaluates badge rules right after a practice/diagnostic session completes.
Each badge row's `rule_json` names a `type` that maps to one evaluator below,
so adding a new badge is just a seed-data row plus (if it's a genuinely new
rule shape) one more evaluator function - no schema change needed.
"""

from dataclasses import dataclass
from typing import Callable

from sqlmodel import Session, func, select

from app.models.gamification import Badge, UserBadge, XPEvent
from app.models.practice import PracticeSession
from app.services.xp.streak_service import get_current_streak


@dataclass
class BadgeContext:
    session: PracticeSession | None
    total_xp: int
    streak_days: int
    sessions_completed: int


def _first_session(ctx: BadgeContext, rule: dict) -> bool:
    return ctx.sessions_completed >= 1


def _streak(ctx: BadgeContext, rule: dict) -> bool:
    return ctx.streak_days >= rule["days"]


def _total_xp(ctx: BadgeContext, rule: dict) -> bool:
    return ctx.total_xp >= rule["amount"]


def _perfect_session(ctx: BadgeContext, rule: dict) -> bool:
    session = ctx.session
    return (
        session is not None
        and session.total_questions >= rule.get("min_questions", 5)
        and session.correct_count == session.total_questions
    )


def _diagnostic_complete(ctx: BadgeContext, rule: dict) -> bool:
    return ctx.session is not None and ctx.session.session_type == "diagnostic"


RULE_EVALUATORS: dict[str, Callable[[BadgeContext, dict], bool]] = {
    "first_session": _first_session,
    "streak": _streak,
    "total_xp": _total_xp,
    "perfect_session": _perfect_session,
    "diagnostic_complete": _diagnostic_complete,
}


def evaluate_and_award_badges(
    db: Session, user_id: int, session: PracticeSession | None = None
) -> list[Badge]:
    """Call after a session's XP has already been awarded (and flushed) so
    total_xp reflects this session. Returns newly-earned badges, if any."""
    already_earned_ids = set(
        db.exec(select(UserBadge.badge_id).where(UserBadge.user_id == user_id)).all()
    )
    candidates = [b for b in db.exec(select(Badge)).all() if b.id not in already_earned_ids]
    if not candidates:
        return []

    total_xp = db.exec(
        select(func.coalesce(func.sum(XPEvent.amount), 0)).where(XPEvent.user_id == user_id)
    ).one()
    streak_days = get_current_streak(db, user_id)
    sessions_completed = db.exec(
        select(func.count())
        .select_from(PracticeSession)
        .where(PracticeSession.user_id == user_id, PracticeSession.completed_at.is_not(None))
    ).one()

    ctx = BadgeContext(
        session=session,
        total_xp=int(total_xp),
        streak_days=streak_days,
        sessions_completed=sessions_completed,
    )

    newly_earned = []
    for badge in candidates:
        evaluator = RULE_EVALUATORS.get(badge.rule_json.get("type"))
        if evaluator is not None and evaluator(ctx, badge.rule_json):
            db.add(UserBadge(user_id=user_id, badge_id=badge.id))
            newly_earned.append(badge)
    return newly_earned
