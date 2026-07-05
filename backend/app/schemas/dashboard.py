from datetime import date

from pydantic import BaseModel

from app.schemas.coach import WeeklyCoachReportRead
from app.schemas.daily_plan import DailyPlanResponse
from app.schemas.gamification import BadgeRead
from app.schemas.user import UserRead


class DashboardSubjectSummary(BaseModel):
    subject_id: int
    subject_name: str
    mastery_score: float
    predicted_ap_score: int
    exam_date: date | None
    target_score: int | None


class DashboardResponse(BaseModel):
    user: UserRead
    subjects: list[DashboardSubjectSummary]
    today_plan: DailyPlanResponse | None = None
    latest_weekly_report: WeeklyCoachReportRead | None = None
    total_xp: int = 0
    streak_days: int = 0
    earned_badges: list[BadgeRead] = []
