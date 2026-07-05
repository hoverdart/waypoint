"""The core daily-planner formula (treated as core IP by the product spec):

    priority_score = weakness_factor * retention_factor * ap_unit_weight
                      * confidence_uncertainty * topic_timer * randomization_factor

Implemented literally as a pure function of pre-computed factors, so it's
trivially unit-testable with hand-picked floats. `derive_priority_factors`
turns raw mastery/unit fields into those factors.

Non-obvious invariant: weakness_factor, retention_factor, and
confidence_uncertainty are each `1 - score`, floored at FACTOR_FLOOR rather
than allowed to hit exactly 0. Because the formula is a product, a single
factor of 0 would zero out the whole priority score regardless of the other
factors - which would permanently hide topics with a "perfect" underlying
score on that one dimension (e.g. a never-attempted topic's default
retention_score of 1.0 would otherwise make it entirely unselectable).
"""

import random

from app.core.mathutils import clamp

FACTOR_FLOOR = 0.05

# Width of the randomization band applied per planner generation call - wide
# enough to reshuffle near-ties, narrow enough that a genuinely weak topic
# can't be buried by bad luck.
RANDOMIZATION_MIN = 0.85
RANDOMIZATION_MAX = 1.15

# AP unit weights are stored as percentages (e.g. 12.5 meaning 12.5%).
AP_WEIGHT_PERCENT_SCALE = 100.0


def weakness_factor(mastery_score: float) -> float:
    return max(FACTOR_FLOOR, 1.0 - mastery_score)


def retention_factor(retention_score: float) -> float:
    return max(FACTOR_FLOOR, 1.0 - retention_score)


def confidence_uncertainty(confidence_score: float) -> float:
    return max(FACTOR_FLOOR, 1.0 - confidence_score)


def ap_unit_weight(ap_weight_midpoint_percent: float) -> float:
    return clamp(ap_weight_midpoint_percent / AP_WEIGHT_PERCENT_SCALE, 0.0, 1.0)


def randomization_factor(rng: random.Random | None = None) -> float:
    rng = rng or random
    return rng.uniform(RANDOMIZATION_MIN, RANDOMIZATION_MAX)


def compute_priority_score(
    weakness: float,
    retention: float,
    ap_weight: float,
    confidence_unc: float,
    topic_timer: float,
    randomization: float,
) -> float:
    return weakness * retention * ap_weight * confidence_unc * topic_timer * randomization


def derive_priority_factors(
    mastery_score: float,
    retention_score: float,
    confidence_score: float,
    ap_weight_midpoint_percent: float,
    topic_timer: float,
    rng: random.Random | None = None,
) -> dict[str, float]:
    """Returns every named factor (including the randomization draw actually
    used), so callers can both score a topic and explain which factor drove
    the score, from the same values."""
    return {
        "weakness_factor": weakness_factor(mastery_score),
        "retention_factor": retention_factor(retention_score),
        "ap_unit_weight": ap_unit_weight(ap_weight_midpoint_percent),
        "confidence_uncertainty": confidence_uncertainty(confidence_score),
        "topic_timer": topic_timer,
        "randomization_factor": randomization_factor(rng),
    }


def score_from_factors(factors: dict[str, float]) -> float:
    return compute_priority_score(
        weakness=factors["weakness_factor"],
        retention=factors["retention_factor"],
        ap_weight=factors["ap_unit_weight"],
        confidence_unc=factors["confidence_uncertainty"],
        topic_timer=factors["topic_timer"],
        randomization=factors["randomization_factor"],
    )
