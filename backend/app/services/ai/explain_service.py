"""Orchestrates the capped "explain" feature: check cap -> call the configured
AIProvider -> record usage. Unit-testable end-to-end with a fake AIProvider so
tests never hit the real Anthropic API.
"""

from datetime import datetime

from sqlmodel import Session

from app.models.ai import AIUsage
from app.models.user import User
from app.services.ai.provider import AIProvider, ExplainContext
from app.services.ai.usage_service import get_or_create_current_period, record_usage, would_exceed_cap


class AICapExceededError(Exception):
    pass


def request_explanation(
    db: Session,
    user: User,
    context: ExplainContext,
    ai_provider: AIProvider,
    free_weekly_cap: int,
    premium_weekly_cap: int,
    is_premium: bool = False,
    now: datetime | None = None,
) -> tuple[str, AIUsage]:
    max_allowed = premium_weekly_cap if is_premium else free_weekly_cap
    usage = get_or_create_current_period(db, user.id, max_allowed, now)

    if would_exceed_cap(usage, is_premium):
        raise AICapExceededError("Weekly AI explanation cap reached")

    explanation = ai_provider.explain(context)
    record_usage(db, usage, is_premium)
    return explanation, usage
