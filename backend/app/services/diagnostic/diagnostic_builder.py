"""Builds a short, condensed diagnostic whose per-unit question allocation
mirrors the real AP exam's relative unit weighting (largest-remainder
apportionment so counts sum exactly to the target), skewed toward moderate
difficulty since a diagnostic should establish a baseline, not be a stress test.
"""

import random

from sqlmodel import Session, select

from app.core.exceptions import DomainError
from app.services.practice.scope import validate_practice_scope
from app.models.practice import PracticeSession
from app.models.question import Question
from app.models.subject import Unit
from app.services.practice.self_review import requires_self_review

PREFERRED_DIFFICULTIES = {2, 3, 4}


def allocate_questions_per_unit(
    units: list[tuple[int, float]], total_questions: int
) -> dict[int, int]:
    """units: (unit_id, ap_weight_midpoint) pairs. Largest-remainder
    apportionment so the returned counts sum exactly to total_questions."""
    weight_sum = sum(w for _, w in units)
    if weight_sum <= 0 or not units:
        return {}

    raw = [(uid, total_questions * w / weight_sum) for uid, w in units]
    allocation = {uid: int(r) for uid, r in raw}
    remainder = total_questions - sum(allocation.values())
    by_largest_fraction = sorted(raw, key=lambda t: t[1] - int(t[1]), reverse=True)
    for uid, _ in by_largest_fraction[:remainder]:
        allocation[uid] += 1
    return allocation


def build_diagnostic_session(
    db: Session,
    user_id: int,
    subject_id: int,
    total_questions: int,
    rng: random.Random | None = None,
) -> tuple[PracticeSession, list[Question]]:
    validate_practice_scope(db, subject_id)
    if not 1 <= total_questions <= 60:
        raise DomainError("Diagnostic question count must be between 1 and 60")
    rng = rng or random.Random()
    units = list(db.exec(select(Unit).where(Unit.subject_id == subject_id, Unit.is_active == True)).all())
    allocation = allocate_questions_per_unit(
        [(u.id, (u.ap_weight_min + u.ap_weight_max) / 2.0) for u in units], total_questions
    )

    selected_questions: list[Question] = []
    remaining: list[Question] = []
    for unit in units:
        candidates = list(db.exec(select(Question).where(
            Question.subject_id == subject_id,
            Question.unit_id == unit.id,
            Question.is_active == True,  # noqa: E712
            Question.validation_status == "approved",
        )).all())
        # Essays requiring judgment cannot supply an automatic baseline.
        candidates = [q for q in candidates if not requires_self_review(q)]
        rng.shuffle(candidates)
        # Stable ordering retains randomness within each difficulty group.
        candidates.sort(key=lambda q: q.difficulty not in PREFERRED_DIFFICULTIES)
        count = allocation.get(unit.id, 0)
        selected_questions.extend(candidates[:count])
        remaining.extend(candidates[count:])

    # Sparse units must not shorten a diagnostic when other units have content.
    rng.shuffle(remaining)
    remaining.sort(key=lambda q: q.difficulty not in PREFERRED_DIFFICULTIES)
    selected_questions.extend(remaining[:total_questions - len(selected_questions)])
    if not selected_questions:
        raise DomainError("No approved questions are available for this diagnostic yet.")

    session = PracticeSession(
        user_id=user_id,
        subject_id=subject_id,
        session_type="diagnostic",
        total_questions=len(selected_questions),
        session_metadata={"question_ids": [q.id for q in selected_questions]},
    )
    db.add(session)
    db.flush()
    return session, selected_questions
