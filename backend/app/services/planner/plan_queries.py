from datetime import date

from sqlmodel import Session, select
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.subject import UserSubject


def visible_today_plans(db: Session, user_id: int) -> list[DailyPlan]:
    removed = set(db.exec(select(UserSubject.subject_id).where(
        UserSubject.user_id == user_id, UserSubject.is_active == False,
    )).all())
    plans = db.exec(select(DailyPlan).where(
        DailyPlan.user_id == user_id, DailyPlan.plan_date == date.today(),
    ).order_by(DailyPlan.id)).all()
    visible = []
    for plan in plans:
        subject_id = plan.generated_reason.get("subject_id")
        if subject_id is None:
            subject_id = db.exec(select(DailyPlanItem.subject_id).where(DailyPlanItem.daily_plan_id == plan.id)).first()
        if subject_id not in removed:
            visible.append(plan)
    return visible
