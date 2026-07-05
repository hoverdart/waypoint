"""subject_mastery = average of unit_mastery weighted by each unit's AP exam
frequency (the midpoint of ap_weight_min/ap_weight_max). Also derives the
predicted 1-5 AP score, which the source spec explicitly leaves unformulated -
this is a documented, tunable heuristic pending real outcome data.
"""

from sqlmodel import Session, select

from app.core.mathutils import clamp
from app.models.mastery import SubjectMastery, UnitMastery
from app.models.subject import Unit

# Mastery thresholds mapping to a base 1-5 AP score prediction.
SCORE_THRESHOLDS = [
    (0.85, 5),
    (0.70, 4),
    (0.50, 3),
    (0.30, 2),
    (0.0, 1),
]

# Below this confidence, shrink the prediction halfway toward the conservative
# middle (3) so a thin sample can't swing a prediction to an extreme.
LOW_CONFIDENCE_THRESHOLD = 0.3
LOW_CONFIDENCE_SHRINKAGE = 0.5
MEDIUM_CONFIDENCE_THRESHOLD = 0.6
MEDIUM_CONFIDENCE_SHRINKAGE = 0.25
CONSERVATIVE_MIDPOINT_SCORE = 3


def compute_subject_mastery_from_units(
    unit_scores: list[tuple[float, float, float]],
) -> tuple[float, float]:
    """unit_scores: list of (ap_weight_midpoint, mastery_score, confidence_score).
    Returns (mastery_score, confidence_score) for the subject.
    """
    weight_sum = sum(w for w, _, _ in unit_scores)
    if weight_sum <= 0:
        return 0.0, 0.0
    mastery = sum(w * m for w, m, _ in unit_scores) / weight_sum
    confidence = sum(w * c for w, _, c in unit_scores) / weight_sum
    return mastery, confidence


def predict_ap_score(mastery_score: float, confidence_score: float) -> int:
    base = next(score for threshold, score in SCORE_THRESHOLDS if mastery_score >= threshold)

    if confidence_score < LOW_CONFIDENCE_THRESHOLD:
        base = round(base * (1 - LOW_CONFIDENCE_SHRINKAGE) + CONSERVATIVE_MIDPOINT_SCORE * LOW_CONFIDENCE_SHRINKAGE)
    elif confidence_score < MEDIUM_CONFIDENCE_THRESHOLD:
        base = round(
            base * (1 - MEDIUM_CONFIDENCE_SHRINKAGE)
            + CONSERVATIVE_MIDPOINT_SCORE * MEDIUM_CONFIDENCE_SHRINKAGE
        )

    return int(clamp(base, 1, 5))


def recompute_subject_mastery(db: Session, user_id: int, subject_id: int) -> SubjectMastery:
    units = db.exec(select(Unit).where(Unit.subject_id == subject_id)).all()
    unit_ids = [u.id for u in units]
    ums_by_unit = {
        um.unit_id: um
        for um in db.exec(
            select(UnitMastery).where(
                UnitMastery.user_id == user_id, UnitMastery.unit_id.in_(unit_ids)
            )
        ).all()
    }
    unit_scores = [
        (
            (u.ap_weight_min + u.ap_weight_max) / 2.0,
            ums_by_unit[u.id].mastery_score if u.id in ums_by_unit else 0.0,
            ums_by_unit[u.id].confidence_score if u.id in ums_by_unit else 0.0,
        )
        for u in units
    ]
    mastery_score, confidence_score = compute_subject_mastery_from_units(unit_scores)

    sm = db.get(SubjectMastery, (user_id, subject_id))
    if sm is None:
        sm = SubjectMastery(user_id=user_id, subject_id=subject_id)
    sm.mastery_score = mastery_score
    sm.confidence_score = confidence_score
    sm.predicted_ap_score = predict_ap_score(mastery_score, confidence_score)
    db.add(sm)
    return sm
