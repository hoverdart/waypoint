from datetime import date

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.coach import WeeklyCoachReport
from app.models.gamification import Badge, UserBadge
from app.models.mastery import SubjectMastery
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.subject import Subject, UserSubject
from app.models.user import User
from app.schemas.daily_plan import DailyPlanItemRead, DailyPlanResponse
from app.schemas.dashboard import DashboardResponse, DashboardSubjectSummary
from app.schemas.gamification import BadgeRead
from app.services.xp.streak_service import get_current_streak
from app.services.xp.xp_service import get_total_xp

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> DashboardResponse:
    user_subjects = db.exec(
        select(UserSubject).where(UserSubject.user_id == user.id, UserSubject.is_active == True)  # noqa: E712
    ).all()

    summaries = []
    for us in user_subjects:
        subject = db.get(Subject, us.subject_id)
        subject_mastery = db.get(SubjectMastery, (user.id, us.subject_id))
        summaries.append(
            DashboardSubjectSummary(
                subject_id=subject.id,
                subject_name=subject.name,
                mastery_score=subject_mastery.mastery_score if subject_mastery else 0.0,
                predicted_ap_score=subject_mastery.predicted_ap_score if subject_mastery else 1,
                exam_date=us.exam_date,
                target_score=us.target_score,
            )
        )

    today_plan_row = db.exec(
        select(DailyPlan).where(DailyPlan.user_id == user.id, DailyPlan.plan_date == date.today())
    ).first()
    today_plan = None
    if today_plan_row is not None:
        items = db.exec(
            select(DailyPlanItem).where(DailyPlanItem.daily_plan_id == today_plan_row.id)
        ).all()
        today_plan = DailyPlanResponse(
            id=today_plan_row.id,
            plan_date=today_plan_row.plan_date,
            point_budget=today_plan_row.point_budget,
            status=today_plan_row.status,
            items=[DailyPlanItemRead.model_validate(i) for i in items],
        )

    latest_report = db.exec(
        select(WeeklyCoachReport)
        .where(WeeklyCoachReport.user_id == user.id)
        .order_by(WeeklyCoachReport.week_start.desc())
    ).first()

    earned_badge_ids = db.exec(select(UserBadge.badge_id).where(UserBadge.user_id == user.id)).all()
    earned_badges = db.exec(select(Badge).where(Badge.id.in_(earned_badge_ids))).all()

    return DashboardResponse(
        user=user,
        subjects=summaries,
        today_plan=today_plan,
        latest_weekly_report=latest_report,
        total_xp=get_total_xp(db, user.id),
        streak_days=get_current_streak(db, user.id),
        earned_badges=[BadgeRead.model_validate(b) for b in earned_badges],
    )
