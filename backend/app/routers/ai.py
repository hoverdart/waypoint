from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.config import Settings, get_settings
from app.db.session import get_db
from app.dependencies import get_ai_provider, get_current_user
from app.models.question import Question, QuestionOption
from app.models.user import User
from app.schemas.ai import AIExplainRequest, AIExplainResponse, AIUsageResponse
from app.services.ai.explain_service import AICapExceededError, request_explanation
from app.services.ai.provider import AIProvider, ExplainContext
from app.services.ai.usage_service import get_or_create_current_period

router = APIRouter(tags=["ai"])

# Nobody is marked premium yet (no billing/tier column exists) - the cap
# machinery is fully wired so flipping this to a real user.tier check later is
# a one-line change.
IS_PREMIUM_PLACEHOLDER = False


@router.post("/ai/explain", response_model=AIExplainResponse)
def explain(
    payload: AIExplainRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    settings: Settings = Depends(get_settings),
    ai_provider: AIProvider = Depends(get_ai_provider),
) -> AIExplainResponse:
    question = db.get(Question, payload.question_id)
    if question is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    student_answer = payload.free_response_text
    if payload.selected_option_id is not None:
        option = db.get(QuestionOption, payload.selected_option_id)
        student_answer = option.text if option else None

    context = ExplainContext(
        question_prompt=question.prompt,
        correct_answer=question.correct_answer,
        student_answer=student_answer,
        action=payload.action,
        compare_topic=payload.compare_topic,
    )

    try:
        explanation, usage = request_explanation(
            db,
            user,
            context,
            ai_provider,
            free_weekly_cap=settings.ai_free_weekly_cap,
            premium_weekly_cap=settings.ai_premium_weekly_cap,
            is_premium=IS_PREMIUM_PLACEHOLDER,
        )
    except AICapExceededError as exc:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=str(exc)) from exc

    db.commit()
    return AIExplainResponse(
        explanation=explanation,
        free_used=usage.free_used,
        premium_used=usage.premium_used,
        max_allowed=usage.max_allowed,
    )


@router.get("/ai/usage", response_model=AIUsageResponse)
def get_usage(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    settings: Settings = Depends(get_settings),
) -> AIUsageResponse:
    max_allowed = settings.ai_premium_weekly_cap if IS_PREMIUM_PLACEHOLDER else settings.ai_free_weekly_cap
    usage = get_or_create_current_period(db, user.id, max_allowed)
    db.commit()
    return AIUsageResponse(
        free_used=usage.free_used,
        premium_used=usage.premium_used,
        max_allowed=usage.max_allowed,
        period_start=usage.period_start,
        period_end=usage.period_end,
    )
