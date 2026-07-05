# WayPoint Backend

FastAPI + SQLModel + Postgres backend implementing the mastery/topic-timer/daily-planner
engine, Clerk-backed auth, capped Anthropic-backed AI explanations, and the admin question
review API. See [`../docs/LOCAL_DEV.md`](../docs/LOCAL_DEV.md) for the full local dev workflow
across both services; this file covers the backend in isolation.

## Setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt   # includes requirements.txt

cp .env.example .env
# then fill in DATABASE_URL, CLERK_SECRET_KEY, ANTHROPIC_API_KEY, etc.

alembic upgrade head
python -m scripts.seed          # seeds the 6 priority AP subjects + demo question bank
uvicorn app.main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` for interactive API docs.

## Tests

Tests run against a real Postgres database (not SQLite) - the schema relies on
Postgres-specific features (JSONB, CHECK constraints, composite primary keys) that SQLite
would silently paper over. Each test runs inside a savepoint that's rolled back afterward, so
the app is free to call `.commit()` without leaking data between tests.

```bash
createdb waypoint_test   # once, if it doesn't already exist
pytest
```

## Directory layout

- `app/models/` - SQLModel table models (one module per related table group)
- `app/schemas/` - Pydantic request/response DTOs (never return table models directly)
- `app/routers/` - thin FastAPI routers; all business logic lives in `app/services/`
- `app/services/mastery/` - confidence, retention, topic mastery, topic timer, unit/subject rollups
- `app/services/planner/` - point budget, priority score, reasons, daily plan generation
- `app/services/diagnostic/`, `app/services/practice/` - diagnostic and regular practice flows
- `app/services/auth/` - `AuthProvider` protocol + Clerk adapter (swap providers by adding a new adapter)
- `app/services/ai/` - `AIProvider` protocol + Anthropic adapter, weekly usage cap enforcement
- `app/services/coach/` - weekly coach report generation
- `app/services/admin/` - admin CRUD for questions/units/topics
- `alembic/` - migrations (`alembic revision --autogenerate -m "..."` after model changes)
- `scripts/seed.py` - idempotent seed script; `scripts/seed_data/` holds the actual content
- `scripts/weekly_coach_job.py` - cron entrypoint; see `../docs/JOBS.md` for scheduling options
- `tests/unit/` - pure-function and single-service tests; `tests/integration/` - full API/flow tests

## Running the weekly coach report job manually

```bash
python -m scripts.weekly_coach_job
```
