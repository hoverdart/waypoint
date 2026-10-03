"""Retain historical units while publishing the current curriculum.

Revision ID: 20261003_active_curriculum
Revises: fb09457c0a3d
"""
from alembic import op
import sqlalchemy as sa

revision = "20261003_active_curriculum"
down_revision = "fb09457c0a3d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("units", sa.Column("is_active", sa.Boolean(), server_default=sa.true(), nullable=False))


def downgrade():
    op.drop_column("units", "is_active")
