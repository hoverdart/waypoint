from datetime import datetime, timezone
from sqlmodel import Field, SQLModel


class LessonCompletion(SQLModel, table=True):
    __tablename__ = "lesson_completions"
    user_id: int = Field(foreign_key="users.id", primary_key=True)
    unit_id: int = Field(foreign_key="units.id", primary_key=True)
    lesson_slug: str = Field(primary_key=True, max_length=80)
    revision: int = Field(primary_key=True)
    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
