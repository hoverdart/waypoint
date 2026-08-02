# Development guide

This is the only document you need to start working locally. Use the scripts at the
bottom for the normal feedback loop.

## What lives where

| Area | Start here | Purpose |
| --- | --- | --- |
| Frontend | `frontend/app/` | Next.js pages and layouts |
| UI | `frontend/components/` | Reusable interface components |
| Browser API client | `frontend/lib/api/` | Calls the FastAPI backend |
| Backend routes | `backend/app/routers/` | HTTP endpoints; keep them thin |
| Backend logic | `backend/app/services/` | Mastery, planner, practice, auth, AI, and reports |
| Data | `backend/app/models/`, `backend/alembic/` | SQLModel tables and migrations |
| Tests | `backend/tests/`, `frontend/**/*.test.*`, `frontend/e2e/` | Backend, unit/component, and browser coverage |

The normal request path is: Next.js page/component → `frontend/lib/api` → FastAPI router
→ service → Postgres. Put business rules in a backend service, not a router or React component.

## First-time setup (without Docker)

You need Node 24, Python 3.12, and PostgreSQL 16. Create two databases once:

```bash
createuser -s waypoint
psql postgres -c "ALTER USER waypoint WITH PASSWORD 'waypoint';"
createdb -O waypoint waypoint_dev
createdb -O waypoint waypoint_test
```

Then install each app:

```bash
# backend
cd backend
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
cp .env.example .env
.venv/bin/alembic upgrade head
.venv/bin/python -m scripts.seed

# frontend
cd ../frontend
npm ci
cp .env.example .env.local
```

Add your Clerk keys to `frontend/.env.local` to render the frontend and sign in. Add the
matching secret key to `backend/.env` for authenticated API calls. Anthropic is optional; it
only enables the Explain feature.

## Run the app

Use two terminals:

```bash
# terminal 1
cd backend && .venv/bin/uvicorn app.main:app --reload --port 8000

# terminal 2
cd frontend && npm run dev
```

Open `http://localhost:3000`. API docs are at `http://localhost:8000/docs`.

## Test before sharing work

Run these from the repository root:

```bash
scripts/test-backend.sh       # pytest; requires waypoint_test Postgres database
scripts/test-frontend.sh      # lint, Next route type generation, TypeScript, Vitest
scripts/test-all.sh           # backend + frontend checks
scripts/test-e2e.sh           # seed local DB, build app, and run Playwright
scripts/test-all.sh --e2e     # every local check
```

E2E needs `.env.local` with real Clerk development/test keys and a one-time Chromium install:
`cd frontend && npx playwright install chromium`. It starts the frontend and backend itself.

## Database changes

When changing a SQLModel table, make and review a migration, then apply it locally:

```bash
cd backend
.venv/bin/alembic revision --autogenerate -m "describe change"
.venv/bin/alembic upgrade head
```

## Docker option

Docker uses a separate Postgres port (`5433` by default). Copy the three templates, add Clerk
keys to `frontend/.env.local`, then run:

```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
docker compose up --build
```

Do not run Docker and the local Postgres setup against the same database configuration.

For the one scheduled job, see [JOBS.md](JOBS.md).
