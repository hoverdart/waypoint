"""Persist versioned guided lesson completion per learner."""
from alembic import op
import sqlalchemy as sa

revision = "20261003_lesson_progress"
down_revision = "20261003_active_curriculum"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("lesson_completions",
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), primary_key=True),
        sa.Column("unit_id", sa.Integer(), sa.ForeignKey("units.id"), primary_key=True),
        sa.Column("lesson_slug", sa.String(80), primary_key=True),
        sa.Column("revision", sa.Integer(), primary_key=True),
        sa.Column("completed_at", sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table("lesson_completions")
