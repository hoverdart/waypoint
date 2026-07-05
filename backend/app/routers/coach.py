from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.coach import WeeklyCoachReport
from app.models.user import User
from app.schemas.coach import WeeklyCoachReportRead

router = APIRouter(tags=["coach"])


@router.get("/coach-report/weekly/latest", response_model=WeeklyCoachReportRead)
def get_latest_weekly_report(
    db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> WeeklyCoachReport:
    report = db.exec(
        select(WeeklyCoachReport)
        .where(WeeklyCoachReport.user_id == user.id)
        .order_by(WeeklyCoachReport.week_start.desc())
    ).first()
    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No weekly report yet")
    return report
