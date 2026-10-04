"""Add optional structured evidence tables to questions."""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '20261004_question_tables'
down_revision = '20261003_lesson_progress'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('questions', sa.Column('data_table', sa.JSON().with_variant(postgresql.JSONB(), 'postgresql'), nullable=True))


def downgrade():
    op.drop_column('questions', 'data_table')
