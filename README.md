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

## Repo layout

```
waypoint/
├── frontend/    Next.js App Router client
├── backend/     FastAPI service, mastery/planner engine, admin API
├── docs/        local dev + jobs/scheduling docs
├── docker-compose.yml
└── .github/workflows/weekly-coach-report.yml
```

See [`backend/README.md`](backend/README.md) for the backend's internal structure, and
[`docs/JOBS.md`](docs/JOBS.md) for how the weekly coach report is scheduled.

## Priority AP subjects

AP Calculus AB, AP Biology, AP Psychology, AP US History, AP Chemistry, AP Computer Science A.
