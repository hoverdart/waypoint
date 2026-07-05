from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.user import User
from app.schemas.daily_plan import (
    DailyPlanItemRead,
    DailyPlanItemUpdateRequest,
    DailyPlanResponse,
    GeneratePlanRequest,
)
from app.services.planner.daily_plan_generator import generate_daily_plan

router = APIRouter(tags=["daily-plan"])


def _to_response(db: Session, plan: DailyPlan) -> DailyPlanResponse:
    items = db.exec(select(DailyPlanItem).where(DailyPlanItem.daily_plan_id == plan.id)).all()
    return DailyPlanResponse(
        id=plan.id,
        plan_date=plan.plan_date,
        point_budget=plan.point_budget,
        status=plan.status,
        items=[DailyPlanItemRead.model_validate(i) for i in items],
    )


@router.post("/daily-plan/generate", response_model=DailyPlanResponse)
def generate_plan(
    payload: GeneratePlanRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> DailyPlanResponse:
    plan = generate_daily_plan(
        db, user_id=user.id, subject_id=payload.subject_id, plan_date=date.today()
    )
    db.commit()
    db.refresh(plan)
    return _to_response(db, plan)


@router.get("/daily-plan/today", response_model=list[DailyPlanResponse])
def get_today_plan(
    db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> list[DailyPlanResponse]:
    plans = db.exec(
        select(DailyPlan).where(DailyPlan.user_id == user.id, DailyPlan.plan_date == date.today())
    ).all()
    return [_to_response(db, plan) for plan in plans]


@router.patch("/daily-plan/items/{item_id}", response_model=DailyPlanResponse)
def update_plan_item(
    item_id: int,
    payload: DailyPlanItemUpdateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> DailyPlanResponse:
    item = db.get(DailyPlanItem, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan item not found")
    plan = db.get(DailyPlan, item.daily_plan_id)
    if plan is None or plan.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan item not found")

    item.status = payload.status
    db.add(item)
    db.commit()
    db.refresh(plan)
    return _to_response(db, plan)
