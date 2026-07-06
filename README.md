# WayPoint

*"Every day, we tell students exactly what to study next to maximize their AP score."*

WayPoint is a deterministic study GPS for AP exam prep: a mastery/topic-timer/priority-scoring
engine drives a daily plan, backed by MCQ/FRQ practice, diagnostics, deterministic explanations,
a capped AI "explain" fallback, and a weekly coach report. Two UI layers - Professional and
Gamified - sit on the same backend.

## Stack

- **Frontend**: Next.js (App Router) + TypeScript + Tailwind CSS v4 + shadcn/ui + Clerk
- **Backend**: FastAPI + Python + Pydantic + SQLModel
- **Database**: Postgres (Neon-ready)
- **AI**: Anthropic Claude, strictly for the capped on-demand "explain" feature - question
  generation is offline/manual, never live

## Quickstart

See [`docs/LOCAL_DEV.md`](docs/LOCAL_DEV.md) for full setup (Docker-free and Docker Compose
paths). Short version:

```bash
# backend
cd backend && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env   # fill in CLERK_SECRET_KEY / ANTHROPIC_API_KEY when available
alembic upgrade head && python -m scripts.seed
uvicorn app.main:app --reload --port 8000

# frontend (separate terminal)
cd frontend && cp .env.example .env.local && npm install && npm run dev
```

Backend API docs: `http://localhost:8000/docs`. Frontend: `http://localhost:3000`.

## Testing & CI/CD

```bash
cd backend && pytest                    # 137 tests, ~92% coverage
cd frontend && npm test                 # 46 unit/component tests (Vitest)
cd frontend && npm run test:e2e         # Playwright E2E (see docs/TESTING.md for setup)
```

Every push/PR runs the full suite via [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
The E2E job needs two repo secrets (`E2E_CLERK_PUBLISHABLE_KEY`, `E2E_CLERK_SECRET_KEY`) to run -
see [`docs/TESTING.md`](docs/TESTING.md) for the full breakdown of what each job does and how to
enable it.

## Repo layout

```
waypoint/
├── frontend/    Next.js App Router client
├── backend/     FastAPI service, mastery/planner engine, admin API
├── docs/        local dev + jobs/scheduling docs
├── docker-compose.yml
└── .github/workflows/weekly-coach-report.yml
```

See [`backend/README.md`](backend/README.md) for the backend's internal structure,
[`docs/JOBS.md`](docs/JOBS.md) for how the weekly coach report is scheduled, and
[`docs/TESTING.md`](docs/TESTING.md) for the test suites and CI/CD pipeline.

## Priority AP subjects

AP Calculus AB, AP Biology, AP Psychology, AP US History, AP Chemistry, AP Computer Science A.

## Deploying

This is a monorepo with the Next.js app under `frontend/`, not at the repo root - most hosts
need to be told that explicitly:

- **Frontend (Vercel or similar)**: set the project's **root directory** to `frontend`. Set
  `NEXT_PUBLIC_API_BASE_URL` to wherever the backend below actually runs, plus real (non-keyless)
  `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`, `CLERK_SECRET_KEY`, `NEXT_PUBLIC_CLERK_SIGN_IN_URL=/login`,
  and `NEXT_PUBLIC_CLERK_SIGN_UP_URL=/signup`.
- **Backend + Postgres**: Vercel doesn't run long-lived Python/Postgres services - deploy
  `backend/` to something that does (Railway, Fly.io, Render, a plain VM via the included
  `docker-compose.yml`) and point the frontend's `NEXT_PUBLIC_API_BASE_URL` at it. Set
  `CORS_ALLOWED_ORIGINS` on the backend to your deployed frontend's real origin.
