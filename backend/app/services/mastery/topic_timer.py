"""Topic timer: the spaced-repetition urgency signal.

Grows the longer a topic goes unpracticed, faster for low-mastery topics,
slower for high-mastery ones, with AP unit weight as a secondary multiplier.
Capped so an indefinitely-ignored topic doesn't end up demanding review every
single day. Resets to zero the moment a topic is practiced.
"""

from app.core.mathutils import clamp

# growth_rate ranges from 1.15 (mastery=0, fastest growth) down to 0.65
# (mastery=1, slowest growth) - mastery is the dominant multiplier per spec.
GROWTH_RATE_AT_ZERO_MASTERY = 1.15
GROWTH_RATE_MASTERY_COEFFICIENT = 0.5

# AP unit weight is a secondary multiplier on top of mastery.
AP_WEIGHT_MULTIPLIER_COEFFICIENT = 0.15


def growth_rate(mastery_score: float) -> float:
    return GROWTH_RATE_AT_ZERO_MASTERY - (GROWTH_RATE_MASTERY_COEFFICIENT * mastery_score)


def ap_multiplier(unit_ap_weight_normalized: float) -> float:
    """unit_ap_weight_normalized is expected in [0, 1]."""
    return 1.0 + (AP_WEIGHT_MULTIPLIER_COEFFICIENT * unit_ap_weight_normalized)


def advance_topic_timer_daily(
    current_timer: float,
    mastery_score: float,
    unit_ap_weight_normalized: float,
    timer_max: float,
) -> float:
    grown = (current_timer + 1) * growth_rate(mastery_score) * ap_multiplier(
        unit_ap_weight_normalized
    ) - 1
    return clamp(grown, 0.0, timer_max)


def reset_timer() -> float:
    return 0.0
