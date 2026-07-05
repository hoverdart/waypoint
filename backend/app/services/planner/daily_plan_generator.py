"""Selects the highest-priority topics for a subject until a study-time-based
point budget is exhausted. Mixes in occasional calibration checks. Recomputes
candidates from live mastery/timer state every call - a topic skipped
yesterday naturally stays eligible today because skipping it never reset its
timer or touched its mastery, not because plan items are copied forward.
"""

import random
from dataclasses import dataclass
from datetime import date

from sqlmodel import Session, select

from app.models.mastery import TopicMastery
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.question import Question
from app.models.subject import Topic, Unit, UserSubject
from app.services.planner.point_budget import ACTIVITY_COSTS
from app.services.planner.point_budget import minutes_to_points as _minutes_to_points
from app.services.planner.priority import derive_priority_factors, score_from_factors
from app.services.planner.reasons import reason_for_item

# Chance a calibration item is mixed into a generated plan (spec: "occasional",
# no exact number given - documented default).
CALIBRATION_CHANCE = 0.15
CALIBRATION_CONFIDENCE_THRESHOLD = 0.7

CHALLENGE_MASTERY_THRESHOLD = 0.8
CHALLENGE_AP_WEIGHT_THRESHOLD_PERCENT = 10.0
FRQ_CHANCE_AT_HIGH_MASTERY = 0.3
REVIEW_MASTERY_CEILING = 0.6
WEAKNESS_MASTERY_CEILING = 0.3

ITEM_TYPE_TO_ACTIVITY_COST_KEY = {
    "weakness": "normal_topic",
    "review": "easy_review",
    "frq": "hard_frq",
    "challenge": "timed_mini_exam",
    "calibration": "easy_review",
}

DEFAULT_STUDY_MINUTES_PER_DAY = 20


@dataclass
class TopicCandidate:
    topic_id: int
    unit_id: int
    subject_id: int
    mastery_score: float
    confidence_score: float
    retention_score: float
    topic_timer: float
    ap_weight_midpoint_percent: float
    has_frq_questions: bool = False
    calibration_eligible: bool = False


@dataclass
class SelectedItem:
    topic_id: int
    unit_id: int
    subject_id: int
    item_type: str
    point_cost: int
    priority_score: float
    reason: str


def determine_item_type(candidate: TopicCandidate, rng: random.Random) -> str:
    if candidate.mastery_score < WEAKNESS_MASTERY_CEILING:
        return "weakness"
    if candidate.mastery_score < REVIEW_MASTERY_CEILING:
        return "review"
    if (
        candidate.mastery_score >= CHALLENGE_MASTERY_THRESHOLD
        and candidate.ap_weight_midpoint_percent >= CHALLENGE_AP_WEIGHT_THRESHOLD_PERCENT
    ):
        return "challenge"
    if candidate.has_frq_questions and rng.random() < FRQ_CHANCE_AT_HIGH_MASTERY:
        return "frq"
    return "review"


def _score_candidate(candidate: TopicCandidate, rng: random.Random) -> tuple[float, dict]:
    factors = derive_priority_factors(
        mastery_score=candidate.mastery_score,
        retention_score=candidate.retention_score,
        confidence_score=candidate.confidence_score,
        ap_weight_midpoint_percent=candidate.ap_weight_midpoint_percent,
        topic_timer=candidate.topic_timer,
        rng=rng,
    )
    return score_from_factors(factors), factors


def select_plan_items(
    candidates: list[TopicCandidate],
    point_budget: int,
    rng: random.Random | None = None,
) -> list[SelectedItem]:
    rng = rng or random.Random()
    selected: list[SelectedItem] = []
    remaining = point_budget
    chosen_topic_ids: set[int] = set()

    calibration_candidates = [c for c in candidates if c.calibration_eligible]
    if calibration_candidates and rng.random() < CALIBRATION_CHANCE:
        chosen = rng.choice(calibration_candidates)
        cost = ACTIVITY_COSTS[ITEM_TYPE_TO_ACTIVITY_COST_KEY["calibration"]]
        if cost <= remaining:
            score, factors = _score_candidate(chosen, rng)
            selected.append(
                SelectedItem(
                    topic_id=chosen.topic_id,
                    unit_id=chosen.unit_id,
                    subject_id=chosen.subject_id,
                    item_type="calibration",
                    point_cost=cost,
                    priority_score=score,
                    reason=reason_for_item(factors, "calibration"),
                )
            )
            remaining -= cost
            chosen_topic_ids.add(chosen.topic_id)

    scored = [
        (*_score_candidate(c, rng), c) for c in candidates if c.topic_id not in chosen_topic_ids
    ]
    scored.sort(key=lambda t: t[0], reverse=True)

    for score, factors, candidate in scored:
        if remaining <= 0:
            break
        item_type = determine_item_type(candidate, rng)
        cost = ACTIVITY_COSTS[ITEM_TYPE_TO_ACTIVITY_COST_KEY[item_type]]
        if cost > remaining:
            continue
        selected.append(
            SelectedItem(
                topic_id=candidate.topic_id,
                unit_id=candidate.unit_id,
                subject_id=candidate.subject_id,
                item_type=item_type,
                point_cost=cost,
                priority_score=score,
                reason=reason_for_item(factors, item_type),
            )
        )
        remaining -= cost
        chosen_topic_ids.add(candidate.topic_id)

    return selected


def _build_candidates(db: Session, subject_id: int, user_id: int) -> list[TopicCandidate]:
    rows = db.exec(
        select(Topic, Unit).join(Unit, Topic.unit_id == Unit.id).where(Unit.subject_id == subject_id)
    ).all()
    topic_ids = [topic.id for topic, _ in rows]

    tms_by_topic = {
        tm.topic_id: tm
        for tm in db.exec(
            select(TopicMastery).where(
                TopicMastery.user_id == user_id, TopicMastery.topic_id.in_(topic_ids)
            )
        ).all()
    }

    frq_topic_ids = set(
        db.exec(
            select(Question.topic_id).where(
                Question.topic_id.in_(topic_ids),
                Question.type == "frq",
                Question.is_active == True,  # noqa: E712
            )
        ).all()
    )

    candidates = []
    for topic, unit in rows:
        tm = tms_by_topic.get(topic.id)
        mastery_score = tm.mastery_score if tm else 0.0
        confidence_score = tm.confidence_score if tm else 0.0
        retention_score = tm.retention_score if tm else 1.0
        topic_timer = tm.topic_timer if tm else 100.0  # never-attempted: surface early
        candidates.append(
            TopicCandidate(
                topic_id=topic.id,
                unit_id=unit.id,
                subject_id=subject_id,
                mastery_score=mastery_score,
                confidence_score=confidence_score,
                retention_score=retention_score,
                topic_timer=topic_timer,
                ap_weight_midpoint_percent=(unit.ap_weight_min + unit.ap_weight_max) / 2.0,
                has_frq_questions=topic.id in frq_topic_ids,
                calibration_eligible=confidence_score >= CALIBRATION_CONFIDENCE_THRESHOLD,
            )
        )
    return candidates


def generate_daily_plan(
    db: Session,
    user_id: int,
    subject_id: int,
    plan_date: date,
    rng: random.Random | None = None,
) -> DailyPlan:
    user_subject = db.exec(
        select(UserSubject).where(
            UserSubject.user_id == user_id, UserSubject.subject_id == subject_id
        )
    ).first()
    minutes = user_subject.study_minutes_per_day if user_subject else DEFAULT_STUDY_MINUTES_PER_DAY
    point_budget = _minutes_to_points(minutes)

    candidates = _build_candidates(db, subject_id, user_id)
    selected = select_plan_items(candidates, point_budget, rng)

    plan = DailyPlan(
        user_id=user_id,
        plan_date=plan_date,
        point_budget=point_budget,
        status="pending",
        generated_reason={"subject_id": subject_id, "study_minutes_per_day": minutes},
    )
    db.add(plan)
    db.flush()

    for item in selected:
        db.add(
            DailyPlanItem(
                daily_plan_id=plan.id,
                subject_id=item.subject_id,
                unit_id=item.unit_id,
                topic_id=item.topic_id,
                item_type=item.item_type,
                point_cost=item.point_cost,
                priority_score=item.priority_score,
                reason=item.reason,
                status="pending",
            )
        )

    return plan
