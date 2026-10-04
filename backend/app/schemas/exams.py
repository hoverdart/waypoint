from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.practice import AnswerInput, QuestionRead


class ExamStartRequest(BaseModel):
    subject_id: int = Field(gt=0)
    form_id: str = Field(min_length=1, max_length=100)
    time_multiplier: Literal[1.0, 1.5, 2.0] = 1.0


class ExamDraftRequest(BaseModel):
    answers: list[AnswerInput] = Field(default_factory=list, max_length=60)
    current_index: int = Field(default=0, ge=0, le=59)
    expected_revision: int = Field(ge=0)


class ExamSectionSummary(BaseModel):
    title: str
    duration_seconds: int
    question_count: int
    score_weight: float
    instructions: str


class ExamFormRead(BaseModel):
    form_id: str
    title: str
    source_url: str
    sections: list[ExamSectionSummary]
    available: bool


class ExamSectionRead(ExamSectionSummary):
    index: int
    status: Literal['ready', 'active', 'expired', 'finished']
    started_at: datetime | None
    deadline: datetime | None
    finished_at: datetime | None


class ExamSessionRead(BaseModel):
    session_id: int
    subject_id: int
    title: str
    form_id: str
    time_multiplier: float
    server_time: datetime
    current_section: int
    completed: bool
    sections: list[ExamSectionRead]
    questions: list[QuestionRead]
    answers: list[AnswerInput]
    current_index: int
    revision: int
    break_policy: str = 'Practice allows an untimed break between sections. A section clock continues if you leave the page.'
