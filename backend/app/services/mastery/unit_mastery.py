"""unit_mastery = equal-weighted average of topic_mastery within the unit.

The product spec doesn't specify per-topic weighting within a unit (only that
subject mastery is weighted by AP unit frequency) - equal weighting across
topics is the documented default, since there's no published per-topic AP
weighting to draw on.
"""

from sqlmodel import Session, select

from app.models.mastery import TopicMastery, UnitMastery
from app.models.subject import Topic


def compute_unit_mastery_from_topics(
    topic_scores: list[tuple[float, float]],
) -> tuple[float, float]:
    """topic_scores: list of (mastery_score, confidence_score) for every topic
    in the unit. Topics never attempted should be passed as (0.0, 0.0).
    Returns (mastery_score, confidence_score) for the unit.
    """
    if not topic_scores:
        return 0.0, 0.0
    mastery_avg = sum(m for m, _ in topic_scores) / len(topic_scores)
    confidence_avg = sum(c for _, c in topic_scores) / len(topic_scores)
    return mastery_avg, confidence_avg


def recompute_unit_mastery(db: Session, user_id: int, unit_id: int) -> UnitMastery:
    topic_ids = db.exec(select(Topic.id).where(Topic.unit_id == unit_id)).all()
    tms_by_topic = {
        tm.topic_id: tm
        for tm in db.exec(
            select(TopicMastery).where(
                TopicMastery.user_id == user_id, TopicMastery.topic_id.in_(topic_ids)
            )
        ).all()
    }
    topic_scores = [
        (tms_by_topic[tid].mastery_score, tms_by_topic[tid].confidence_score)
        if tid in tms_by_topic
        else (0.0, 0.0)
        for tid in topic_ids
    ]
    mastery_score, confidence_score = compute_unit_mastery_from_topics(topic_scores)

    um = db.get(UnitMastery, (user_id, unit_id))
    if um is None:
        um = UnitMastery(user_id=user_id, unit_id=unit_id)
    um.mastery_score = mastery_score
    um.confidence_score = confidence_score
    db.add(um)
    return um
