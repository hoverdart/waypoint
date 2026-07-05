"""Shared post-session mastery rollup, used by both the diagnostic scorer and
regular practice session submission so the two flows can't drift apart.
"""

from datetime import datetime

from sqlmodel import Session, select

from app.models.subject import Topic
from app.services.mastery.subject_mastery import recompute_subject_mastery
from app.services.mastery.topic_mastery import AttemptSignal, update_topic_mastery_after_session
from app.services.mastery.unit_mastery import recompute_unit_mastery


def apply_session_attempts_to_mastery(
    db: Session,
    user_id: int,
    subject_id: int,
    attempts_by_topic: dict[int, list[AttemptSignal]],
    now: datetime,
) -> None:
    touched_unit_ids: set[int] = set()
    for topic_id, attempts in attempts_by_topic.items():
        recent_results = [a.is_correct for a in attempts]
        update_topic_mastery_after_session(db, user_id, topic_id, attempts, recent_results, now=now)
        topic = db.get(Topic, topic_id)
        touched_unit_ids.add(topic.unit_id)
    db.flush()

    for unit_id in touched_unit_ids:
        recompute_unit_mastery(db, user_id, unit_id)
    db.flush()

    recompute_subject_mastery(db, user_id, subject_id)
