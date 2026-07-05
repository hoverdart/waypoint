"""HTTP trigger for schedulers that can only fire webhooks (e.g.
cron-job.org), guarded by a shared secret. GitHub Actions runs the same job
via scripts/weekly_coach_job.py directly instead - see docs/JOBS.md.
"""

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlmodel import Session

from app.config import Settings, get_settings
from app.db.session import get_db
from app.services.coach.weekly_report_service import last_monday, run_for_all_users

router = APIRouter(prefix="/internal/jobs", tags=["internal"])


@router.post("/weekly-coach-report")
def trigger_weekly_coach_report(
    x_jobs_secret: str | None = Header(default=None),
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> dict:
    if not settings.jobs_trigger_secret or x_jobs_secret != settings.jobs_trigger_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing job trigger secret"
        )

    succeeded, total = run_for_all_users(db, last_monday())
    return {"succeeded": succeeded, "total": total}
