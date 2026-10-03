from datetime import datetime

from pydantic import BaseModel, Field

from app.services.ai.provider import ExplainAction


class AIExplainRequest(BaseModel):
    question_id: int = Field(gt=0)
    action: ExplainAction
    selected_option_id: int | None = Field(default=None, gt=0)
    free_response_text: str | None = Field(default=None, max_length=20000)
    compare_topic: str | None = Field(default=None, max_length=300)


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
