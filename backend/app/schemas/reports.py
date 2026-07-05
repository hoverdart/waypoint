from datetime import datetime

from pydantic import BaseModel, ConfigDict


class QuestionReportRequest(BaseModel):
    reason: str
    details: str | None = None


class QuestionReportRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    question_id: int
    reason: str
    details: str | None
    status: str
    created_at: datetime
