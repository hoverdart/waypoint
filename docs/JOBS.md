# Weekly coach report

Run the report locally from `backend/`:

```bash
.venv/bin/python -m scripts.weekly_coach_job
```

It is safe to re-run: one report is upserted per user and week.

For scheduled deployments, either use the included GitHub Action
(`.github/workflows/weekly-coach-report.yml`) with a `DATABASE_URL` repository secret, or have
an HTTP scheduler call `POST /internal/jobs/weekly-coach-report` with
`x-jobs-secret: <JOBS_TRIGGER_SECRET>`.
