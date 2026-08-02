# Testing

Use the root scripts described in [README.md](README.md):

```bash
scripts/test-backend.sh
scripts/test-frontend.sh
scripts/test-e2e.sh
scripts/test-all.sh --e2e
```

Backend tests use the `waypoint_test` Postgres database and roll each test back. Frontend
component tests use Vitest. E2E tests use Playwright against a production Next.js build and
need real Clerk development/test keys in `frontend/.env.local`.

CI runs the backend checks, frontend checks, production build, and—when Clerk secrets are set—the E2E suite.
