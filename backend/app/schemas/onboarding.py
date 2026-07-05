from datetime import date

from pydantic import BaseModel

from app.schemas.subject import UserSubjectRead
from app.schemas.user import UserRead


class OnboardingSubjectInput(BaseModel):
    subject_id: int
    target_score: int | None = None
    exam_date: date | None = None
    study_minutes_per_day: int = 20


class OnboardingRequest(BaseModel):
    mode: str = "professional"
    subjects: list[OnboardingSubjectInput]


class OnboardingResponse(BaseModel):
    user: UserRead
    user_subjects: list[UserSubjectRead]
