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

from app.core.exceptions import DomainError, NotFoundError
from app.models.user import User
from app.models.mastery import TopicMastery
from app.models.planner import DailyPlan, DailyPlanItem
from app.models.question import Question
from app.models.subject import Subject, Topic, Unit, UserSubject
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
    has_mcq_questions: bool = True
    calibration_eligible: bool = False
    uses_equal_unit_weights: bool = False


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
    if not candidate.has_mcq_questions and candidate.has_frq_questions:
        return "frq"
    if candidate.mastery_score < WEAKNESS_MASTERY_CEILING:
        return "weakness"
    if candidate.mastery_score < REVIEW_MASTERY_CEILING:
        return "review"
    if (
        not candidate.uses_equal_unit_weights
        and candidate.mastery_score >= CHALLENGE_MASTERY_THRESHOLD
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
    score = score_from_factors(factors)
    if candidate.uses_equal_unit_weights:
        # A fallback weight must not become a claim about official frequency.
        factors.pop("ap_unit_weight")
    return score, factors


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
            if candidate.has_mcq_questions and remaining >= ACTIVITY_COSTS["easy_review"]:
                item_type = "review"
                cost = ACTIVITY_COSTS["easy_review"]
            else:
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
        select(Topic, Unit).join(Unit, Topic.unit_id == Unit.id).where(Unit.subject_id == subject_id, Unit.is_active == True)
    ).all()
    topic_ids = [topic.id for topic, _ in rows]
    units = {unit.id: unit for _, unit in rows}
    equal_weights = bool(units) and all(unit.ap_weight_min + unit.ap_weight_max == 0 for unit in units.values())
    fallback_weight = 100.0 / len(units) if equal_weights else 0.0

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
                Question.validation_status == "approved",
            )
        ).all()
    )

    mcq_topic_ids = set(db.exec(
        select(Question.topic_id).where(
            Question.topic_id.in_(topic_ids), Question.type == "mcq",
            Question.is_active == True, Question.validation_status == "approved",  # noqa: E712
        )
    ).all())
    candidates = []
    for topic, unit in rows:
        if topic.id not in mcq_topic_ids and topic.id not in frq_topic_ids:
            continue
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
                ap_weight_midpoint_percent=fallback_weight if equal_weights else (unit.ap_weight_min + unit.ap_weight_max) / 2.0,
                uses_equal_unit_weights=equal_weights,
                has_frq_questions=topic.id in frq_topic_ids,
                has_mcq_questions=topic.id in mcq_topic_ids,
                calibration_eligible=topic.id in mcq_topic_ids and confidence_score >= CALIBRATION_CONFIDENCE_THRESHOLD,
            )
        )
    return candidates


def generate_daily_plan(
    db: Session,
    user_id: int,
    subject_id: int,
    plan_date: date,
    rng: random.Random | None = None,
    study_minutes: int | None = None,
) -> DailyPlan:
    if study_minutes is not None and not 5 <= study_minutes <= 180:
        raise DomainError("Study time must be between 5 and 180 minutes")
    subject = db.get(Subject, subject_id)
    if subject is None or not subject.is_active:
        raise NotFoundError("Subject not found")
    # Serialize generation per student so two concurrent clicks cannot create
    # duplicate plans for the same course and day.
    user = db.exec(select(User).where(User.id == user_id).with_for_update()).first()
    if user is None:
        raise NotFoundError("User not found")
    todays_plans = db.exec(select(DailyPlan).where(
        DailyPlan.user_id == user_id, DailyPlan.plan_date == plan_date,
    ).order_by(DailyPlan.id.desc())).all()
    plan = next((p for p in todays_plans if p.generated_reason.get("subject_id") == subject_id), None)
    if plan is not None and study_minutes is None:
        return plan
    user_subject = db.exec(select(UserSubject).where(
        UserSubject.user_id == user_id, UserSubject.subject_id == subject_id,
    )).first()
    minutes = study_minutes if study_minutes is not None else (
        user_subject.study_minutes_per_day if user_subject else DEFAULT_STUDY_MINUTES_PER_DAY
    )
    requested_budget = _minutes_to_points(minutes)
    existing_items = list(db.exec(select(DailyPlanItem).where(
        DailyPlanItem.daily_plan_id == plan.id
    )).all()) if plan else []
    completed_cost = sum(item.point_cost for item in existing_items if item.status == "completed")
    finished_topics = {item.topic_id for item in existing_items if item.status in ("completed", "skipped")}
    candidates = [c for c in _build_candidates(db, subject_id, user_id) if c.topic_id not in finished_topics]
    selected = select_plan_items(candidates, max(0, requested_budget - completed_cost), rng)
    if plan is None:
        plan = DailyPlan(user_id=user_id, plan_date=plan_date, point_budget=requested_budget)
        db.add(plan)
        db.flush()
    plan.point_budget = max(requested_budget, completed_cost)
    plan.generated_reason = {"subject_id": subject_id, "study_minutes_per_day": minutes}
    selected_by_topic = {item.topic_id: item for item in selected}
    existing_by_topic = {item.topic_id: item for item in existing_items}
    for item in existing_items:
        if item.status == "pending" and item.topic_id not in selected_by_topic:
            # Keep IDs valid for any already-started session; don't delete work.
            item.status = "skipped"
            db.add(item)
    for selection in selected:
        item = existing_by_topic.get(selection.topic_id)
        if item is None:
            item = DailyPlanItem(
                daily_plan_id=plan.id, subject_id=selection.subject_id,
                unit_id=selection.unit_id, topic_id=selection.topic_id,
                item_type=selection.item_type, point_cost=selection.point_cost,
                priority_score=selection.priority_score, reason=selection.reason,
            )
        else:
            item.item_type = selection.item_type
            item.point_cost = selection.point_cost
            item.priority_score = selection.priority_score
            item.reason = selection.reason
        db.add(item)
    db.flush()
    from app.services.planner.plan_status import update_plan_status
    update_plan_status(db, plan)
    return plan
