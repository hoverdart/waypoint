from datetime import datetime, timezone

import pytest

from app.models.ai import AIUsage
from app.services.ai.explain_service import AICapExceededError, request_explanation
from app.services.ai.provider import ExplainAction, ExplainContext
from app.services.ai.usage_service import period_bounds, would_exceed_cap
from tests.factories import make_user


class FakeAIProvider:
    def __init__(self):
        self.calls = 0

    def explain(self, context):
        self.calls += 1
        return "fake explanation"


def test_period_bounds_spans_exactly_one_week():
    now = datetime(2026, 1, 7, 15, 30, tzinfo=timezone.utc)  # a Wednesday
    start, end = period_bounds(now)
    assert start.weekday() == 0
    assert (end - start).days == 7


def test_would_exceed_cap_false_when_under_limit():
    usage = AIUsage(
        user_id=1,
        period_start=datetime.now(timezone.utc),
        period_end=datetime.now(timezone.utc),
        max_allowed=5,
        free_used=3,
    )
    assert not would_exceed_cap(usage, is_premium=False)


def test_would_exceed_cap_true_at_limit():
    usage = AIUsage(
        user_id=1,
        period_start=datetime.now(timezone.utc),
        period_end=datetime.now(timezone.utc),
        max_allowed=5,
        free_used=5,
    )
    assert would_exceed_cap(usage, is_premium=False)


def test_free_and_premium_caps_tracked_separately():
    usage = AIUsage(
        user_id=1,
        period_start=datetime.now(timezone.utc),
        period_end=datetime.now(timezone.utc),
        max_allowed=5,
        free_used=5,
        premium_used=0,
    )
    assert would_exceed_cap(usage, is_premium=False)
    assert not would_exceed_cap(usage, is_premium=True)


def test_request_explanation_calls_provider_and_records_usage(db_session):
    user = make_user(db_session)
    provider = FakeAIProvider()
    context = ExplainContext(
        question_prompt="What is a limit?", correct_answer="...", action=ExplainAction.EXPLAIN_DIFFERENTLY
    )

    explanation, usage = request_explanation(
        db_session, user, context, provider, free_weekly_cap=5, premium_weekly_cap=30
    )

    assert explanation == "fake explanation"
    assert provider.calls == 1
    assert usage.free_used == 1


def test_request_explanation_raises_once_cap_exceeded_and_never_calls_provider_again(db_session):
    user = make_user(db_session)
    provider = FakeAIProvider()
    context = ExplainContext(question_prompt="Q", correct_answer="A", action=ExplainAction.ANALOGY)

    for _ in range(2):
        request_explanation(db_session, user, context, provider, free_weekly_cap=2, premium_weekly_cap=30)

    with pytest.raises(AICapExceededError):
        request_explanation(db_session, user, context, provider, free_weekly_cap=2, premium_weekly_cap=30)

    assert provider.calls == 2


def test_premium_cap_allows_more_than_free_cap(db_session):
    user = make_user(db_session)
    provider = FakeAIProvider()
    context = ExplainContext(question_prompt="Q", correct_answer="A", action=ExplainAction.WHY_WRONG)

    for _ in range(2):
        request_explanation(
            db_session, user, context, provider, free_weekly_cap=2, premium_weekly_cap=5, is_premium=True
        )

    # would have raised at call 3 if using the free cap
    _, usage = request_explanation(
        db_session, user, context, provider, free_weekly_cap=2, premium_weekly_cap=5, is_premium=True
    )
    assert usage.premium_used == 3
