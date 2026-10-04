# AP prep application delivery audit

Verified on 2026-10-03. Frontend and backend share `codex/ap-prep-app`.

## Requested outcome and evidence

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Complete frontend using the existing stack | Next.js App Router, TypeScript, Tailwind, shadcn, Clerk; editorial cream/forest styling, serif landing typography, responsive course pages, professional and gamified views | Production build, 78 component tests, desktop/mobile screenshot review, real Chromium flows |
| Functional backend | FastAPI, SQLModel, PostgreSQL; migrations, authenticated APIs, deterministic mastery/planner/scoring, weekly coach job | 206 PostgreSQL-backed tests; CI on Python 3.12/Postgres 16; actual Alembic upgrade/rollback/re-upgrade and repeat seed |
| AP subjects and questions | Seven available courses, 52 units, 360 study topics, 775 original questions; English Language has the expanded 198-question bank while six foundation courses await depth review | Whole-bank answer-key/mapping/coverage assertions and idempotent database seeding tests |
| Student study workflow | Authentication, onboarding, diagnostics, course/topic practice, answer saving/resume, results, daily plans, analytics, course preferences, XP/streaks/badges | Real Clerk browser test covers onboarding through results, saved-answer recovery, plan completion, preferences, analytics, mode switching, mobile navigation, account management and sign-out |
| Security | Clerk verification with exact origin allowlist; per-user ownership; bounded input; replay protection and locked submission/cap operations; admin allowlist; immutable question revisions; protected scheduler; safe production errors; security response headers | Ownership/replay/concurrency/admin tests; API input tests; real sign-out protection; frontend and backend dependency audits report no known production vulnerabilities |
| Preserve history while maintaining content | Curriculum migrations reparent recognized topics without removing attempts; question edits archive old versions; removing enrollment retains study data | Curriculum migration, admin revision, enrollment, draft, and history regression tests |
| Unified branch and organized pushes | Both app areas committed together on one branch; `CONTEXT.md` updated at milestones | Git history and origin tracking; user's unrelated `AGENTS.md` edit excluded |
| Reviewable setup and handoff | README, development/test guides, env examples, Dockerfiles/Compose, migration and seed commands, scheduler instructions | Clean Node 24 `npm ci`; Compose config validates local-only database binding; local production build and real DB/browser checks |

## Content inventory

| Course | Units | Topics | MCQ | FRQ |
| --- | ---: | ---: | ---: | ---: |
| Calculus AB | 8 | 45 | 45 | 5 |
| Biology | 8 | 42 | 39 | 5 |
| Psychology | 5 | 56 | 54 | 5 |
| U.S. History | 9 | 37 | 32 | 5 |
| Chemistry | 9 | 36 | 34 | 5 |
| Computer Science A | 4 | 48 | 46 | 4 |

Psychology and CSA use the current five- and four-unit organizations checked against
College Board course pages. Topic labels are WayPoint study subdivisions. Every seeded
topic has practice content; this is an original bank, not a collection of official exams.

## Verification boundaries

- FRQ scores use the disclosed rubric keyword heuristic. The results show the student's
  response, model response, and criteria for self-review; they do not claim official AP grading.
- Questions are original generated practice content. Automated structural checks do not
  substitute for an educator's editorial review, and the bank can continue to expand.
- Drafts save on Next/Back or Save & exit, as stated in the practice UI.
- AI explanations are optional and capped. Core practice and checked-in explanations work
  without an Anthropic key. Provider behavior is tested with a fake provider; no paid
  Anthropic calls were required for verification.
- Deployment was not requested or performed. Configure production Clerk/database/API
  origins and HTTPS using the setup guides. Docker Compose configuration was validated;
  the tested runtime used local processes rather than a container deployment.
- GitHub browser tests require repository Clerk test secrets. They are currently skipped
  in CI; the same browser suite passed locally against real Clerk and PostgreSQL.
- Final application commit `06974c4` passed backend tests, dependency audits, frontend
  checks, and production build in [CI run 37161349117](https://github.com/hoverdart/waypoint/actions/runs/37161349117).

## Expanded scope after this delivery

The user subsequently requested comprehensive coverage of every AP course in
participation order. That work is **in progress**, not completed by this six-course
foundation audit. See [AP_EXPANSION.md](AP_EXPANSION.md) and the latest CONTEXT.md entries.
