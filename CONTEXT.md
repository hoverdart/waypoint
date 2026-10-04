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

## 2026-10-03 — Owned AI explanations and useful result feedback

- AI explanations require an owned completed question attempt, blocking unseen/draft question access through arbitrary IDs. Foreign options are rejected; input text is bounded. MCQ explanation context now contains the full answer text rather than only its letter.
- Completed results return option text and FRQ rubric criteria; unfinished results return 409. Frontend displays the student's answer, full correct answer/model response, rubric criteria, and an explicit keyword-scoring limitation. Similar-question launch errors are recoverable.
- Verification: 191 backend tests, 66 frontend tests, ESLint, TypeScript, production build, and 7 real Clerk/PostgreSQL browser tests pass. Browser checks cover result feedback and a 390px signed-in dashboard with no horizontal overflow.
- Next settings work confirmed from source: settings currently redirects course/time changes to onboarding; onboarding accepts unbounded mode/time/score inputs and cannot remove courses. Implement validated course preferences in-place while preserving history.

- Mobile visual QA caught fixed navigation inside a backdrop-filter ancestor, positioning it across the header. Moved it outside HeaderShell; the browser test verifies its bottom-of-viewport bounds. Result feedback now uses only the selected option's or general explanation's misconception, never another option's tag.

## 2026-10-03 — Editable course preferences

- Settings now edits course enrollment, target score, exam date, and daily study minutes directly. Saves have pending, success, and retry states. Removing a course deactivates its enrollment without deleting attempts, mastery, or plans; restoring it reuses the same enrollment ID. New plans use the saved study time; today's time can still be adjusted on the plan page.
- Added private GET/PATCH /users/me/subjects and a shared locked enrollment service used by onboarding. Validation bounds score (1–5), daily minutes (5–180), course count, unique course IDs, and active-catalog membership. Mode accepts only professional/gamified, and profile display names are bounded.
- Today's plan and dashboard exclude deactivated enrollments while retaining their saved plans. ModeToggle restores its previous state on failed saves. Course catalog directs students to Settings.
- Verification: 199 backend tests and 69 frontend tests pass, with ESLint/TypeScript passing. Seven real-auth browser tests pass, including preference persistence, removal, history access, and restoration; final production build, Settings screenshot review, and link assertions also pass. Internal fallback email identifiers are hidden from the account section.

- Final account-menu audit remains: screenshots do not clearly show Clerk UserButton in the header; verify sign-out/account management is visibly accessible and test it before completion.

## 2026-10-03 — Account access, action recovery, and CI audit

- Replaced reliance on the header avatar with a visible Account link on desktop/mobile. Settings exposes Clerk profile/security management and explicit sign-out, with a retry state for failed sign-out. Real browser tests verify the profile modal and protected-route rejection after signing out.
- Plan Start/Skip actions and both dashboard plan cards now catch failures and offer retry feedback. PlanItemCard reuses the existing shared practice-launch hook. 75 frontend tests pass; account browser suite passes all 7 cases.
- CI audit found no runs for this branch because push triggers only covered main/master. Added codex/ap-prep-app to triggers. Playwright uses system Python in CI, preserving local virtualenv usage. Root README testing statements updated to match triggers and avoid stale test counts. Clean dependency installation verification underway before the next push.

- Clean-install audit: original lockfile failed npm ci because emnapi dependency entries were inconsistent. Repaired the lockfile, declared Node 24 (matching CI), and clean-installed successfully. Fresh-install tests/lint/types and all 7 browser tests passed on locked Next 16.2.12.
- Production npm audit then reported known critical Next advisories and transitive issues. Compatible security updates are in progress; shadcn CLI moved to devDependencies. Do not push the dependency milestone until install/build/tests/browser/audit checks are complete.
- Remaining admin audit: question editing deletes/recreates option rows, which can violate historical attempt references; schemas also lack bounded/consistent question validation. Address historical option preservation/versioning and validation before the goal is complete.

- Dependency remediation: regenerated the lockfile with current npm after an npm 11.6 optional-dependency inconsistency, then verified standard npm ci under Node 24. Raised Next.js minimum to ^16.3.8, aligned eslint-config-next, and refreshed compatible dependencies. Production npm audit reports 0 vulnerabilities. Added a CI production-audit gate. Current clean-install unit tests: 75 pass; lint and TypeScript pass after moving practice timer initialization into an effect. Matching Playwright Chromium v1243 installed; all 7 final browser tests and production build pass on Next 16.3.8.

## 2026-10-03 — Immutable question revisions and backend dependency security

- Question edits now create a new draft revision and archive the prior question. Prior prompts, options, explanations, attempts, and in-flight sessions stay unchanged. Archived versions cannot be edited or approved again, and reseeding respects their inactive state. Admin editor navigates to the new revision, edits option text/answer keys consistently, and handles errors.
- Validated question scope, type, difficulty, answer-key/option consistency, unique labels, explanation references, and bounded FRQ criteria. Approval requires explanation coverage. Admin pagination is bounded.
- Tests: 206 backend tests and 78 frontend tests pass, including completed/in-flight session preservation, invalid-edit atomicity, archived reseeding, and editor failure recovery. ESLint and TypeScript pass.
- CI run 37160361778 passed frontend checks/build but failed backend tests because an unconstrained newer SQLModel release changed datetime handling. Pinned SQLModel 0.0.39 to match the existing schema rather than silently changing storage semantics.
- Backend dependency audit found cryptography 48.0.1 advisories constrained by Clerk SDK 6. Upgraded Clerk backend SDK to 7 and cryptography to >=50,<51. Added a backend audit gate to CI. Final backend dependency audit reports no known vulnerabilities; all 7 real Clerk/PostgreSQL browser tests and production frontend build pass with Clerk backend SDK 7.

## 2026-10-03 — Completion audit

- Recorded requirement-by-requirement evidence and verification boundaries in docs/DELIVERY.md. Confirmed 279 questions (250 MCQ, 29 FRQ), 264 topics, 43 units across six subjects.
- CI run 37160971101 is successful: backend tests/audit, frontend checks/audit, and production build pass. CI browser job skips without repository Clerk secrets; real local Clerk/PostgreSQL browser verification covers the same flows.
- Final audit fixes: invalid/unavailable analytics course parameters fall back to an enrolled course; empty-state directions point to Settings. Added security headers following OWASP HTTP Headers guidance (https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html). Extended browser checks to gamified mode and 390px analytics. All 7 browser tests and production build pass.
- Scheduler secret comparison uses compare_digest. Its 4 integration tests pass. Docker Compose validates Postgres binding to 127.0.0.1; local setup no longer creates a superuser role. Production docs specify ENVIRONMENT=production and HTTPS. 78 frontend tests and ESLint pass.
- Final application commit 06974c4 is pushed. CI run 37161349117 succeeded for that exact commit: backend and frontend checks, dependency audits, and production build passed. Local real-auth browser suite passed all 7 tests; CI browser execution remains skipped without repository Clerk test secrets. Delivery is complete; no requested deployment is outstanding.

## 2026-10-03 — Comprehensive AP expansion authorized

- User clarified that delivery must cover all AP subjects with substantial question diversity and exam-aligned features, proceeding from most-taken to least-taken. The earlier six-course delivery is a functional foundation, not completion of this expanded content requirement.
- Working across frontend/backend on the existing unified branch; public push authorization persists. User's AGENTS.md edit remains excluded.
- Official 2025 exam participation is the latest subject-volume report found on College Board's data page. Ranking recorded in backend/scripts/seed_data/rollout.py, covering 40 reported subjects plus three current catalog courses without 2025 counts. Those three remain unranked and require launch/syllabus verification before activation. Source: https://apcentral.collegeboard.org/media/pdf/program-summary-report-2025.pdf.
- First course is English Language (616,294 exams), then U.S. History, English Literature, World History, U.S. Government. Exam participation is a proxy for course popularity, not enrollment.
- Completion gates per course: current official framework/format provenance; all tested skills mapped; substantive independent stimuli and multiple questions at varied difficulty; detailed distractor explanations; all applicable response formats and rubrics; representative timed practice; content coverage audits; real seed/API/UI verification. Portfolio and performance-task courses require their own workflows rather than artificial multiple-choice exams.
- English Language research confirms 45 MCQs (reading and revision) in 60 minutes and three essays (synthesis, rhetorical analysis, argument) in 135 minutes. Official framework spirals eight skill categories across nine units. Existing keyword FRQ scoring is insufficient for essay evaluation; introduce rubric self-review with explicit provenance and exclude ungraded work from mastery calculations.

### Expansion milestone 1 — Rubric review and first English Language form

- Added owned, post-submission rubric self-review with strict row score validation, session locking, persistent edits, and failure recovery. Public results return null accuracy/score for self-reviewed essays; internal placeholder attempts do not feed mastery. Self-review neither awards accuracy XP nor changes auto-scored results. Mixed sessions calculate accuracy using scored questions only. History/results clearly separate rubric responses.
- Rubric definitions support level descriptions and admin validation. Existing keyword rubrics remain supported for the original bank; they will be reviewed course by course. No schema migration is required; reviews persist in existing session metadata.
- Added a nine-unit English Language progression mapped to 22 current framework skills. Unit weights are zero because official weighting is by skill category, not unit; do not invent unit percentages. First original form contains five independent passages with 24 reading / 21 writing MCQs, three difficulty levels, and per-option rationales. It remains outside the live seed registry until the course depth/essay/exam workflow is ready.
- Added `python -m scripts.content_audit`, reporting all 43 catalog courses with actual coverage gaps, independent stimuli, format counts, and question/difficulty depth per topic. This is a structural audit, not an educational certification.
- Sources: current course/exam pages and fall-2024 CED at https://apcentral.collegeboard.org/courses/ap-english-language-and-composition and /exam. Original practice scenarios and data are explicitly fictional, not attributed to real studies or writers.
- First essay form added: one synthesis task with six fictional sources including a numerical table and concept diagram, one rhetorical analysis, and one argument task. Each has a substantial illustrative model and a 1/4/1 rubric with level descriptions. The candidate bank now has 45 MCQ + 3 essays; this is not the course's target depth.
- Verification before milestone push: production build and TypeScript pass, 82 frontend tests and ESLint pass, all 7 real Clerk/PostgreSQL browser tests pass. Backend passed 224 tests before the final essay seed regression; final count recorded below after that check.
- Final milestone verification: 226 backend tests pass, including candidate seeding/reseeding and all three essay types through submission and persistent self-review. The 82 frontend tests, lint, production build, and 7 existing real-auth browser tests passed. Broader all-course goal remains active; see docs/AP_EXPANSION.md for explicit depth targets and next steps.

### Expansion milestone 2 — Second independent English Language MCQ form

- Added 45 original passage-based questions: curator essay, fictional historical letter, citizen-science reflection, cooking-instruction revision, and research-reporting revision. Both forms have 24 reading and 21 writing questions. Candidate total: 90 MCQ + 3 essays, ten independent MCQ stimuli.
- Added checks for independent stimulus IDs, unique prompts, contextual passage lengths, per-choice explanations, admin-compatible question structures, and exact curriculum mapping. Candidate seed/reseed regression now verifies 93 persistent question IDs without option replacement.
- Verification: all 227 backend tests pass. No frontend/runtime contract change in this milestone. Previous milestone e819332 passed CI run 37162904548, including backend/frontend checks and audits; local real-auth browser checks passed all 7 cases.
- Remaining English Language work: additional forms and essay diversity to reach depth targets, per-topic difficulty coverage, section-aware timed mock exams, and real browser verification of the new course and rubric review. All other ranked courses remain pending comprehensive expansion.

### Expansion milestone 3 — Essay diversity and weighting-aware readiness

- Added a second three-essay set (phone-policy synthesis with six sources and a visual poster, measurement/fairness rhetorical analysis, traditions argument). Candidate bank: 90 MCQ + 6 essays. All model approaches are illustrative, not sole acceptable answers; hypothetical examples are labeled.
- Audited each 45-question form against official skill-category percentages as well as the reading/writing split. Rewrote targeted items for the appropriate rhetorical purpose/audience or reasoning skill; both forms now pass every category range. Added a regression gate so later form edits cannot silently lose alignment. Difficulty labels remain author estimates, not empirically calibrated exam difficulty.
- Added safe scoring-method metadata before submission, accurate self-review instructions in the practice UI, and accessible essay entry with word/character counts and the API's 20,000-character bound.
- Course integration audit found that zero official unit weights previously flattened subject mastery and planner priorities to zero. Added an explicit equal-unit fallback when all unit weights are unknown, retaining weakness-based ranking without falsely reporting high AP frequency. This is a WayPoint estimation fallback, not official English Language unit weighting.
- Excluded rubric-self-review essays from automatically scored diagnostics. Regression exercises a 60-question candidate diagnostic and verifies positive subject mastery; no essay can generate a false automatic failure in that selection.
- Verification: 233 backend tests, 85 frontend tests, ESLint, TypeScript/production build pass. Previous content milestone 0322723 passed CI run 37163201909. Existing seven real-auth browser tests passed at milestone 1; new-course browser verification remains pending activation.
- Next: Forms C/D and remaining essay sets; run coverage audit to close all 49 unit/skill topic depth/difficulty gaps; implement section-aware timed mocks and test the student flow before enabling English Language. Continue U.S. History second, then the remaining participation-ranked courses. Expanded goal remains active and incomplete.

### Expansion milestone 4 — Section-aware timed exam workflow

- Previous goal turn classified as progress: three pushed expansion commits and tested content/runtime improvements. Current authoritative state remains English Language candidate with 90 MCQ and six essays; other courses await their ranked expansion.
- Added exam blueprints for Forms A/B, resolving exact original item keys and preserving passage order. Incomplete, duplicate, inactive, or wrong-type item sets fail closed rather than silently shortening a mock. English Language uses 45 MCQ / 60 minutes and three essays / 135 minutes including reading time; standard, 1.5x, and 2x practice allowances are fixed at start. Untimed inter-section breaks are explicitly labeled practice behavior.
- Added owned exam APIs and locked section transitions. Server deadlines reject late drafts; revision checks reject stale overwrites; future/closed questions cannot be accessed through the exam reader or generic practice-session reader. Generic draft/submit cannot bypass section locks. Scoring and XP occur only once when the last section closes, using saved answers and blanks for unanswered items. Essays remain self-reviewed, not automatic failures.
- Frontend reuses existing MCQ/FRQ forms and results. Added course launch cards, an exam route, countdown, question navigation, autosave with in-flight edit preservation, explicit section-close confirmation, retry/reload states, and correct history resume links. Unknown unit weights no longer display as 0% exam weighting.
- Full test run exposed a pre-existing host-local vs UTC streak boundary failure after UTC midnight. Completion times use UTC; default streak day now also uses UTC. Added a regression with different host/UTC dates rather than weakening the test. User-local streak preferences are not yet implemented.
- New real-auth browser flow will exercise candidate content using an explicit disposable-database seed script; this does not activate the unfinished course in production.
- Verification completed: 244 backend tests, 95 frontend tests, lint and production build pass. Seven existing browser cases passed; the new real Clerk/PostgreSQL exam case passed after fixing mobile overflow and completed-exam results routing. It verifies MCQ persistence/resume, section locks, an untimed break, mobile essay entry, essay persistence, completion, and rubric-review persistence. Inspected the mobile essay screenshot.
- PostgreSQL connections now explicitly use UTC to prevent aware timestamp writes being cast into a host-local naive date; streak grouping normalizes aware values. Regression covers a differing host day and database reload. Historical timestamps written under a non-UTC database setting are not retroactively reinterpreted.
- Files affected: backend exam router/schemas/services, shared practice guards/history, UTC database/streak handling and regression tests; frontend exam components/route/API, course launch/history integration and browser/component tests. No migration required. English Language remains 90 MCQ + six essays; Forms C/D, further essays and coverage closure remain next, followed by U.S. History. Overall expansion remains incomplete.

### Expansion milestone 5 — Third independent English Language MCQ form

- Previous turn classified as progress: pushed `9f93c35`, whose CI run 37164447524 subsequently passed. Current work remains within backend content/tests and root documentation; no frontend behavior changes.
- Added 45 original questions across five new passages: an observatory opening address, a reflective marsh essay, a fictional nineteenth-century reading-room petition, a tool-lending proposal, and a neighborhood heat-mapping draft. Each item has four answer-specific rationales and curriculum mapping. Scenarios and observations are expressly fictional; no official exam questions or published passages were copied.
- Form C has 24 reading and 21 writing questions and satisfies the published skill-category ranges. It is included in the candidate bank but not the timed exam catalog until its three essays exist. Candidate total: 135 MCQ + six essays, 15 independent MCQ stimuli, nine units and 49 unit/skill topics.
- Coverage audit: no completely uncovered topics; 19 topics still below three questions and ten without difficulty variety. This is structural progress, not a claim of calibrated difficulty, educator review, or comprehensive completion. Next: Form C essays, Form D, remaining essay diversity and coverage gaps, then U.S. History in participation order.
- Verification: all 245 backend tests pass, including item/stimulus independence, admin-compatible content, category weights, improved coverage, and idempotent seeding of 141 questions. No frontend changes required new browser checks in this content milestone.

### Expansion milestone 6 — Third complete English Language exam

- Previous turn classified as progress: pushed `9672be4`; CI run 37164801462 passed. Added the Form C essay set and registered its complete timed rehearsal using the existing exam workflow. Changes are confined to backend content, blueprint, tests, and documentation.
- New synthesis task examines a public photograph archive with six fictional sources, a request/use data table, and a website mockup; rhetorical analysis examines the original observatory address; argument examines deliberately becoming a beginner. Each includes a substantial illustrative model and the existing six-point self-review rubric. No automatic essay grade or official AP prediction is implied.
- Candidate total is now 135 MCQ and nine essays (three of each type), with three complete independent timed forms. The course remains outside production enrollment until remaining depth targets are met. Next: Form D, nine additional essays, and remaining unit/skill depth and difficulty gaps, then U.S. History.
- Verification: 247 backend tests pass, including Form C item isolation, 45/3 section resolution, complete submission, self-review scoring separation, rubric validation, model depth, and idempotent seeding of 144 questions. Existing frontend exam components require no change.

### Expansion milestone 7 — Fourth English Language reading section

- Previous goal turn classified as progress: `85e80b9` was pushed and CI run 37164949542 passed. Added 24 original reading questions across three new texts: theater memoir, intergenerational seed-saving reflection, and civic testimony about a closed footbridge. Each uses its own passage and individual answer rationales; all settings and events are fictional.
- Targeted thin claim/evidence, thesis, syntax, and diction coverage. Current candidate: 159 MCQs, nine essays, 18 independent MCQ stimuli. Topics below three questions decreased from 18 to 11; topics without difficulty variety decreased from ten to eight. Author-assigned difficulty is not empirically calibrated.
- Form D remains outside the timed catalog until its 21 writing questions and three essays are complete. Existing three forms remain available only in candidate/test seeding. Production course activation and all-subject completion remain pending.
- Verification: 248 backend tests pass, including independent stimuli, valid curriculum mapping, rationales, category distribution for the reading section, improved coverage, and idempotent seeding of 168 questions. Changes are confined to backend content/tests and documentation. Next: Form D writing to close composition gaps, then essay depth and English Language activation checks before U.S. History.
