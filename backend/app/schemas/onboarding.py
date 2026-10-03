from datetime import date

from typing import Literal

from pydantic import BaseModel, Field, field_validator

from app.schemas.subject import UserSubjectRead
from app.schemas.user import UserRead


class OnboardingSubjectInput(BaseModel):
    subject_id: int = Field(gt=0)
    target_score: int | None = Field(default=None, ge=1, le=5)
    exam_date: date | None = None
    study_minutes_per_day: int = Field(default=20, ge=5, le=180)


class SubjectPreferencesRequest(BaseModel):
    subjects: list[OnboardingSubjectInput] = Field(max_length=40)

    @field_validator("subjects")
    @classmethod
    def unique_subjects(cls, values):
        if len({s.subject_id for s in values}) != len(values):
            raise ValueError("Choose each course only once")
        return values


class OnboardingRequest(SubjectPreferencesRequest):
    mode: Literal["professional", "gamified"] = "professional"
    subjects: list[OnboardingSubjectInput] = Field(min_length=1, max_length=40)


class OnboardingResponse(BaseModel):
    user: UserRead
    user_subjects: list[UserSubjectRead]
