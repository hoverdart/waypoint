from sqlmodel import Session, select

from app.models.planner import DailyPlan, DailyPlanItem


def update_plan_status(db: Session, plan: DailyPlan) -> None:
    statuses = db.exec(select(DailyPlanItem.status).where(DailyPlanItem.daily_plan_id == plan.id)).all()
    if not statuses:
        plan.status = "pending"
    elif "pending" in statuses:
        plan.status = "active" if "completed" in statuses else "pending"
    else:
        plan.status = "completed" if "completed" in statuses else "skipped"
    db.add(plan)
