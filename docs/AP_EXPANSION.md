# Comprehensive AP expansion

Status: **in progress**, starting with AP English Language and Composition.
The earlier six-course delivery remains the working software foundation; it does
not satisfy the expanded all-course content requirement.

## Order and evidence

Use exam participation as the available proxy for popularity, not course enrollment.
The [2025 Program Summary Report](https://apcentral.collegeboard.org/media/pdf/program-summary-report-2025.pdf)
is the latest subject-volume report found on the official data page as of 2026-10-03.
`backend/scripts/seed_data/rollout.py` records all 40 reported subjects in descending
order. Business with Personal Finance, Cybersecurity, and Networking appear in the
[current course catalog](https://apcentral.collegeboard.org/courses) without 2025
counts; their launch status and exam specifications must be verified before rollout.

Start: English Language → United States History → English Literature → World History:
Modern → United States Government → Psychology → Biology → Calculus AB → Human
Geography → Statistics. Continue through the complete checked-in ranking.

## Definition of coverage

A course requires a current official framework and exam-format reference, all tested
skills/topics mapped, diverse original stimuli and difficulty, explanation of every
MCQ option, appropriate response formats, useful rubrics, and representative timed
practice. Source texts/data written for practice must be labeled original/fictional.
A question count alone does not establish alignment, diversity, or educational quality.

English Language's initial depth target is 180 distinct MCQs across at least 20
independent passage sets, 18 essays spanning all three task types, and at least three
questions with more than one difficulty per unit/skill topic. Four independent MCQ
forms should each contain 45 questions in five sets, including 23–25 reading and
20–22 writing questions. Essays need synthesis source packs, rhetorical-analysis
passages, and argument tasks; the 60-minute/135-minute section structure must be
supported. These are WayPoint content targets, not College Board requirements for a
commercial practice bank or a claim of psychometric equivalence.

Portfolio, research, performance, listening, and speaking assessments require their
actual task workflows. They must not be represented as generic MCQ-only courses.
Self-review is identified as student assessment and does not generate automatic
mastery or accuracy rewards. Educator review is a separate quality status; software
checks must never claim to provide it.

## Current English Language work

- Nine-unit progression with 22 framework skill codes and 49 unit/skill topics.
- Four independent 45-question MCQ forms: each has three reading sets (24 questions)
  and two revision sets (21 questions), for 180 questions across twenty original passages,
  levels 2–4, and individual rationales.
- Form D combines a theater memoir, a seed-saving reflection, civic testimony,
  and music-rehearsal and trail-description revision drafts. Its essay section
  covers repairability purchasing, civic testimony, and public recognition.
- Twelve essays across four sets: synthesis (six sources per task, including data and a
  visual stimulus), rhetorical analysis, and argument; models and six-point rubric
  reflection. All four MCQ forms meet the published skill-category percentage ranges.
  Form C adds a public opening address, a nature essay, a fictional historical civic
  letter, and tool-lending and neighborhood heat-mapping revision drafts. All 49
  unit/skill topics now have at least three questions. Every topic
  has difficulty variety. Labels are author estimates, not calibrated difficulty.
- Durable, owned rubric review implemented in backend and frontend. Mixed-session
  accuracy excludes self-review responses. Anonymous, foreign, unfinished, and invalid
  review requests are rejected. Pre-submission guidance identifies the scoring method;
  essay entry provides a word count and bounded, accessible text field. Diagnostics
  exclude self-review essays, and courses without official unit weights use an explicit
  equal-unit fallback for mastery and planning.
- Section-aware Forms A/B/C/D now support server-enforced deadlines, saved drafts,
  revision conflict protection, history resume, locked sections, and final results
  with persistent essay self-review. Standard/1.5x/2x practice time and an explicitly
  untimed inter-section break are available. These are rehearsal tools, not official
  AP score predictions or an accommodation approval system.
- Candidate course remains outside live enrollment until content depth is ready.
  Next: six additional essays and course activation verification.

For candidate browser verification, point `DATABASE_URL` at a disposable database
named `waypoint_test`, `waypoint_migration_test`, or `waypoint_exam_test`, run migrations
and the regular seed, then run `python -m scripts.seed_exam_preview` from `backend/`.
Run the frontend Playwright suite with the same database and
`E2E_INCLUDE_CANDIDATES=1`; real Clerk test credentials are required. The preview seed
rejects other database names and does not change the production course registry.

Run `python -m scripts.content_audit` from `backend/` to see the current 43-course
inventory and structural gaps. The audit separates live foundation banks, candidate
content, and unstarted courses. Its output is not an educator endorsement.

References checked: [course framework](https://apcentral.collegeboard.org/courses/ap-english-language-and-composition),
[exam structure and rubric links](https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam).
