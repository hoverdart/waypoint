"""Shared column helpers used across model modules."""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# JSON on SQLite (tests can fall back to it), JSONB on Postgres/Neon.
JSONVariant = sa.JSON().with_variant(postgresql.JSONB(), "postgresql")
