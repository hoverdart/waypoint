"""Cron-compatible weekly coach report job. Simple script, not a long-running
worker, per the "jobs: simple cron-compatible scripts first" requirement.

Usage: python -m scripts.weekly_coach_job
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlmodel import Session

from app.db.session import engine
from app.services.coach.weekly_report_service import last_monday, run_for_all_users


def main() -> None:
    week_start = last_monday()
    with Session(engine) as db:
        succeeded, total = run_for_all_users(db, week_start)
        print(f"Weekly coach job complete: {succeeded}/{total} succeeded.")


if __name__ == "__main__":
    main()
