from datetime import date

from pydantic import BaseModel, ConfigDict


class WeeklyCoachReportRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    week_start: date
    week_end: date
    summary: str
    biggest_win: str | None
    biggest_weakness: str | None
    next_week_priorities: list
    projected_score_note: str | None
