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
