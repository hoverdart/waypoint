# WayPoint frontend

Next.js App Router, TypeScript, Tailwind, shadcn, and Clerk. See
[local setup](../docs/LOCAL_DEV.md) for the full frontend/backend workflow.

```sh
npm install
npm run dev
```

Configure `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`, `CLERK_SECRET_KEY`, and
`NEXT_PUBLIC_API_BASE_URL` in an ignored `.env.local` file. The API URL is
embedded at build time; rebuild after changing it. Authentication uses the
local `/login` and `/signup` routes.

## Verification

```sh
npm test
npm run lint
npx tsc --noEmit
npm run build
```

Browser tests run production builds on dedicated ports 3109 (frontend) and
8109 (backend), configurable through `E2E_FRONTEND_PORT` and `E2E_BACKEND_PORT`.
They fail if those ports are occupied rather than reusing an unrelated app.
Provide a migrated, seeded, disposable PostgreSQL database with `DATABASE_URL`:

```sh
npx playwright install chromium
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/waypoint_e2e npm run test:e2e
```

The suite loads `.env.local` then `.env`. With Clerk development keys it creates
and removes a temporary Clerk user, verifying onboarding, diagnostics, course
practice, saved-answer recovery, results, and daily-plan completion. Study data
remains in the disposable local database. Without a Clerk secret the authenticated
spec is skipped; that run alone does not verify the full application.
