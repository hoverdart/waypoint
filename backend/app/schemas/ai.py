from datetime import datetime

from pydantic import BaseModel

from app.services.ai.provider import ExplainAction


class AIExplainRequest(BaseModel):
    question_id: int
    action: ExplainAction
    selected_option_id: int | None = None
    free_response_text: str | None = None
    compare_topic: str | None = None


class AIExplainResponse(BaseModel):
    explanation: str
    free_used: int
    premium_used: int
    max_allowed: int


class AIUsageResponse(BaseModel):
    free_used: int
    premium_used: int
    max_allowed: int
    period_start: datetime
    period_end: datetime
