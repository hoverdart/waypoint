from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class DailyPlanItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    unit_id: int
    topic_id: int
    item_type: str
    point_cost: int
    priority_score: float
    reason: str
    status: str


class DailyPlanRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    plan_date: date
    point_budget: int
    subject_id: int | None = None
    status: str


class DailyPlanResponse(DailyPlanRead):
    items: list[DailyPlanItemRead] = []


class GeneratePlanRequest(BaseModel):
    subject_id: int = Field(gt=0)
    study_minutes: int | None = Field(default=None, ge=5, le=180)


class DailyPlanItemUpdateRequest(BaseModel):
    status: Literal["pending", "completed", "skipped"]
