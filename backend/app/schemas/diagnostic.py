from pydantic import BaseModel, Field

from app.schemas.practice import AnswerInput, QuestionRead


class DiagnosticStartRequest(BaseModel):
    subject_id: int


class DiagnosticStartResponse(BaseModel):
    session_id: int
    session_type: str
    questions: list[QuestionRead]


class DiagnosticSubmitRequest(BaseModel):
    answers: list[AnswerInput] = Field(min_length=1, max_length=60)


class DiagnosticSubmitResponse(BaseModel):
    session_id: int
    correct_count: int
    total_questions: int
    score: float
