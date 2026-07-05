"""Turns the factor that actually drove a topic's priority score into the
plain-English reason shown to the student, using the spec's example phrasings
verbatim. "Dominant" factor = whichever of the four meaningful (non-timer,
non-random) factors is largest, since each is already a normalized 0-1 value.
"""

REASON_BY_FACTOR = {
    "weakness_factor": "Your mastery dropped",
    "retention_factor": "You haven't practiced this recently",
    "ap_unit_weight": "This unit is high-frequency on the AP exam",
    "confidence_uncertainty": "We need more evidence to estimate your mastery",
}

CALIBRATION_REASON = "Quick check to confirm what you already know"

# Only these factors have a user-facing phrasing; topic_timer's urgency is
# already represented by retention_factor's message, and randomization_factor
# is an internal tie-breaker, not something to explain to the student.
REASON_ELIGIBLE_FACTORS = tuple(REASON_BY_FACTOR.keys())


def reason_for_item(factors: dict[str, float], item_type: str) -> str:
    if item_type == "calibration":
        return CALIBRATION_REASON

    eligible = {k: v for k, v in factors.items() if k in REASON_ELIGIBLE_FACTORS}
    dominant_factor = max(eligible, key=eligible.get)
    return REASON_BY_FACTOR[dominant_factor]
