# Implementation Context

## Current scope

- Full AP exam preparation app, using the existing Next.js/TypeScript/Clerk frontend and FastAPI/SQLModel/Postgres backend.
- All frontend and backend changes share `codex/ap-prep-app`, as requested. Preserve existing user edits to AGENTS.md and this document.
- Implementation sequence: verify baseline; secure practice/diagnostic submissions; complete course browsing and self-directed practice; expand and validate curriculum content; refine the visual system; verify complete flows.

## Change log

- 2026-08-02: Added this context document and repository guidance requiring it to be kept current during implementation.

## Verification

- 2026-10-03: Existing frontend baseline passes: 46 tests across 13 files.
- Backend baseline cannot connect to local Postgres. Preparing an isolated temporary Postgres instance to run real database tests.
- Audit found practice submission lacks replay, question membership, and daily-plan ownership validation. These are the first security fixes.

## Completed in this implementation

- Backend: shared locked submission validation prevents repeated XP/mastery awards, duplicate/missing/foreign questions, and mismatched answer options. Diagnostic submission now checks session ownership. Practice completion verifies daily-plan ownership and matching topic before any writes. Bounded practice/answer request schemas reject invalid counts and oversized responses.
- Verification: 148 backend tests pass against isolated PostgreSQL 18 at localhost:55432, database waypoint_test. Sandbox requires elevated execution for local database connections. Added 11 security regression cases; updated one diagnostic fixture to persist its selected question IDs as real sessions do.
- Frontend: course detail route `/subjects/[id]`, searchable expandable units/topics, selectable MCQ/FRQ session size, topic/unit/course practice launch, recoverable launch errors, course links, and diagnostic error notifications. Added four course component tests; verification in progress.
- Remaining: content breadth/curriculum audit, visual redesign, mobile navigation, practice persistence/history/review, deployment configuration and full browser verification. No deployment or push performed.

## Latest progress / continuation notes

- Frontend course UI: 50 tests and TypeScript passed after course additions. Mobile navigation and initial editorial redesign subsequently pass 52 tests, TypeScript, and ESLint. A new hero test and revised browser expectations were added after that run and still need verification.
- Visual changes: warm paper/forest palette, tighter surfaces, serif landing headline with an explicitly illustrative daily study note, simpler sticky header, mobile bottom navigation, and skip-to-content link. Existing landing sections still need visual review/refinement. Browser visual QA and production build pending.
- Content audit: 176 questions across six subjects; 89 existing topics lack questions (Calculus 18, Biology 13, Psychology 22, US History 10, Chemistry 11, CSA 15). No content expansion yet.
- Official current curriculum checked 2026-10-03: https://apcentral.collegeboard.org/courses/ap-computer-science-a lists four units: Using Objects and Methods (15–25%), Selection and Iteration (25–35%), Class Creation (10–18%), Data Collections (30–40%). Existing seed still uses ten legacy units.
- https://apcentral.collegeboard.org/courses/ap-psychology lists five units: Biological Bases of Behavior, Cognition, Development and Learning, Social Psychology and Personality, Mental and Physical Health (each 15–25%). Existing seed still uses nine legacy units. Correct structures and mappings while preserving existing database attempts/mastery when reseeding; do not silently delete user data.
- Temporary Postgres initialized at /tmp/waypoint-postgres, listening on 127.0.0.1:55432. Tests: TEST_DATABASE_URL=postgresql+psycopg://waypoint@127.0.0.1:55432/waypoint_test .venv/bin/python -m pytest (backend working directory, elevated network permission). All 148 backend tests pass.
- Further security audit needed: authentication authorized parties, AI question-answer access, admin validation, empty sessions and filter consistency, production headers. Practice currently has no answer draft persistence or back navigation and no submission error handling; improve these with tests. Course launches now handle errors, including empty sessions.

## 2026-10-03 — Saved practice milestone

- Added private paginated practice history (`GET /practice`) and locked draft saves (`PATCH /practice/{id}/draft`). Drafts preserve selected answers, free responses, time spent, current question, and a validated daily-plan association without awarding XP or changing mastery. Completed sessions reject late draft writes.
- Frontend now resumes server-saved answers, saves on Next/Back and Save & exit, preserves answers on network failure, and supports submission retry. `/practice` provides resume/review links and older-session pagination. Added a Practice navigation destination.
- Added tests for draft persistence, cross-user isolation, invalid drafts, completed-session protection, pagination, frontend save/back/resume/retry flows, and history links.
- Verification: backend 153 tests pass; frontend 59 tests pass; TypeScript and ESLint pass. Production build in progress with elevated permissions because Turbopack worker port binding is denied inside the sandbox.
- Replaced network-fetched display/body fonts with system typography so builds do not depend on Google Fonts. Set the Turbopack root explicitly to frontend/.
- User authorized periodic commits and pushes to the existing unified branch. User's pre-existing AGENTS.md edit is not included in app commits.
- Known remaining work still includes the curriculum/content expansion, additional security audit and runtime/browser verification described above. Saved drafts require Next/Back or Save & exit; unsaved edits to the current question are not yet autosaved.
- Production Next.js build now passes, including all 16 application routes and proxy. No external font download is required. Backend milestone committed as 683b420; frontend milestone follows on the same branch.

## 2026-10-03 — First content expansion and push status

- Added 18 original offline-authored Calculus AB MCQs with worked explanations across the 18 previously uncovered topics. The course now has 50 questions and practice coverage for all 45 current seeded topics. New content correctly uses source=generated rather than claiming human authorship.
- Added full-bank structural validation (curriculum mapping, answer keys, option uniqueness, explanations, FRQ rubrics) and an idempotent expanded-seed test preserving question and option IDs. All 156 backend tests pass.
- Local commits: 683b420 (backend), b280557 (frontend). A push to origin was rejected twice by automatic approval review: the destination is the public https://github.com/hoverdart/waypoint repository, and the reviewer requires explicit authorization for exposing code at that destination. Authenticated GitHub user is Abdullah-Waris and has WRITE permission. An asynchronous destination-specific approval question is pending; do not retry until answered.
- Production frontend started locally on 127.0.0.1:3000 for visual QA. Playwright Chromium was absent; installing into /tmp/waypoint-playwright. Font-independent build, TypeScript, ESLint, and 59 frontend tests pass.

## 2026-10-03 — Remote and visual verification

- User explicitly approved publishing to the public https://github.com/hoverdart/waypoint repository. Authorization persists: no further destination confirmation is needed. Successfully pushed commits 683b420, b280557, and f2cc322 to origin/codex/ap-prep-app and verified remote head f2cc322.
- Browser checks revealed port 3000 also served another app, and IPv4-only preview caused Next.js localhost proxy failures. Use default binding on isolated http://localhost:3108 for this app. Production preview handle 36446; Chromium installed at /tmp/waypoint-playwright.
- Replaced oversized pinned landing sections and scroll-hidden content with compact static editorial sections and six linked course cards. Desktop (1440px) and mobile (390px) screenshots inspected: no horizontal overflow (document width 390), desktop total height 2852px, mobile 4683px. Landing responds HTTP 200 and has title WayPoint. Screenshots at /tmp/waypoint-landing-desktop.png and /tmp/waypoint-landing-mobile.png.
- Latest frontend checks: 60 tests, TypeScript, ESLint, and production build pass for the landing refinement. Browser auth check redirects to Clerk-hosted /sign-in because local .env omits redirect paths. Added explicit /login and /signup to ClerkProvider and middleware; rebuild/browser recheck pending for that final adjustment.
- Explicit local auth-route adjustment verified: production build succeeds; 60 frontend tests and ESLint pass; Chromium assertions confirm /dashboard redirects to localhost:3108/login, the actual Clerk login form renders, and all six landing course headings are visible. Current production preview handle 59956.

## 2026-10-03 — Biology, Chemistry, and U.S. History coverage

- Added 34 original offline-authored explained MCQs (Biology 13, Chemistry 11, U.S. History 10), covering every formerly empty topic in those seeded courses. Counts: Calculus 50, Biology 44, Chemistry 39, U.S. History 37, Psychology 30, CSA 28; total 228.
- Extracted the shared question-record builder used by the new question banks. All generated additions retain source=generated and contain deterministic answer explanations; no runtime question generation.
- Added coverage assertions and all-six-subject idempotent database seed/reseed verification preserving question and option IDs. All 160 backend tests pass against PostgreSQL.
- Next functional issue found: daily-plan regeneration control is a disabled placeholder, repeated generation duplicates today's plans, and planner candidates may lack approved questions. Address these together with bounded budget input, stable existing completed work, and regression tests.

## 2026-10-03 — Functional daily time budgets

- Replaced the disabled time-budget placeholder with a per-course 5/10/20/30/45/60-minute control, pending state, successful-update message, and recoverable failure state.
- Planner now serializes generation per student and reuses an existing course/day plan, preventing duplicate plans from repeated clicks. Explicit time changes preserve completed work and all item IDs, marking unselected pending items skipped so already-started sessions remain valid. Completed and skipped topics stay out of the regenerated work for that day.
- Candidates require approved active questions. FRQ-only topics receive FRQ tasks; short budgets can select a smaller MCQ review instead of yielding an empty plan. Plan status updates after item changes and practice completion. Response includes course ID even for an empty plan; time and status inputs are bounded.
- Verification: 165 backend tests, 62 frontend tests, and TypeScript pass. An ESLint unescaped-apostrophe error was corrected; lint rerun and production build pending. User's existing AGENTS.md change remains untouched.
- Daily-budget milestone final checks: ESLint and production build pass. Content expansion c89e65c was pushed successfully. Daily budget changes are ready to commit and push on the same branch.

## 2026-10-03 — Current Psychology and CSA curricula

- Reorganized Psychology into five current units and CSA into four, following College Board course pages and course-at-a-glance PDFs: https://apcentral.collegeboard.org/courses/ap-psychology and https://apcentral.collegeboard.org/courses/ap-computer-science-a. Topic labels are WayPoint study subdivisions.
- Added 54 explained original MCQs. Active bank: 279 questions across six subjects and 264 study topics, with at least one question per topic. Psychology has 59 questions; CSA has 50. Generated content is labeled accordingly and still benefits from educator review.
- New migration 20261003_active_curriculum adds Unit.is_active. Apply `alembic upgrade head` before `python -m scripts.seed`. Reseeding reparents recognized legacy topics and preserves their IDs, attempts, session history, and mastery; unused legacy units are archived. New practice, diagnostics, plans, and mastery summaries exclude archived units. Existing sessions remain accessible and submittable.
- Verification: 170 backend tests pass on PostgreSQL (waypoint_test_v2 at localhost:55432). A fresh database passed actual Alembic upgrade/downgrade/upgrade and two seed runs. Migration regression tests cover historical attempt preservation and archived-session completion.
- Daily-budget milestone 5cad0f7 is pushed. Unified branch remains codex/ap-prep-app; public push authorization is explicit and persistent. User's AGENTS.md modification remains excluded.

## 2026-10-03 — Valid study-session creation

- Backend practice creation now checks active course/unit/topic relationships and rejects empty selections before inserting a session. Invalid or archived scopes cannot create unusable history entries.
- Diagnostics retain weighted unit allocation and preferred difficulty, then fill sparse quotas from remaining approved questions without duplicates. Zero-weight curricula use available questions; empty curricula return a useful error.
- Added 10 regression cases for empty selections, invalid scopes, sparse unit/difficulty fallback, and zero weights. Full backend suite: 180 passing tests.
- Curriculum milestone 6ec1f42 is pushed. Next verification work: real Clerk authenticated browser flow using isolated ports and a seeded local database.

## 2026-10-03 — Real authenticated browser verification and concurrency fix

- Playwright now starts dedicated frontend/backend ports 3109/8109 (overridable), loads local credentials without printing values, sets the matching API URL/CORS origin, and refuses accidental reuse of unrelated servers. Expanded golden path covers real Clerk onboarding, a 20-question diagnostic, course practice, Save & exit/reload recovery, results, and daily-plan task completion. It asserts no server-error responses.
- The first browser run exposed simultaneous AI allowance creation failures from result cards. Serialized allowance creation and cap-check/increment by locking the user row until commit. A real six-connection concurrency test verifies exactly one allowance row and no cap overrun.
- Clerk now verifies authorized token origins against CORS_ALLOWED_ORIGINS, rejects malformed identities, and does not expose SDK exception details. Guidance checked: https://clerk.com/articles/how-to-add-authentication-to-a-python-backend. Configure exact frontend origins in every environment.
- Verification: 186 backend tests, 62 frontend tests, production build, and all 7 Playwright tests pass with real Clerk and PostgreSQL. Temporary Clerk users are removed by test teardown; their study records live only in the disposable database waypoint_migration_test. Final ESLint and TypeScript rechecks also pass.
- Added frontend verification instructions and updated backend content/auth setup documentation. Remaining work includes richer result feedback, remaining action error states/settings, AI question-access validation, signed-in mobile QA, and final production readiness audit.
