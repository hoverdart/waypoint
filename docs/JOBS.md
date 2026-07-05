# Background Jobs

WayPoint's only scheduled job for the MVP is the weekly coach report. Per the "simple
cron-compatible scripts first" requirement, there's no queue or worker process - just a plain
script (`backend/scripts/weekly_coach_job.py`) that can be invoked however is convenient.

## Running it manually

```bash
cd backend && source .venv/bin/activate
python -m scripts.weekly_coach_job
```

It loops every user, builds/upserts that user's report for the most recent Monday, and is
idempotent per `(user_id, week_start)` - safe to re-run.

## Scheduling it

Two supported paths, pick whichever fits your deployment:

**GitHub Actions** (`.github/workflows/weekly-coach-report.yml`, already included): runs on a
weekly cron schedule, checks out the repo, installs backend dependencies, and runs the script
directly against `DATABASE_URL` (set as a repo secret). No HTTP hop needed since Actions can
just execute the script.

**HTTP-only schedulers** (e.g. cron-job.org), which can only fire webhooks, not run scripts:
hit `POST /internal/jobs/weekly-coach-report` on the deployed backend with header
`x-jobs-secret: <JOBS_TRIGGER_SECRET>` (set the same value in `backend/.env` / your deployment
secrets). The endpoint runs the identical job logic and returns `{"succeeded": N, "total": M}`.

Both paths call the same `run_for_all_users()` function under the hood - the job doesn't know
or care which trigger invoked it.
