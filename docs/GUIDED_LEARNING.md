# Guided learning

Guided sequences are available inside AP English Language, Units 1–3. Open
a published unit on the course page and select **Open guided lessons**. Unit 1 has three
original lessons on rhetorical context, claims and evidence, and evidence selection.
Unit 2 has six distinct lessons on audience inference, audience-aware revision,
supporting claims, evidence limits, recognizing a thesis, and writing a defensible
thesis. Unit 3 adds six lessons on assumptions, complementary evidence, lines of reasoning,
commentary, and reading and writing with methods of development. Later units do
not yet have guided sequences.
Each provides an explanation, fictional worked example, analysis, and a retryable
three-option understanding check. Students may move freely between lessons and
start the unit's practice using the course's selected format and session length.

Correct checks save completion to the authenticated account. Reopening the sequence
selects the first unfinished lesson. Completion does not award XP, update mastery,
or imply exam readiness. Reading position and unsubmitted check choices are not
saved across reloads. These are foundational sequences, not a complete lesson curriculum.

## Setup and maintenance

Run `alembic upgrade head` from `backend/` with the intended `DATABASE_URL` before
serving the feature. Migration `20261003_lesson_progress` adds the completion table.
Its key is learner, unit, lesson slug, and revision; repeat successful checks are
idempotent, including concurrent requests. Rollback removes lesson completion data.

Lesson definitions live in `backend/app/content/lessons.py`. They contain original
instructional content and are selected by course code and active unit order. Keep
slugs stable. Increment a lesson's revision when changing its check or substantially
changing its learning objective: old completions then remain historical and do not
complete the new version. Requests carrying a stale revision receive HTTP 409.

Keep examples explicitly fictional where applicable. Check curriculum alignment
against current primary sources and review pedagogy, distractors, and feedback;
passing structural tests does not replace educator review. Publish content only to
the intended active unit. The course-detail API derives `lesson_count` from the
same content registry used by the lesson routes, so the UI does not advertise empty
sequences.

## API and security

- `GET /units/{unit_id}/lessons` requires authentication, returns lessons and the
  caller's version-specific completion, and excludes answer keys and feedback.
- `POST /units/{unit_id}/lessons/{slug}/check` accepts only integer `option` (0–2)
  and positive integer `revision`. It returns correctness and feedback for the
  selected option. Only a correct answer persists completion.
- User identity always comes from authentication. Callers cannot choose a learner
  ID. Unknown/inactive units or subjects and unavailable lessons are rejected.
- Lessons render as React text, without HTML injection or external source scripts.

The checks are formative and allow retries. They are not secret assessments and
are not suitable as prerequisites for high-stakes certification.
