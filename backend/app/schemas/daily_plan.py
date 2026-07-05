from datetime import date

from pydantic import BaseModel, ConfigDict


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
    status: str


class DailyPlanResponse(DailyPlanRead):
    items: list[DailyPlanItemRead] = []


class GeneratePlanRequest(BaseModel):
    subject_id: int


class DailyPlanItemUpdateRequest(BaseModel):
    status: str
