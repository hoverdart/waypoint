"""Python-side enums for app logic and Pydantic schemas.

These are NOT mapped to native Postgres ENUM types. Every enum-like column is
stored as VARCHAR with a DB-level CHECK constraint (see the Alembic migration) so
new values can be added without an ALTER TYPE migration during early iteration.
"""

from enum import Enum


class UserMode(str, Enum):
    PROFESSIONAL = "professional"
    GAMIFIED = "gamified"


class QuestionType(str, Enum):
    MCQ = "mcq"
    FRQ = "frq"


class QuestionSource(str, Enum):
    GENERATED = "generated"
    IMPORTED = "imported"
    HUMAN_WRITTEN = "human_written"


class ValidationStatus(str, Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_REVIEW = "needs_review"


class SessionType(str, Enum):
    DIAGNOSTIC = "diagnostic"
    DAILY_PLAN = "daily_plan"
    MCQ = "mcq"
    FRQ = "frq"
    TIMED = "timed"


class PlanStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class PlanItemType(str, Enum):
    REVIEW = "review"
    WEAKNESS = "weakness"
    CALIBRATION = "calibration"
    FRQ = "frq"
    CHALLENGE = "challenge"


class PlanItemStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class QuestionReportStatus(str, Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    DISMISSED = "dismissed"
