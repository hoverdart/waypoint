# Testing & CI/CD

Three layers of automated testing, plus a GitHub Actions pipeline that runs all of them.

## Backend: pytest (unit + integration)

137 tests, ~92% coverage. Pure algorithm logic (mastery, planner, diagnostic, XP/streak/badges)
gets true unit tests with no DB; anything DB-touching runs against a real Postgres test database
(`waypoint_test`), isolated per test via a rolled-back savepoint - never SQLite, since the schema
leans on Postgres-only features (JSONB, composite PKs, CHECK constraints).

```bash
cd backend && source .venv/bin/activate
pytest                                                  # fast path
pytest --cov=app --cov-report=term-missing              # with coverage
```

No `.env` file or real Clerk/Anthropic keys are needed to run this suite - `FakeAuthProvider`
and a fake `AIProvider` stand in for the real integrations. `tests/unit/test_clerk_auth_provider.py`
is worth knowing about specifically: it's a regression test for a real bug found during
development (a lowercase `authorization` header key silently broke every Clerk-authenticated
request, since `clerk_backend_api` reads the exact-case `Authorization` key from a plain dict).

## Frontend unit/component tests: Vitest + React Testing Library

46 tests across 13 files, focused on what's actually unit-testable: pure logic (XP/level
calculation), interactive client components (confidence rating, MCQ option selection, plan item
cards), and the shared `apiFetch` client. Per Next.js's own testing guidance, `async` Server
Components (most of this app's pages) aren't unit-tested - they're covered by the E2E suite
instead.

```bash
cd frontend
npm test                  # single run
npm run test:watch        # watch mode
npm run test:coverage     # with a coverage report
```

## Frontend E2E tests: Playwright

Two spec files under `frontend/e2e/`:

- **`unauthenticated.spec.ts`** - landing page content, Clerk's sign-in/sign-up forms rendering,
  and every protected route correctly redirecting to `/login`. Runs with zero configuration.
- **`golden-path.spec.ts`** - the full authenticated flow: onboarding → dashboard → daily plan
  generation → diagnostic → results. Creates a throwaway Clerk user via the Backend API, signs
  in programmatically with `@clerk/testing` (no UI form-filling, no OTP), and cleans the user up
  afterward. **Requires `CLERK_SECRET_KEY`** (a real Clerk dev/test instance, not keyless mode -
  see below) and skips itself with a clear message if that isn't set.

Playwright manages both the frontend (`npm run build && npm run start` - tested against the
production build, per Next.js's own recommendation) and the backend (`uvicorn`) as `webServer`
processes, so a single command runs the whole stack:

```bash
cd frontend
npx playwright install --with-deps chromium   # one-time browser install
npm run test:e2e
```

### Why the authenticated spec needs a real Clerk instance

`<ClerkProvider>` wraps this app's entire layout - every route, including the public landing
page - needs Clerk to actually initialize to render at all. Locally, `.env.local` already has
either your own real keys or Clerk's auto-provisioned "keyless" dev credentials, so this works
out of the box. In a fresh CI checkout there's no `.clerk/.tmp/keyless.json` to fall back to
(it's gitignored and machine-specific), so the E2E job needs real credentials supplied as
secrets - see below.

Clerk's own dev-instance banner warns that free/dev instances have "strict usage limits." If a
run fails with the sign-in widget never loading, it's usually this, not a real bug - re-run it
(the config already retries once locally, twice in CI).

## CI/CD: GitHub Actions (`.github/workflows/ci.yml`)

Runs on every push/PR to `main`/`master`. Four jobs:

| Job | What it does | Needs secrets? |
|---|---|---|
| `backend-tests` | `pytest --cov` against a Postgres service container | No |
| `frontend-checks` | lint, `tsc --noEmit`, `npm run test:coverage` | No |
| `frontend-build` | `npm run build` (no env vars needed - every route is dynamic, none are statically prerendered) | No |
| `e2e` | Full Playwright suite against a migrated + seeded Postgres database | **Yes** |

The `e2e` job (and a small `check-e2e-secrets` job that gates it) only runs once you've added two
repository secrets, since `<ClerkProvider>` needs a real Clerk instance to boot the app at all in
production mode:

1. In your Clerk dashboard, create (or reuse) a **development** instance you're fine with tests
   creating and deleting throwaway users on.
2. In GitHub: **Settings → Secrets and variables → Actions**, add:
   - `E2E_CLERK_PUBLISHABLE_KEY` - the instance's publishable key (`pk_test_...`)
   - `E2E_CLERK_SECRET_KEY` - the instance's secret key (`sk_test_...`)

Until those are set, `e2e` shows as **skipped** (not failed) - the other three jobs are fully
self-sufficient and will pass with zero configuration.

The weekly coach report job (`.github/workflows/weekly-coach-report.yml`) is separate and needs
its own `DATABASE_URL` secret pointed at your real deployed database - see
[`docs/JOBS.md`](JOBS.md).
