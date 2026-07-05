"""Import every model module so SQLModel.metadata is fully populated before
Alembic autogenerate or create_all runs. Import this module for its side effects.
"""

from sqlmodel import SQLModel

from app.models import (  # noqa: F401
    ai,
    coach,
    gamification,
    mastery,
    planner,
    practice,
    question,
    reports,
    subject,
    user,
)

metadata = SQLModel.metadata
