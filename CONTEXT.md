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

### Expansion milestone 8 — Official released-exam resources

- User requested scraping old AP tests for additional questions. The previous response only explained the copyright constraint and was not implementation progress; this turn revalidated the available official sources and added an actionable course resource feature.
- Added a backend catalog of verified College Board archive links for all six live courses plus English Language. English Language also includes direct 2025 Set 1/2 question PDFs paired with their scoring guides. URLs were discovered and checked through the official past-exam index and course archives on 2026-10-04. No exam text, third-party excerpts, PDFs, or secure AP Classroom content are copied into the repository or question bank.
- Course-detail API now supplies released-exam resources. The course page shows accessible external links, labels PDFs, explains that older formats may differ, and states that external work is not saved or scored by WayPoint. URLs are editorially controlled; no user-supplied URL fetching or runtime scraper is introduced.
- Sources: https://apcentral.collegeboard.org/courses/past-exam-questions and https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam/past-exam-questions. The latter currently exposes both 2025 sets and scoring guides; the archive handles availability changes for other years.
- Affected areas: backend catalog/schema/course API/tests; frontend course page/resource component/types/tests. Read installed Next dynamic-route documentation before editing the course page. Original question-bank expansion remains active: Form D writing and essays are next, followed by remaining English Language depth and U.S. History.
- Verification: 250 backend tests and 97 frontend tests pass. Production build/TypeScript and lint pass. Concurrent npm wrapper invocations initially produced a missing temporary Node executable and a terminated lint process; rerunning those checks sequentially passed. Tests cover official-host URL restrictions, paired question/scoring links in course responses, unknown-course behavior, external-link accessibility, empty catalogs, and honest tracking limitations.

### Expansion milestone 9 — Four complete English Language MCQ forms

- Previous goal turn classified as progress: pushed released-resource feature `c58f5ec`, verified by successful CI run 37165268249. Resumed original-content expansion with 21 Form D writing questions across music-rehearsal and trail-information drafts. All trial data and settings are fictional.
- Candidate reaches 180 MCQ across 20 independent passage stimuli, plus nine essays. Each of four MCQ forms has 24 reading and 21 writing items and meets the published skill-category proportions. Form D still needs its essay section before timed release.
- Composition coverage gaps are closed structurally: all writing topics have at least three questions. All 49 unit/skill topics have multiple difficulty labels, and only Unit 2 thesis/argument structure remains below three questions. Labels remain author estimates, not empirical calibration or educator certification.
- Verification: all 251 backend tests pass, including category weights for all four forms, independent new stimuli, admin content validation, rationales, coverage depth, and idempotent seeding of 189 questions. Backend content/tests and documentation changed; frontend behavior is unchanged.
- Next: add nine essays to meet the 18-essay target, complete Form D, close the last topic-depth gap, and verify activation before continuing to U.S. History. Overall goal remains active and incomplete.

### Expansion milestone 10 — Four complete English Language exam forms

- Previous turn classified as progress: pushed `6c0b7f0`; CI run 37165602130 passed. Added Form D synthesis on repairability in municipal purchasing (six fictional sources including bid data and a label mockup), rhetorical analysis of the original bridge testimony, and argument on public recognition. Each has a substantial model and six-point self-review rubric.
- Registered Form D in the candidate timed-exam catalog. Parameterized end-to-end backend checks now exercise all four forms: exact form-specific item membership, 45/3 section counts, section transitions, final submission, and automatic/self-review separation.
- Candidate bank: 180 MCQs and 12 essays, four complete timed forms. All 49 unit/skill topics now have at least three questions and multiple author-estimated difficulty levels. The last gap was Unit 2 thesis/argument structure, now supported by the rhetorical analysis of the testimony's qualified central argument. Structural checks do not establish educator review or calibrated difficulty.
- Verification: 255 backend tests pass, including idempotent seeding of 192 questions. Historical Form C coverage comparison now explicitly uses the A/B/C snapshot so later additions cannot invalidate its baseline. No frontend behavior changed.
- Next: six additional diverse essays to reach the 18-essay target, activation verification, and then U.S. History. Overall all-course objective remains active.

### Expansion milestone 11 — English Language essay depth target

- Previous goal turn classified as progress: completed and pushed Form D plus the final topic-depth gap. Added six supplemental essays: synthesis on group-project grading and public-art duration; rhetorical analysis of two new independent passages on printing craft and scientific leadership; arguments about unplanned time and ambitious goals.
- Each synthesis has six fictional sources including a table and visual; all six essays have distinct substantial model responses and the six-point self-review rubric. These are original practice tasks with clearly labeled fictional scenarios, not copied released exams. Sets E/F are supplemental essay practice, not additional complete mock exams.
- Candidate bank now meets the documented structural targets: 180 MCQs, 20 independent MCQ stimuli, 18 essays (six per task type), four complete timed forms, and at least three questions with varied author-estimated difficulty for all 49 unit/skill topics. This does not establish psychometric equivalence or external educator review.
- Verification: 256 backend tests pass, including independent prompts/models/item IDs, source packs, admin-compatible rubrics, complete coverage, and idempotent seeding of 198 questions. Existing API and frontend workflows are unchanged.
- Activation audit located the remaining deployment work: add English Language to the normal seed registry/subject list, update the fixed six-course presentation and seed regressions, distinguish expanded coverage from foundation banks in the audit, and rerun the normal student flow. No production activation is claimed yet. U.S. History remains next in participation order; all-course goal remains incomplete.

### Expansion milestone 12 — English Language enrollment activation

- Previous goal turn classified as progress: supplemental essays completed the planned structural targets. English Language is now registered in the normal seed module and subject catalog, with 198 questions, nine units, 49 topics, and four complete timed forms. Available courses are ordered by the verified participation ranking, and the landing page presents all seven courses in that order.
- Normal seeding now contains 477 questions across seven courses, 52 units, and 313 topics. The other six banks remain foundations requiring comprehensive depth review; only English Language is marked `live_expanded_bank` in the structural audit. This status is not educator certification.
- Retired the English Language candidate-only preview seed and E2E flag. The regular browser suite now exercises its onboarding, course launch, persisted MCQ and essay drafts, history resume, section transitions, results, and saved rubric self-review. Existing ordinary-practice and anonymous-access checks also pass.
- Verification: 256 backend tests, 97 frontend tests, production build/TypeScript, and all eight real Clerk/PostgreSQL browser tests pass. Seed/reseed preserves IDs for all 477 questions. Normal seed was applied to the disposable local verification database only; this is a code/seed activation, not a claim that an external production deployment has run it.
- Files affected: backend seed/catalog/audit and regressions; frontend landing list and its tests; normal exam E2E inclusion; delivery/expansion docs. No database migration is needed. Next course for deep expansion: U.S. History, with current framework verification, source-based MCQs, SAQ/DBQ/LEQ workflows, and representative timed practice. Overall goal remains active.

### Expansion milestone 13 — U.S. History framework audit

- Previous goal turn classified as progress: English Language was registered for normal seeding/enrollment and passed the real browser suite. Began the next ranked course, U.S. History, by inspecting the live nine-period/37-question foundation bank and current official sources.
- Found a material May 2027 exam update: all three SAQs are required and source-based (secondary text, primary text, non-text); LEQ is one broad required prompt instead of the prior choice menu. The official update says content and rubric criteria are unchanged. Timed history implementation must follow this current format, not older released-test selection behavior.
- Corrected Period 2 weighting from 4–6% to the official 6–8%. Added a database regression demonstrating that reseeding repairs existing weights without changing the unit ID. Other eight period ranges match the current course page.
- Added docs/US_HISTORY_EXPANSION.md with verified exam references, explicit 2027 requirements, content targets, historical-source provenance rules, and the pending MCQ/SAQ/DBQ/LEQ work. This is a roadmap, not a claim those features exist. Backend curriculum/test and root documentation are the affected areas; frontend unchanged.
- Next: complete topic mapping and sourced question sets, then current-format free-response workflows. All-course expansion remains active and incomplete.
- Verification: all 257 backend tests pass, including exact nine-period weights and in-place correction through normal reseeding. No frontend changes required browser checks for this milestone.

### Expansion milestone 14 — Period 1 framework coverage and sourced practice

- Previous turn classified as progress: corrected U.S. History weights and verified the changed 2027 exam requirements. This turn expands Period 1 from four coarse topics to all seven framework topic areas, preserving the existing four names and adding stable `ced:1.x` tags.
- Added nine original MCQs across contextualization, cultural encounters before 1607, and causation. Stimuli are explicitly labeled instructional summaries, not fabricated primary-source quotations; prompts include verified Library of Congress/NPS research references. Questions assess evidence limits, purpose/audience, historical context, and interacting causes, with individual answer rationales.
- Current U.S. History bank: 46 questions across 40 topics. The added three topics each have three questions at varied author-estimated difficulty. This does not complete Period 1's total depth or the other eight periods. Total normal seed: 486 questions and 316 topics across seven courses.
- Source framework: https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-at-a-glance.pdf, read alongside the previously verified fall-2026 corrections. Historical references: https://www.loc.gov/exhibits/1492/america.html and https://www.nps.gov/peco/learn/historyculture/spanish-encounters.htm. New names/descriptions are WayPoint paraphrases of topic scope.
- Affected areas: backend curriculum, original content, seed regressions, and documentation. Next: expand the remaining period topic mappings and add authentic primary/non-text stimulus practice, followed by 2027 SAQ/DBQ/LEQ workflows.
- Verification: all 258 backend tests pass, including exact Period 1 framework codes, valid questions/rationales, complete current-topic coverage, and stable topic/question IDs on reseeding. Frontend behavior is unchanged.

### Expansion milestone 15 — Period 2 and verified primary-source practice

- Previous goal turn classified as progress: Period 1 mapping and nine source-based questions were pushed. Expanded Period 2 from four to eight framework areas, retaining existing names/IDs and adding `ced:2.1` through `ced:2.8` tags.
- Added 12 original questions across contextualization, slavery, colonial culture, and comparison. Three use a verified short public-domain excerpt from Virginia's December 1662 law; the rest explicitly identify their stimuli as original instructional summaries. Each prompt includes provenance and each option has its own rationale. The law is analyzed as evidence of institutionalized hereditary slavery, with limits on inferring lived experience from legal prescription alone.
- References checked: Library of Congress religion exhibits (rel01.html and rel02.html) and Encyclopedia Virginia's transcription of the 1662 statute at https://encyclopediavirginia.org/primary-documents/negro-womens-children-to-serve-according-to-the-condition-of-the-mother-1662/. No copyrighted AP exam text was imported.
- U.S. History now contains 58 questions across 44 topics; normal seed totals are 498 questions and 320 topics. Periods 1–2 map their framework topic areas, but their original topics still need more depth and Periods 3–9 remain coarse. Current-format SAQ/DBQ/LEQ workflows are still pending.
- Backend content/curriculum/build helper/tests and docs changed. Next: Period 3 mapping and diverse primary/non-text evidence. Overall goal remains active.
- Verification: all 259 backend tests pass, including all eight Period 2 codes, valid distinct stimulus types, per-option explanations, and stable seed/reseed IDs. Frontend unchanged.

### Expansion milestone 16 — Revolutionary ideals and constitutional evidence

- Previous goal turn classified as progress: Period 2 coverage and verified primary-source questions were pushed. Added eight original Period 3 questions using short public-domain excerpts checked against National Archives transcriptions of the Declaration and Constitution.
- Added two distinct topics, political ideas of the Revolution (CED 3.4) and constitutional structure/federal power (CED 3.9), without renaming or removing legacy topics. Questions distinguish political principles from participation, legal grants from actual exercise, and interpretation from unsupported generalization. All options include explanations.
- U.S. History now has 66 questions across 46 topics; normal seed totals are 506 questions and 322 topics. Period 3 is only partially expanded. Combined legacy topics remain until their existing questions and progress can be safely mapped; this is not complete framework coverage.
- Sources checked: https://www.archives.gov/founding-docs/declaration-transcript and https://www.archives.gov/founding-docs/constitution-transcript. Questions are original, not copied AP items.
- Affected areas: backend question sets, curriculum, regression tests, and docs. Next: remaining Period 3 areas, diverse non-text stimuli, and broader period expansion before the current-format FRQ workflows.
- Verification: all 260 backend tests pass, including source attribution, content validation, topic mapping, and idempotent seeding. Frontend unchanged.

### Expansion milestone 17 — Western territorial incorporation

- Previous goal turn classified as progress: founding-text questions were tested and pushed. Added four original source-based questions on the Northwest Ordinance and a Movement in the Early Republic topic (CED 3.12).
- Verified the short public-domain excerpt against the National Archives transcription at https://www.archives.gov/milestone-documents/northwest-ordinance. Questions cover interpretation, contextualization, argumentation, and corroboration across difficulties 2–4, with individual option explanations. No AP exam questions were copied.
- U.S. History now has 70 questions across 47 topics; total normal seed content is 510 questions across 323 topics. Period 3 and wider course depth remain incomplete; the overall expansion goal remains active.
- Affected areas: backend content/curriculum/tests and delivery documentation. Verification: all 261 backend tests pass, including valid answer keys, provenance, mappings, and idempotent seeding. Frontend unchanged. Next: remaining Period 3 framework areas and varied non-text sources, then later periods and current-format FRQ support.

### Expansion milestone 18 — Confederation finances and ratification

- Previous goal turn classified as progress: western territorial questions were tested and pushed. Added eight original questions and two Period 3 topics (CED 3.7 and 3.8), preserving the combined legacy topic and existing IDs.
- Primary excerpts verified against National Archives transcriptions of the Articles of Confederation and the 1789 resolution proposing amendments. Questions distinguish state revenue collection from federal authority, connect institutional weaknesses to constitutional change, and analyze ratification concerns without treating promised protections as proof of universal enforcement.
- U.S. History now contains 78 questions across 49 topics; normal seed totals are 518 questions across 325 topics. Period 3 still needs missing framework areas and broader evidence formats. Other remaining courses and history FRQ workflows remain outstanding; the overall goal is active.
- Affected areas: backend curriculum/content/tests and documentation. All 262 backend tests pass, including the new provenance, answer-key, topic-code and schema validations plus idempotent reseeding. Changed-file whitespace check passes. Frontend unchanged.
- References: https://www.archives.gov/milestone-documents/articles-of-confederation and https://www.archives.gov/founding-docs/bill-of-rights-transcript. No copyrighted AP questions imported.

### Expansion milestone 19 — Revolutionary ideals and women’s legal status

- Previous goal turn classified as progress: confederation and ratification content was tested and pushed. Added four original source-analysis questions and the Influence of Revolutionary Ideals topic (CED 3.6).
- Verified a short public-domain excerpt of Abigail Adams’s March 31–April 5, 1776 letter against the American Battlefield Trust transcription: https://www.battlefields.org/learn/primary-sources/abigail-adams-john-adams-remember-ladies. The Massachusetts Historical Society endpoint returned 502, so the working transcription is the visible provenance link.
- Questions analyze claims, context, audience, and limits of evidence, distinguishing advocacy from actual changes in legal rights. Each answer option has an explanation. No released AP question text was imported.
- U.S. History now has 82 questions across 50 topics; normal seed totals are 522 questions across 326 topics. Period 3 and all-course expansion remain incomplete. Next: missing Period 3 context, identity, and continuity/change areas, then later periods and varied evidence formats.
- Affected areas: backend content, curriculum, tests, and docs. All 263 backend tests pass; changed-file whitespace checks pass. Frontend unchanged. Overall goal remains active.

### Expansion milestone 20 — National identity and regional loyalties

- Previous goal turn classified as progress: revolutionary ideals content was tested and pushed. Added four original questions and Developing an American Identity (CED 3.11), preserving legacy topics and IDs.
- Verified Washington’s 1796 Farewell Address against the Senate Historical Office transcription at https://www.senate.gov/artandhistory/history/resources/pdf/Washingtons_Farewell_Address.pdf. Prompts identify its modernized spelling/punctuation. Questions cover claims, context, purpose, and counterevidence, without treating a persuasive appeal as proof of universal agreement.
- U.S. History now has 86 questions across 51 topics; normal seed totals are 526 questions across 327 topics. The full course and wider AP expansion remain incomplete. Next: Period 3 contextualization and continuity/change, then full later-period mapping and broader source formats.
- Affected areas: backend curriculum/content/tests and docs. All 264 backend tests pass; changed-file whitespace check passes. Frontend unchanged. No copyrighted AP questions imported; overall goal remains active.

### Expansion milestone 21 — Imperial-crisis context

- Previous goal turn classified as progress: national identity questions were tested and pushed. Added three original contextualization questions and CED 3.1 topic, with an explicitly labeled instructional summary covering imperial rivalry, postwar costs, and later disputes over authority.
- Reference verified: https://history.state.gov/milestones/1750-1775/french-indian-war (retired historical series; used for established historical context). Questions reject reversed chronology and inevitability claims while distinguishing contributing conditions from automatic outcomes.
- U.S. History now contains 89 questions across 52 topics; normal seed totals are 529 questions across 328 topics. Continuity/change and complete Period 3 alignment remain pending, as do later-period expansion and history FRQ workflows. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 265 backend tests pass, including content validation and stable reseeding. Changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions copied.

### Expansion milestone 22 — Uneven revolutionary change

- Previous goal turn classified as progress: imperial-crisis context was tested and pushed. Added four original questions and Continuity and Change in Period 3 (CED 3.13).
- Verified Article I, section 9 against https://www.archives.gov/founding-docs/constitution-transcript. Questions distinguish political independence from the persistence of slavery and distinguish the 1808 end of a constitutional restriction on congressional action from emancipation. Every option includes a rationale.
- U.S. History now has 93 questions across 53 topics; normal seed totals are 533 questions across 329 topics. Period 3 still lacks distinct Revolutionary War coverage and final ordering/mapping of legacy topics. Later periods, diversified non-text evidence, and history FRQ support remain outstanding; overall goal remains active.
- Affected areas: backend curriculum/content/tests and docs. All 266 backend tests pass; changed-file whitespace check passes. Frontend unchanged. No copyrighted AP questions imported.

### Expansion milestone 23 — Revolutionary War and French assistance

- Previous goal turn classified as progress: continuity/change questions were tested and pushed. Added four original questions and a distinct American Revolutionary War topic (CED 3.5).
- Verified historical context against https://history.state.gov/milestones/1776-1783/french-alliance. The stimulus is explicitly an original instructional summary. Questions connect Saratoga, French strategic motives, international assistance, and evidence of naval contributions without presenting the war as exclusively domestic or foreign-led.
- U.S. History now has 97 questions across 54 topics; normal seed totals are 537 questions across 330 topics. Remaining work includes final Period 3 legacy mapping/order, broader wartime perspectives, non-text stimuli, later periods, and history FRQ workflows. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 267 backend tests pass; changed-file whitespace check passes. Frontend unchanged. No copyrighted AP questions imported.

### Expansion milestone 24 — Period 3 curriculum sequence

- Previous goal turn classified as progress: Revolutionary War questions were tested and pushed. Verified Period 3 sequence against https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-at-a-glance.pdf and mapped all 13 framework codes across the existing 15 topics.
- Reordered topics without changing their names or seed identities. Retained the two overlapping foundation topics alongside related expanded topics; the combined Articles/Constitution topic has explicit 3.7–3.9 mappings. Existing questions retain their topic assignments.
- New integration regression simulates stale ordering and missing tags, then verifies reseeding repairs metadata while preserving every topic ID and question-to-topic association. All 268 backend tests pass; changed-file whitespace check passes.
- Affected areas: backend curriculum/tests and documentation. Counts remain 97 U.S. History questions and 537 total. Topic-code mapping does not establish content depth; later-period expansion, diverse evidence, and history FRQ workflows remain outstanding. Overall goal remains active.

### Expansion milestone 25 — Period 4 diplomacy

- Previous goal turn classified as progress: Period 3 sequencing and stable-identity regression were tested and pushed. Began Period 4 with four original Monroe Doctrine questions and America on the World Stage (CED 4.4).
- Verified the public-domain excerpt against https://www.archives.gov/milestone-documents/monroe-doctrine. The prompt marks its omission explicitly; questions distinguish public policy, contemporary context, sourcing, and capacity to enforce a policy.
- U.S. History now has 101 questions across 55 topics; normal seed totals are 541 questions across 331 topics. Period 4 mapping, broader evidence formats, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 269 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 26 — Independent history source-set identities

- Previous goal turn classified as progress: Period 4 diplomacy questions were tested and pushed. Fixed a content-builder limitation: a second source set for the same curriculum code previously reused stimulus and item identifiers. Added optional validated `set_id` slugs while preserving identifiers when omitted for all existing content.
- Added tests for deterministic distinct identifiers under a shared curriculum code, backward compatibility, invalid identifiers, and a bank-wide audit of item uniqueness and stimulus-group consistency. Foundation questions without source-set metadata remain explicitly outside that metadata audit.
- Affected areas: backend content builder and tests. All 280 backend tests pass; changed-file whitespace check passes. No question-count changes (101 U.S. History / 541 total), frontend changes, or migrations.
- This enables repeated topic coverage and independent forms; it does not itself create those forms. Next: deeper Period 4 content and varied stimuli using stable set identifiers. Overall expansion goal remains active.

### Expansion milestone 27 — Seneca Falls and reform

- Previous goal turn classified as progress: stable source-set identifiers and bank-wide metadata checks were tested and pushed. Added four original Declaration of Sentiments questions and An Age of Reform (CED 4.11), using the named seneca-falls source set.
- Verified the public-domain excerpt against https://www.nps.gov/wori/learn/historyculture/declaration-of-sentiments.htm. Questions analyze founding-language adaptation, antebellum context, continuity/change, and evidence of actual legal outcomes. Every option includes its own rationale.
- U.S. History now has 105 questions across 56 topics; normal seed totals are 545 questions across 332 topics. Other reform movements, broader Period 4 mapping, later periods, and history FRQ workflows remain outstanding; overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 281 backend tests pass, including named-source validation and bank-wide identifier checks. Changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 28 — Indian removal and federal policy

- Previous goal turn classified as progress: reform questions were tested and pushed. Added four original questions and Jackson and Federal Power (CED 4.8), using a named removal-message source set.
- Verified Jackson’s December 1830 message at https://www.archives.gov/milestone-documents/jacksons-message-to-congress-on-indian-removal. The short public-domain excerpt remains explicitly attributed; questions critically evaluate its justification, plantation expansion, and omitted consequences for Native people. Complementary Native-authored sources remain needed.
- U.S. History now has 109 questions across 57 topics; normal seed totals are 549 questions across 333 topics. Period 4 mapping/depth, varied evidence, later periods, and history FRQ support remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 282 backend tests pass, including bank-wide source identity checks. Changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 29 — Cherokee opposition and consent

- Previous goal turn classified as progress: removal-policy questions were tested and pushed. Added four original questions using the 1836 Cherokee petition opposing the Treaty of New Echota, complementing the presidential source within CED 4.8.
- Verified the public-domain transcription and provenance at https://docsteach.org/document/cherokee-petition-protest-new-echota-treaty/ (National Archives Identifier 2127291). Questions examine representative authority, the Senate audience, comparison with Jackson’s justification, and limits on generalizing a petition to an entire nation.
- U.S. History now has 113 questions across 57 topics; normal seed totals are 553 questions across 333 topics. Remaining work includes broader Period 4 mapping/depth, non-text evidence, later periods, and history FRQ workflows. Overall goal remains active.
- Affected areas: backend content/tests and docs. All 283 backend tests pass, including distinct identifiers for two sources under the same curriculum code and bank-wide metadata consistency. Changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 30 — Bank War and executive authority

- Previous goal turn classified as progress: Cherokee petition questions were tested and pushed. Added four original Bank War questions under CED 4.8 using a distinct bank-veto source set.
- Public-domain excerpt checked against the Yale Avalon transcription at https://avalon.law.yale.edu/19th_century/ajveto01.asp; institutional context checked with Senate history and National Archives Bank War resources. Questions distinguish Jackson’s political justification from neutral financial evidence and ask what records support claims about executive authority.
- U.S. History now has 117 questions across 57 topics; normal seed totals are 557 questions across 333 topics. Nullification, broader Period 4 framework/depth, non-text evidence, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/tests and docs. All 284 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 31 — Nullification and compromise

- Previous goal turn classified as progress: Bank War questions were tested and pushed. Added four original nullification questions under CED 4.8, with an explicitly labeled instructional summary referenced to https://guides.loc.gov/nullification-proclamation.
- Questions distinguish a tariff concession from acceptance of nullification, compare Jackson’s selective use of federal power, and reject claims that a temporary settlement ended sectional conflict permanently. Each option includes a rationale.
- U.S. History now has 121 questions across 57 topics; normal seed totals are 561 questions across 333 topics. Broader Period 4 framework/depth, non-text evidence, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/tests and docs. All 285 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 32 — Cotton and industrial interdependence

- Previous goal turn classified as progress: nullification questions were tested and pushed. Added four original questions and Market Revolution: Industrialization (CED 4.5).
- Historical context checked against https://www.nps.gov/lowe/learn/historyculture/anti-slavery-in-lowell.htm. The explicitly labeled instructional summary connects northern textile production to enslaved cotton labor. Questions distinguish economic interdependence from identical legal status and from uniform political beliefs.
- U.S. History now has 125 questions across 58 topics; normal seed totals are 565 questions across 334 topics. More industrial technology/workplace evidence, broader Period 4 mapping, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 286 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 33 — Direct released-exam practice resources

- Previous goal turn classified as progress: industrialization questions were tested and pushed. In response to the request to find sites with old AP exams, verified College Board’s U.S. History archive and opened ten linked question/scoring PDFs: 2026, both 2025 sets, and both 2024 sets.
- Added these five question-paper/scoring-guide pairs to the existing course-detail resource list. Each title identifies the pre-2027 format. The existing frontend component renders these links; external responses are not saved or scored by WayPoint. No exam text or PDFs were mirrored.
- Source: https://apcentral.collegeboard.org/courses/ap-united-states-history/exam/past-exam-questions, checked October 3, 2026 using the client date. Actual PDF links were verified from that archive, including the single 2026 paper without a set suffix.
- Affected areas: backend resource catalog and API integration tests. All 287 backend tests pass; changed-file whitespace check passes. Question counts unchanged at 125 U.S. History / 565 total. Frontend code unchanged. Overall expansion remains incomplete and active.

### Expansion milestone 34 — Factory workers and labor reform

- Resumed original question-bank expansion at the user’s request after the discussion of external copyrighted exams. Previous implementation turn classified as progress: verified released-paper links were tested and pushed.
- Added four original Sarah Bagley questions and Market Revolution: Society and Culture (CED 4.6). Verified the public-domain 1846 letter excerpt as quoted by NPS at https://www.nps.gov/lowe/learn/historyculture/the-mill-girls-of-lowell.htm. Questions distinguish activist rhetoric from universal opinion and consider opportunities alongside corporate constraints.
- U.S. History now has 129 questions across 59 topics; normal seed totals are 569 questions across 335 topics. Broader Period 4 framework/depth, non-text evidence, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 288 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 35 — Early-republic political context

- Previous goal turn classified as progress: factory-worker questions were tested and pushed. Added four original questions and Contextualizing Period 4 (CED 4.1), using Jefferson’s 1801 inaugural appeal to shared principles.
- Public-domain language and historical context checked against https://www.loc.gov/exhibits/creating-the-united-states/peaceful-transition.html and the Library of Congress Jefferson collections. Questions distinguish conciliatory rhetoric from proof of unanimity and ask for evidence of institutional continuity during partisan succession.
- U.S. History now has 133 questions across 60 topics; normal seed totals are 573 questions across 336 topics. Remaining Period 4 topic mapping/depth, non-text evidence, later periods, and history FRQ workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 289 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 36 — Actionable topic depth audit

- Previous goal turn classified as progress: early-republic questions were tested and pushed. Expanded the existing content audit with ordered per-topic question counts, curriculum codes, difficulty levels, stimulus-group counts, question types, and explicit depth-gap flags. Added reporting of questions assigned to nonexistent curriculum topics.
- Ran the audit against the current history bank: 133 questions, 60 topics, 37 topics below three questions and 37 lacking difficulty variety. Four legacy Period 4 topics still lack explicit CED mappings. These findings confirm the bank is not comprehensive and identify concrete work beyond aggregate counts.
- Added fixture-based tests for ordering, absent metadata, unmapped questions, shared stimuli, and depth flags plus a live-bank consistency test. All 291 backend tests pass. Affected areas: backend audit tooling/tests and this context; no frontend or content-count changes.
- Next: fill missing Period 4 framework areas and deepen legacy topics, then later periods and representative FRQ/exam support. Overall goal remains active.

### Expansion milestone 37 — Louisiana Purchase and legacy-topic depth

- Previous goal turn classified as progress: actionable topic auditing was tested and pushed. Added four original Louisiana Purchase questions to the existing Markets and Westward Expansion topic, preserving topic identities while reducing an actual depth gap.
- Reference checked: https://history.state.gov/milestones/1801-1829/louisiana-purchase. The original instructional summary and questions connect Mississippi commerce, French imperial setbacks, and Jefferson’s constitutional concerns. Questions are tagged CED 4.2; the broad legacy topic still needs a complete multi-code mapping.
- U.S. History now has 137 questions across 60 topics; normal seed totals are 577 questions across 336 topics. Audit confirms topics below three questions and lacking difficulty variety both decreased from 37 to 36. Remaining coverage and exam/FRQ work are extensive; overall goal remains active.
- Affected areas: backend content/tests and docs. All 292 backend tests pass. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 38 — Regional interests and Missouri

- Previous goal turn classified as progress: Louisiana Purchase questions were tested and pushed. Added four original Missouri Compromise questions and Politics and Regional Interests (CED 4.3).
- Verified the settlement’s scope against https://www.archives.gov/milestone-documents/missouri-compromise. The original summary avoids claiming simultaneous admission dates and identifies the Missouri exception to the territorial restriction. Questions analyze Senate balance, expansion, and the limits of sectional compromise.
- U.S. History now has 141 questions across 61 topics; normal seed totals are 581 questions across 337 topics. Further Period 4 mapping/depth, non-text evidence, later periods, and representative FRQ/exam workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/curriculum/tests and docs. All 293 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 39 — Revival networks and reform

- Previous goal turn classified as progress: Missouri Compromise questions were tested and pushed. Added three original questions to the existing Religious Revival and Reform Movements topic, tagged CED 4.10 with a distinct voluntary-societies stimulus.
- Context checked against https://www.loc.gov/exhibits/religion/rel07.html. The explicitly labeled instructional summary connects revival networks and voluntary reform; questions require distinguishing organizational mechanisms and supporting evidence from unsupported generalizations.
- U.S. History now has 144 questions across 61 topics; normal seed totals are 584 questions across 337 topics. Further Period 4 mapping/depth, non-text evidence, later periods, and representative FRQ/exam workflows remain outstanding. Overall goal remains active.
- Affected areas: backend content/tests and docs. All 294 backend tests pass; changed-file whitespace check passes. Frontend unchanged; no copyrighted AP questions imported.

### Expansion milestone 40 — Distractor quality review

- Previous goal turn classified as progress: revival questions were tested and pushed. Editorial review found that several distractors relied on conspicuous chronological mismatches or unrelated objects, making author-assigned difficulty weak evidence of AP-style reasoning.
- Revised nine distractors and rationales across the three revival questions. Alternatives now distinguish voluntary associations from established churches, revivalism from deism, cooperation from doctrinal uniformity, and direct organizational evidence from contextual evidence. Prompts, keys, and item identifiers remain unchanged.
- Added a reseeding regression that restores revised options from stale data while preserving question and option IDs and matching every explanation to its option. All 295 backend tests pass; changed-file whitespace check passes.
- Counts unchanged: 144 U.S. History questions / 584 total. This review covers only the revival set; other recent sets need the same scrutiny. Passing structural tests does not establish educator review or calibrated AP difficulty. Broader content and exam-workflow work remain outstanding; overall goal remains active.

### Expansion milestone 41 — American literary culture

- Previous goal turn classified as progress: revival distractor improvements were tested and pushed. Resumed the authorized original-content expansion and added four Emerson-based questions plus The Development of an American Culture (CED 4.9).
- Public-domain excerpt and address context verified against https://depts.washington.edu/lsearlec/TEXTS/EMERSON/AMSCHOL.HTM. Questions address intellectual independence, scholarly audience, individual insight, and evidence of literary change. The evidence question distinguishes circulation and reception from changes in writers’ practices.
- U.S. History now contains 148 questions across 62 topics; normal seed totals are 588 questions across 338 topics. These counts do not establish comprehensive coverage, educator review, or calibrated difficulty. Remaining Period 4 coverage, later periods, non-text stimuli, and history FRQ/exam workflows remain outstanding; overall goal remains active.
- Affected areas: backend content/curriculum/tests and documentation. All 296 backend tests pass, including curriculum mapping, answer validation, and whole-bank idempotent seeding. Frontend unchanged. User changes to AGENTS.md remain untouched and excluded from the commit.

### Expansion milestone 42 — Expansion and limits of suffrage

- Previous goal turn classified as progress: American culture questions were tested and pushed. Added four original questions and Expanding Democracy (CED 4.7).
- Checked New York’s 1821 constitution, Article II, against its public-domain transcription at https://en.wikisource.org/wiki/New_York_Constitution_of_1821 and the New York State Archives record at https://considerthesourceny.org/document/new-york-state-constitution-1821-article-ii-voting-rights. The original summary distinguishes alternative qualifications from the separate $250 net freehold qualification for Black men and avoids equating legal eligibility with actual turnout.
- Items assess interpretation, limits of democratization, prescriptive-source limitations, and research design using linked property and voting records. All 297 backend tests pass, including new validation/mapping coverage and whole-bank reseeding. Changed-file whitespace checks pass.
- Affected areas: backend content/curriculum/tests and docs. U.S. History now has 152 questions across 63 topics; total bank 592 questions across 339 topics. Frontend unchanged; user AGENTS.md edits excluded. Further Period 4 coverage, later periods, non-text stimuli, history FRQ/exam workflows, and remaining courses are still incomplete. Overall goal remains active.

### Expansion milestone 43 — Black community institutions

- Previous goal turn classified as progress: suffrage expansion questions were tested and pushed. Added four original questions and African Americans in the Early Republic (CED 4.12).
- Historical sequence checked against the Episcopal Church Archives at https://exhibits.episcopalarchives.org/s/church-awakens/page/allen and NPS’s Free African Society material. The original summary follows mutual aid, Bethel, and the 1816 denomination; questions distinguish institutional autonomy from rejection of religious tradition and ask for evidence beyond founders’ biographies.
- This set addresses free Black institution building only. The topic still needs enslaved people’s experiences, resistance, and additional perspectives; its presence does not establish comprehensive topic coverage.
- U.S. History now has 156 questions across 64 topics; total bank 596 questions across 340 topics. All 298 backend tests pass, including content validation, mapping, and idempotent seeding; changed-file whitespace checks pass.
- Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md changes excluded. Remaining Period 4 coverage, later periods, non-text stimuli, history FRQ/exam workflows, and other courses remain outstanding. Overall goal stays active.

### Expansion milestone 44 — Literacy and resistance

- Previous goal turn classified as progress: Black community institution questions were tested and pushed. Added four original questions using a brief public-domain excerpt from Douglass’s 1845 Narrative, chapter VI, in the existing CED 4.12 topic.
- Verified the passage against the Library of Congress transcription and https://en.wikisource.org/wiki/Page:Narrative_of_the_Life_of_Frederick_Douglass,_an_American_Slave.djvu/57. Questions address literacy as resistance, unintended effects of repression, retrospective testimony, and corroborating evidence for resistance outside open rebellion.
- New stimulus identifiers remain distinct from the institution-building set. All 299 backend tests pass, including schema validation, distinct stimulus checks, and whole-bank idempotent seeding. Changed-file whitespace checks pass.
- Affected areas: backend content/tests and docs. U.S. History now contains 160 questions across 64 topics; normal seed totals are 600 questions across 340 topics. Frontend unchanged; user AGENTS.md edits excluded. This adds one enslaved author’s perspective, not comprehensive coverage of enslaved experiences. Remaining curriculum depth, later periods, non-text sources, history exam/FRQ workflows, and other subjects remain outstanding; overall goal remains active.

### Expansion milestone 45 — Legacy Period 4 curriculum mappings

- Previous goal turn classified as progress: Douglass literacy questions were tested and pushed. Mapped four broad legacy topics to their applicable Period 4 curriculum codes without renaming or replacing topics. Existing narrower topics remain separate.
- Checked the topic sequence against https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-at-a-glance.pdf. Added a database regression that removes the codes and reseeds, verifying restored mappings, retained non-CED skill tags, and unchanged topic IDs.
- All 300 backend tests pass. Live audit: 160 questions, 64 topics, 35 topics below three questions and 35 without difficulty variety. Period 4 now lacks only code 4.14 in its topic mapping; the legacy political-parties and cotton/slavery topics remain below three questions. Mapping presence does not imply sufficient content depth.
- Affected areas: backend curriculum/tests and context documentation. Counts unchanged at 600 questions / 340 topics overall. Frontend unchanged; user AGENTS.md edits excluded. Next: add Period 4 causation and deepen those legacy topics, then continue later periods and history exam/FRQ support. Overall goal remains active.

### Expansion milestone 46 — Period 4 causation

- Previous goal turn classified as progress: legacy curriculum mappings were tested and pushed. Added Causation in Period 4 and four original questions about transportation, commercial farming, alternative causes, and comparative evidence.
- Historical context checked against https://nysm.nysed.gov/research-collections/history/economic-history/news/transporting-grains-erie-canal. The stimulus is an original instructional summary; questions require evaluating causal mechanisms rather than attributing every economic change to the canal.
- Period 4 now maps all 14 CED codes. This is framework coverage only: legacy political-party and cotton/slavery topics still need depth, and other topics need additional stimuli and perspectives.
- All 301 backend tests pass after correcting an accidental date replacement in an existing test fixture; no application date changed. New tests check complete Period 4 mapping and question validation. U.S. History has 164 questions across 65 topics; total bank 604 questions across 341 topics.
- Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Overall goal remains active with later periods, non-text sources, history exam/FRQ workflows, and other courses outstanding.

### Expansion milestone 47 — Cotton production and coerced labor

- Previous goal turn classified as progress: Period 4 causation was tested and pushed. Added three original source-based questions to the existing cotton/slavery topic (CED 4.13), increasing its coverage from one to four questions without creating a replacement topic.
- Checked the historical mechanism against https://www.archives.gov/milestone-documents/patent-for-cotton-gin. The original summary distinguishes processing from planting and picking; items examine the scale of production, evidence connecting acreage to labor demand, and multiple causes rather than technological determinism.
- All 302 backend tests pass, including topic-depth assertions, question validation, and whole-bank reseeding. Changed-file whitespace checks pass. U.S. History now has 167 questions across 65 topics; overall bank has 607 questions across 341 topics.
- Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md changes excluded. The political-parties legacy topic remains shallow, and comprehensive regional society, later periods, diverse non-text sources, history FRQ/exam support, and remaining courses are unfinished. Overall goal remains active.

### Expansion milestone 48 — Electoral procedure and partisan mobilization

- Previous goal turn classified as progress: cotton/slavery depth additions were tested and pushed. Added three original questions to the existing political-parties topic using the 1824 electoral tally and subsequent controversy.
- Verified context against https://www.archives.gov/education/lessons/electoral-tally and House History materials. The original summary explicitly distinguishes the allegation of a corrupt bargain from proof; questions separate plurality from majority and analyze partisan sources without either accepting them uncritically or discarding them.
- Every stored Period 4 topic now meets the basic audit thresholds of three questions and two difficulty levels. A regression checks those thresholds alongside new-item validation. This does not certify comprehensive curriculum coverage, diverse source formats, editorial quality, or calibrated difficulty.
- All 303 backend tests pass. U.S. History now has 170 questions across 65 topics; overall bank has 610 questions across 341 topics. Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded.
- Next: expand Period 5 framework and source coverage while retaining the outstanding need for earlier-period depth, non-text stimuli, history FRQ/exam workflows, and other courses. Overall goal remains active.

### Expansion milestone 49 — Mexican-American War settlement

- Previous goal turn classified as progress: election-of-1824 questions and Period 4 minimum-depth checks were tested and pushed. Began Period 5 expansion with The Mexican-American War (CED 5.3) and three original questions on the 1848 settlement.
- Context verified against https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo. The original summary distinguishes financial terms from equal bargaining power and formal property/citizenship provisions from their implementation. Questions also connect territorial acquisition to sectional conflict.
- All 304 backend tests pass, including new-item validation, period/topic mapping, and whole-bank reseeding. U.S. History now contains 173 questions across 66 topics; total bank 613 questions across 342 topics.
- Affected areas: backend content/curriculum/tests and documentation. Frontend unchanged; user AGENTS.md changes excluded. Period 5 mapping and depth, earlier-period source diversity, later periods, history FRQ/exam support, and remaining courses remain outstanding. Overall goal remains active.

### Expansion milestone 50 — Period 5 legacy mapping and gap inventory

- Previous goal turn classified as progress: Mexican-American War settlement questions were tested and pushed. Mapped the four broad legacy Period 5 topics to relevant framework codes while retaining names, IDs, and existing non-CED skill tags.
- Framework checked against https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-at-a-glance.pdf. Mappings describe topic scope, not proof of question coverage: each legacy topic currently has only one item, while the added Mexican-American War topic has three.
- Live audit identifies missing topic mappings for 5.1 (context), 5.5 (regional differences), 5.9 (wartime government policy), and 5.12 (comparison). Broad existing topics also need narrower source coverage and more questions.
- Added a reseeding regression that removes curriculum tags, restores them, and verifies stable topic identities. All 305 backend tests pass. Counts unchanged: 173 U.S. History questions, 613 overall, 342 total topics.
- Affected areas: backend curriculum/tests and this context. Frontend unchanged; user AGENTS.md edits excluded. Next: source-based questions for missing Period 5 areas and deeper coverage of existing topics. Overall goal remains active; later periods, history exam/FRQ workflows, source diversity, and remaining subjects remain outstanding.

### Expansion milestone 51 — Emancipation and wartime authority

- Previous goal turn classified as progress: Period 5 legacy mappings were tested and pushed. Added Government Policies During the Civil War (CED 5.9) and four original questions using a brief public-domain Emancipation Proclamation excerpt.
- Text and context checked against https://www.archives.gov/milestone-documents/emancipation-proclamation. Items distinguish wartime authority, geographic scope, Black military service, and local implementation. The set avoids treating the proclamation as immediate nationwide abolition or an automatic end to military discrimination.
- All 306 backend tests pass, including curriculum mapping, new-question validation, and whole-bank idempotent reseeding. U.S. History has 177 questions across 67 topics; overall bank has 617 questions across 343 topics.
- Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Wartime economic policy and civil-liberties debates still need coverage, alongside missing Period 5 areas, later periods, non-text stimuli, history FRQ/exam workflows, and other courses. Overall goal remains active.

### Expansion milestone 52 — Reconstruction citizenship

- Previous goal turn classified as progress: emancipation and wartime authority questions were tested and pushed. Added three original Fourteenth Amendment questions to the existing Reconstruction topic (CED 5.10), increasing that topic from one to four questions.
- Public-domain constitutional wording checked against https://www.archives.gov/founding-docs/amendments-11-27. The excerpt retains the jurisdiction qualification; questions address formerly enslaved people’s status, constitutional constraints on states, and evidence of implementation rather than assuming guarantees immediately ended discrimination.
- All 307 backend tests pass, including new-item validation, topic-depth assertions, and whole-bank reseeding. U.S. History has 180 questions across 67 topics; overall bank has 620 questions across 343 topics.
- Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Reconstruction’s political, economic, and violent conflicts need additional coverage. Missing Period 5 areas, later periods, source diversity, history FRQ/exam support, and other courses remain outstanding. Overall goal remains active.

### Expansion milestone 53 — Reconstruction distractor review

- Previous goal turn classified as progress: Reconstruction citizenship questions were tested and pushed. Editorial review identified implausible distractors that weakened the historical reasoning required by that set.
- Replaced nine wrong options and their rationales across three questions. Alternatives now distinguish citizenship from land redistribution, officeholding restrictions and war debt; distinguish national constitutional limits from state discretion; and compare implementation records with evidence of adoption or public reception. Rechecked amendment sections against https://www.archives.gov/founding-docs/amendments-11-27.
- Prompts, keys, and item identifiers remain unchanged. Extended the existing reseeding regression to cover this set as well as revival questions, checking stable question/option IDs and matching rationales. All 308 backend tests pass; changed-file whitespace checks pass.
- Counts unchanged at 180 U.S. History questions / 620 overall. Affected areas: backend content/tests and context. Frontend unchanged; user AGENTS.md changes excluded. This focused review does not establish bank-wide editorial quality or calibrated difficulty; further content and exam work remains extensive. Overall goal remains active.

### Expansion milestone 54 — Question-level curriculum audit

- Previous goal turn classified as progress: Reconstruction distractors were improved, tested, and pushed. Enhanced the existing coverage audit to separate topic scope from explicitly tagged question coverage.
- Each topic now reports question counts by curriculum code (deduplicated per item), mapped codes with no tagged questions, question codes outside its mapping, and questions without curriculum tags. Missing tags are reported as metadata gaps, not assumed absence of substantive coverage.
- Fixture tests exercise broad mappings, duplicate tags, missing tags, and out-of-mapping codes. A live Reconstruction check confirms three questions tagged 5.10, no explicitly tagged 5.11 questions, and one untagged legacy item. The current history bank has no question codes outside their topic mappings.
- All 310 backend tests pass. Counts unchanged: 180 U.S. History questions / 620 overall. Affected areas: backend audit tooling/tests and context; frontend unchanged. User AGENTS.md edits excluded.
- This exposes incomplete coverage hidden by broad topic mappings and will guide further Period 5 additions and legacy-item review. Overall goal remains active, with extensive source diversity, later-period, exam/FRQ, and remaining-course work outstanding.

### Expansion milestone 55 — Compromise provisions and continuing conflict

- Previous goal turn classified as progress: question-level curriculum auditing was implemented, tested, and pushed. Added three original questions to the Compromise of 1850 legacy topic, tagged CED 5.4 and increasing topic depth from one to four items.
- Context checked against https://www.archives.gov/milestone-documents/compromise-of-1850. The original summary and questions distinguish ending the District’s slave trade from abolishing slavery, examine enforcement conflict in free states, and explain how immediate legislative agreement could coexist with unresolved sectional disagreement.
- All 311 backend tests pass, including new-content validation, existing-topic depth, and whole-bank reseeding. U.S. History now has 183 questions across 67 topics; total bank 623 questions across 343 topics.
- Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Broader CED 5.6 failure-of-compromise events still require explicit coverage, alongside missing Period 5 areas, later periods, source diversity, history FRQ/exam workflows, and remaining subjects. Overall goal remains active.

### Expansion milestone 56 — Kansas-Nebraska and failed compromise

- Previous goal turn classified as progress: Compromise of 1850 questions were tested and pushed. Added three original Kansas-Nebraska questions, explicitly tagged CED 5.6, in the existing broad sectional-conflict topic.
- Context checked against https://www.senate.gov/artandhistory/history/minute/Kansas_Nebraska_Act.htm. Items distinguish geographic restriction from popular sovereignty, examine competition for territorial political control, and evaluate evidence for partisan realignment.
- The topic now has seven questions: three explicitly tagged 5.4, three tagged 5.6, and one legacy item without a curriculum tag. New tests verify this distinction through the audit rather than inferring coverage from topic scope.
- All 312 backend tests pass. U.S. History has 186 questions across 67 topics; overall bank has 626 questions across 343 topics. Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded.
- Other failure-of-compromise events and perspectives remain to be covered. Missing Period 5 areas, later periods, non-text sources, history FRQ/exam support, and remaining courses are still outstanding; overall goal remains active.

### Expansion milestone 57 — Period 5 context and Texas annexation

- Previous goal turn classified as progress: Kansas-Nebraska questions were tested and pushed. Added Contextualizing Period 5 (CED 5.1) and three original questions connecting Texas annexation to earlier sectional conflict and competing motives.
- Historical context checked against Texas State Library annexation resources at https://www.tsl.texas.gov/exhibits/annexation/index.html and the Office of the Historian’s Texas annexation overview. The original summary supports questions about precedent, representation, and evidence distinguishing motives among opponents.
- All 313 backend tests pass, including new-question validation, period/topic mapping, and whole-bank reseeding. U.S. History has 189 questions across 68 topics; overall bank has 629 questions across 344 topics.
- Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Period 5 regional differences and comparison remain unmapped; existing topics require more varied sources and depth. Later periods, history FRQ/exam support, and remaining subjects are also outstanding. Overall goal remains active.

### Expansion milestone 58 — Regional difference and interdependence

- Previous goal turn classified as progress: Period 5 context and Texas annexation questions were tested and pushed. Added Sectional Conflict: Regional Differences (CED 5.5) and three original questions on cotton supply chains and political inference.
- Historical context checked against https://home.nps.gov/blrv/learn/historyculture/cotton-economy.htm. The original summary distinguishes commercial interdependence from identical labor institutions; questions require separate evidence before attributing uniform political beliefs to workers or manufacturers.
- All 314 backend tests pass, including new-content validation, period/topic mapping, and whole-bank reseeding. U.S. History has 192 questions across 69 topics; overall bank has 632 questions across 345 topics.
- Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Regional social and cultural differences need additional coverage. Period 5 comparison remains unmapped, while earlier and later periods, non-text sources, history FRQ/exam support, and remaining courses remain incomplete. Overall goal remains active.

### Expansion milestone 59 — Reconstruction amendment comparison

- Previous goal turn classified as progress: regional differences questions were tested and pushed. Added Comparison in Period 5 (CED 5.12) and three original questions distinguishing the Thirteenth, Fourteenth, and Fifteenth Amendments.
- Provisions checked against https://www.archives.gov/founding-docs/amendments-11-27. The summary retains the Thirteenth Amendment’s criminal-punishment exception and avoids equating the Fifteenth Amendment with universal adult suffrage. Questions also address congressional enforcement powers without assuming automatic implementation.
- Period 5 now maps all 12 framework codes through nine stored topics, including broad legacy topics. This does not mean all codes have adequate question coverage. New tests check the mapping and validate the comparative items; all 315 backend tests pass.
- U.S. History has 195 questions across 70 topics; total bank 635 questions across 346 topics. Affected areas: backend content/curriculum/tests and docs. Frontend unchanged; user AGENTS.md edits excluded.
- Next priorities include Manifest Destiny, military conflict, election/secession, and failure of Reconstruction. Earlier-period depth, later periods, non-text stimuli, history FRQ/exam support, and remaining subjects are unfinished. Overall goal remains active.

### Expansion milestone 60 — Mississippi campaign strategy

- Previous goal turn classified as progress: Reconstruction amendment comparison and Period 5 mappings were tested and pushed. Added three original questions to The Civil War, tagged CED 5.8, raising that topic from one to four questions.
- Context checked against https://www.nps.gov/vick/planyourvisit/park-maps-and-brochure.htm and NPS Port Hudson materials. The original summary preserves the July 4 Vicksburg / July 9 Port Hudson sequence; questions analyze strategic geography, chronology, and logistical evidence without treating a single victory as the end of the war.
- All 316 backend tests pass, including content validation, legacy-topic depth, and whole-bank reseeding. U.S. History has 198 questions across 70 topics; total bank 638 questions across 346 topics.
- Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md changes excluded. Other campaigns, election/secession, Manifest Destiny, Reconstruction’s failure, later periods, non-text sources, history FRQ/exam workflows, and remaining subjects remain unfinished. Overall goal remains active.

### Expansion milestone 61 — Oregon and routes to expansion

- Previous goal turn classified as progress: Mississippi campaign questions were tested and pushed. Added three original Oregon settlement questions to Manifest Destiny and Continued Expansion, tagged CED 5.2.
- Context checked against https://history.state.gov/milestones/1830-1860/oregon-territory. The summary specifies the mainland boundary, avoiding an inaccurate claim that every part of the boundary followed the parallel. Questions compare diplomacy and warfare and require evidence before inferring Native representation from a bilateral settlement.
- All nine stored Period 5 topics now meet basic thresholds of three questions and two difficulty levels. New tests check these thresholds and content validation; all 317 backend tests pass. These structural thresholds do not establish comprehensive coverage of all mapped codes.
- U.S. History has 201 questions across 70 topics; total bank 641 questions across 346 topics. Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md changes excluded.
- Election/secession and Reconstruction’s failure still lack dedicated tagged source sets. Other perspectives, later periods, non-text sources, history FRQ/exam workflows, and remaining subjects are unfinished. Overall goal remains active.

### Expansion milestone 62 — Election and secession justification

- Previous goal turn classified as progress: Oregon expansion questions were tested and pushed. Added three original questions tagged CED 5.7 to the existing Civil War topic.
- Context checked against https://home.nps.gov/articles/000/south-carolina-secession.htm. The original summary distinguishes the December 20 ordinance from the declaration four days later, identifies slavery’s centrality in the stated justification, and avoids treating the convention as speaking for every resident.
- Questions address claims, institutional perspective, and corroborating opponents’ characterizations against Lincoln’s contemporary positions. The Civil War topic now has three tagged 5.7 items, three tagged 5.8 items, and one untagged legacy item.
- All 318 backend tests pass, including explicit curriculum coverage and whole-bank reseeding. U.S. History now has 204 questions across 70 topics; total bank 644 questions across 346 topics. Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded.
- Reconstruction’s failure still needs a dedicated tagged source set. Wider election perspectives, later periods, non-text sources, history FRQ/exam support, and remaining subjects are unfinished. Overall goal remains active.

### Expansion milestone 63 — Resistance to Reconstruction and enforcement

- Previous goal turn classified as progress: election/secession questions were tested and pushed. Added three original questions on political intimidation and federal enforcement, tagged CED 5.11 within Reconstruction.
- Context checked against https://www.senate.gov/artandhistory/history/common/generic/EnforcementActs.htm. Items distinguish formal rights from effective participation, analyze national enforcement, and require longitudinal evidence before claiming durable success.
- Every Period 5 code now has explicitly tagged questions. This milestone does not establish full content coverage: Reconstruction’s collapse, including the retreat from enforcement, still requires broader treatment. Updated the audit regression to report both Reconstruction sets and its untagged legacy item accurately.
- All 319 backend tests pass, including a whole-Period-5 item-tag coverage check and whole-bank reseeding. U.S. History has 207 questions across 70 topics; total bank 647 questions across 346 topics.
- Affected areas: backend content/tests and docs. Frontend unchanged; user AGENTS.md edits excluded. Later periods, earlier depth and source diversity, non-text stimuli, history FRQ/exam support, and other subjects are unfinished. Overall goal remains active.

### Expansion milestone 64 — Period 6 foundation mapping

- Previous goal turn classified as progress: Reconstruction enforcement questions were tested and pushed. Began Period 6 expansion by mapping its four legacy topics to relevant framework codes while preserving names, IDs, and non-CED skill tags.
- Framework checked against https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-at-a-glance.pdf. Live audit confirms only four existing Period 6 questions, all without explicit curriculum tags; topic mappings do not imply item-level coverage.
- Missing topic mappings: 6.1 context, 6.4 New South, 6.9 responses to immigration, 6.10 middle class, 6.11 reform, 6.12 government controversies, 6.13 politics, and 6.14 continuity/change. Existing industrial, labor, migration, and western topics all require substantial depth.
- Added a database regression verifying restored curriculum tags and stable topic IDs after reseeding. All 320 backend tests pass. Counts unchanged: 207 U.S. History questions / 647 overall.
- Affected areas: backend curriculum/tests and context. Frontend unchanged; user AGENTS.md edits excluded. Period 6 expansion is next, with prior-period gaps, later periods, non-text stimuli, history FRQ/exam workflows, and remaining subjects still outstanding. Overall goal remains active.

### Expansion milestone 65 — Personalized practice selection

- Previous goal turn classified as progress: Period 6 foundation mappings were tested and pushed. User expanded the functional benchmark to Khan Academy / Duolingo; work now also prioritizes guided teaching, progression, and useful review alongside curriculum expansion. This benchmark is not yet met.
- Regular MCQ practice now uses each learner's latest completed attempt per candidate question: incorrect answers first, unseen material next, then successful answers, oldest reviewed work first. Existing subject/unit/topic and approval filters remain upstream; selection is persisted for resume. Timed and FRQ selection are unchanged.
- Added a backend selection service and integration regressions covering corrected mistakes, newer mistakes, selection limits, persisted order, other-user isolation, and unfinished-attempt exclusion. Fixed the SQLModel subquery result shape caught by the full suite. All 322 backend tests pass.
- Affected files: backend/app/services/practice/selection.py, backend/app/services/practice/session_service.py, backend/tests/integration/test_practice_selection.py, and CONTEXT.md. User AGENTS.md edits excluded. No frontend changes.
- This is prioritization, not a complete adaptive curriculum: large mistake backlogs can fill a session; difficulty adaptation and review/new-material quotas are not implemented. CourseStudy currently offers direct topic practice rather than guided lessons. Guided teaching, progression, comprehensive subject content, non-text stimuli, and history FRQ/exam workflows remain outstanding. Overall goal remains active.

### Expansion milestone 66 — Guided lessons with saved progress

- Previous goal turn classified as progress: personalized MCQ practice was tested and pushed as 2561a53. Following the user's Khan Academy / Duolingo benchmark, added an end-to-end guided-learning feature before continuing broader content work. Both backend and frontend scope was announced before implementation.
- AP English Language Unit 1 now offers three original lessons on rhetorical situation (1.A), claims/evidence (3.A), and evidence selection (4.A). Each includes substantive instruction, an explicitly fictional worked example, reasoning walkthrough, and a retryable check with option-specific feedback. Course alignment checked against https://apcentral.collegeboard.org/courses/ap-english-language-and-composition; no official exam questions copied.
- Backend: new lesson registry, authenticated unit lesson/check routes, versioned per-user completion model, and Alembic migration 20261003_lesson_progress. Completion inserts are idempotent under the composite primary key. Routes reject inactive curriculum, unknown lessons, stale revisions, invalid option types/ranges, and extra fields; learner identity is derived from authentication. Answer keys are omitted from lesson reads. Correct checks do not award XP or change mastery.
- Frontend: course detail advertises lessons from the backend-derived lesson count. GuidedLessons reuses PillButton and the current course visual system; it supports free navigation, checking/retrying, save-error recovery, automatic selection of the first unfinished lesson on reopening, and launching the unit's practice with existing format/length settings. Content renders as escaped text. Read the installed Next.js use-client documentation before editing.
- Verification: all 324 PostgreSQL-backed backend tests, 100 frontend tests, and ESLint pass. Applied the new migration successfully to the local browser-test database. Production build and all nine real-Clerk Chromium tests pass, including the new lesson read/retry/persist/reload/resume/practice journey. Mobile overflow assertion passes and full-page screenshot inspected. Initial sandbox-only DB connection failure was resolved by the established elevated test runner; corrected the new test fixture's zero-based unit order to match published one-based course units.
- Affected areas: backend content/model/router/schema/migration/tests, frontend course/lesson UI/API/types/tests, docs/GUIDED_LEARNING.md, and this context. User AGENTS.md changes remain untouched and excluded.
- Limits: only the first English Language unit has guided lessons. A single formative check marks each lesson complete; it is not mastery certification. Reading position and unsubmitted choices do not survive reload. Lesson revision must be incremented for substantive check/objective changes. Full lesson coverage, richer progression, content depth across courses, non-text sources, history FRQ/exam workflows, and remaining AP subjects are unfinished. Question bank remains 647 questions across seven available courses. Overall goal remains active.

### Expansion milestone 67 — Audience and thesis lesson sequence

- Previous goal turn classified as progress: guided-learning infrastructure and the first English Language sequence were tested and pushed as b31bd20. Expanded the highest-participation course's guided instruction with six distinct Unit 2 lessons: audience values (1.B), adapting writing to readers (2.B), supporting claims (3.A), evidence scope (4.A), recognizing a thesis (3.B), and composing a defensible thesis (4.B).
- Each original lesson includes explanation, fictional worked example, walkthrough, and three-option formative check with specific feedback. Examples vary across museums, housing, school decisions, public access, and community proposals. Curriculum categories rechecked against https://apcentral.collegeboard.org/courses/ap-english-language-and-composition and existing seeded unit skills.
- The backend registry publishes three lessons in Unit 1 and six in Unit 2. Existing frontend consumes backend lesson counts and sequences without frontend changes. Added API regressions for discovery, every answer/feedback branch, successful completion, cross-unit slug rejection, and learner/unit isolation, plus checks against seeded skill mappings. Updated the unavailable-unit fixture to Unit 3.
- All 326 backend tests pass against PostgreSQL; scoped whitespace checks pass. No frontend behavior or schema changes; previous milestone's production build, 100 frontend tests, and nine browser flows remain the latest frontend verification, not rerun for this content-only change.
- Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. User AGENTS.md edits excluded. Nine guided lessons now available; question bank remains 647. Units 3–9, deeper writing instruction and practice, remaining subjects, later U.S. History periods, non-text stimuli, and history exam workflows remain incomplete. Overall goal remains active.

### Expansion milestone 68 — Reasoning and development lessons

- Previous goal turn classified as progress: Unit 2 lessons were tested and pushed as 8a4e668. Added six distinct English Language Unit 3 lessons for skills 3.A, 4.A, 5.A, 6.A, 5.C, and 6.C, following the seeded curriculum sequence.
- Instruction addresses unstated assumptions, complementary evidence, causal and scope leaps, explanatory commentary, recognizing development methods, and selecting a method for an argument. Each lesson contains original teaching, a fictional worked example, a walkthrough, and a formative check with feedback for all three choices. Fifteen guided lessons are now available across Units 1–3.
- Added an API regression covering Unit 3 discovery, all answer/feedback branches, persisted completion, learner/unit isolation, and historical revision exclusion. Existing content checks validate lesson skills against seeded topics. Moved the unavailable-unit fixture to Unit 4.
- All 327 PostgreSQL-backed backend tests pass; scoped whitespace checks pass. Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. Frontend unchanged; the prior 100 frontend tests and nine browser flows remain the latest frontend verification. User AGENTS.md changes excluded.
- Units 4–9 still lack lessons. Checks are formative foundations, not evidence of comprehensive writing competence; extended composition feedback and deeper progression remain unfinished. Question bank remains 647, and wider AP coverage, U.S. History expansion, non-text sources, and history exam workflows remain outstanding. Overall goal remains active.

### Expansion milestone 69 — Purpose and structure lessons

- Previous goal turn classified as progress: Unit 3 reasoning lessons were tested and pushed as fc20add. Added six original English Language Unit 4 lessons aligned to seeded skills 1.A, 2.A, 3.B, 4.B, 5.C, and 6.C.
- Instruction covers occasion and rhetorical choice, purposeful openings/conclusions, qualified thesis structure, rhetorical-analysis thesis writing, definition/contrast, and combining development methods. Examples include public warnings, accessibility, volunteering, and decision-making; every lesson has a worked example, walkthrough, and option-specific formative feedback. Twenty-one lessons now span Units 1–4.
- Generalized the sequence integration test to exercise Unit 2 and Unit 4 publication, skill order, all feedback branches, correct completion, cross-unit rejection, and learner/unit isolation. Updated the unavailable-unit fixture to Unit 5. All 328 backend tests and scoped whitespace checks pass.
- Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. Frontend unchanged and consumes the new sequence through existing APIs. No frontend checks rerun for this content-only change. User AGENTS.md edits excluded.
- Units 5–9, extended writing practice/feedback, broader source diversity, deeper adaptive progression, other AP subjects, U.S. History later periods, non-text stimuli, and history exam workflows remain unfinished. Guided checks do not certify writing competence or full curriculum coverage. Question bank remains 647; overall goal remains active.

### Expansion milestone 70 — Coherence and style lessons

- Previous goal turn classified as progress: Unit 4 purpose/structure lessons were tested and pushed as c37065c. Added six original English Language Unit 5 lessons matching seeded skills 5.A, 6.A, 5.B, 6.B, 7.A, and 8.A.
- Lessons teach qualified explanations, detail-specific commentary, paragraph relationships, meaningful transitions, diction/comparison, and purposeful style. Fictional examples broaden the teaching contexts to science reports, memoir, arts criticism, archives, and museum interpretation. Each lesson provides instruction, worked analysis, and a three-option formative check with tailored feedback. Twenty-seven lessons now cover Units 1–5.
- Extended the parameterized API regression to validate Unit 5 discovery, all answer/feedback branches, completion, and learner/unit isolation; all lesson skills continue to be checked against the seeded curriculum. Updated the unavailable-unit fixture to Unit 6. All 329 backend tests and scoped whitespace checks pass.
- Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. Existing frontend serves the sequence without changes; no frontend tests rerun for content-only work. User AGENTS.md edits excluded.
- These lessons provide scaffolding, not full AP-level assessment or proof of writing competence. Units 6–9, extended writing feedback, deeper adaptive progression, broader AP content, U.S. History later periods, non-text sources, and history exam workflows remain unfinished. Question bank remains 647; overall goal remains active.

### Expansion milestone 71 — Sources and thesis refinement lessons

- Previous goal turn classified as progress: Unit 5 coherence/style lessons were tested and pushed as 4aa74ec. Added six original English Language Unit 6 lessons matching seeded skills 3.A, 4.A, 3.B, 4.B, 7.A, and 8.A.
- Lessons address source relevance and knowledge limits, relationships among sources, identifying complex central positions, revising a thesis in response to evidence, tonal shifts, and precise criticism. Fictional examples include archives, transit, museum restoration, memoir, and public reports. Each has instruction, a worked example, commentary, and a three-option formative check with tailored feedback. Thirty-three lessons now span Units 1–6.
- Extended the parameterized API test to cover Unit 6 publication, skill sequence, every feedback branch, completion, cross-unit slug rejection, and learner/unit isolation. Updated the unavailable-unit fixture to Unit 7. All 330 backend tests and scoped whitespace checks pass.
- Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. Frontend unchanged; no frontend checks rerun for this content-only change. User AGENTS.md changes excluded.
- Remaining: Units 7–9, extended composition practice/feedback, substantive educator review, deeper learning progression, broader AP subjects, later U.S. History periods, non-text stimuli, and history exam workflows. Formative lesson completion does not establish exam readiness. Question bank remains 647; overall goal remains active.

### Expansion milestone 72 — Qualification and sentence choices

- Previous goal turn classified as progress: Unit 6 source/refinement lessons were tested and pushed as 15b95de. Added eight original English Language Unit 7 lessons matching seeded skills 1.A, 2.A, 3.C, 4.C, 7.B, 8.B, 7.C, and 8.C.
- Lessons cover competing purposes, framing a qualified position, concessions, fair responses to objections, sentence emphasis, clause relationships, punctuation effects, and conventions that preserve meaning. Original examples and feedback distinguish grammatical correctness from unsupported causal changes and distinguish qualification from surrender. Forty-one lessons now span Units 1–7.
- Extended the sequence API regression for all Unit 7 answer branches, publication, completion, cross-unit rejection, and learner/unit isolation. The shared test now supports varying sequence lengths. Unavailable-content checks use an unregistered unit order (99) rather than the next unit in development. All 331 backend tests and scoped whitespace checks pass.
- Affected files: backend/app/content/lessons.py, backend/tests/integration/test_guided_lessons.py, docs/GUIDED_LEARNING.md, and CONTEXT.md. Frontend unchanged; no frontend tests rerun for content-only work. User AGENTS.md edits excluded.
- Units 8–9, extended composition practice/feedback, educator review, deeper progression, wider AP coverage, later U.S. History periods, non-text sources, and history exam workflows remain unfinished. Formative checks are not full assessment of the mapped skills. Question bank remains 647; overall goal remains active.
