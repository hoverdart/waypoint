# Implementation Context

## Current scope

- Frontend only. Backend persistence and mastery initialization are owned by a separate developer on another branch.

## Change log

- 2026-08-02: Added this context document and repository guidance requiring it to be kept current during implementation.
- 2026-08-03: Rebuilt the student onboarding UI as profile, AP-goals, diagnostic-coming-soon, and feature-tour/mode stages. Added animated login entry and sign-in completion handoff, profile settings, dashboard grade context, and frontend guards for incomplete onboarding.
- 2026-08-03: Added the frontend API contract in `frontend/lib/api/onboarding.ts`: `GET/PATCH /onboarding` state/draft handling and `POST /onboarding/complete`. The backend branch must add `grade_level`, onboarding/diagnostic status, and idempotent neutral mastery initialization for skipped diagnostics before these network calls can function end-to-end.

## Verification

- `npx tsc --noEmit`, `npm run lint`, and `npm test` passed in `frontend/` (54 tests).
- `npm run build` reached compilation but could not complete because the sandbox cannot fetch the existing Google-hosted Geist, Geist Mono, and Plus Jakarta Sans fonts. This is an environment network limitation, not a code diagnostic.
