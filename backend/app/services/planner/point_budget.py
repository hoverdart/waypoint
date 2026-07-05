"""Converts a study-time preference into a point budget, and prices the
different activity types the daily planner can mix into that budget.

The spec gives four anchor points (10min=25pts, 20min=50pts, 45min=100pts,
60min=140pts) and explicitly leaves the choice between snapping-to-nearest-tier
and interpolating up to the implementer. Interpolation is used here: snapping
creates unfair cliff-edges (44 and 46 minutes would otherwise get identical
budgets), while interpolation stays smooth and is trivially testable at the
anchor points plus any point between/beyond them.
"""

# (minutes, points) anchors from the product spec, sorted ascending by minutes.
MINUTE_POINT_TIERS: list[tuple[float, float]] = [(10, 25), (20, 50), (45, 100), (60, 140)]

# Point cost per daily-plan-item activity type. Engine-tuning constants, not
# user-editable content, so a plain dict is enough for MVP.
ACTIVITY_COSTS: dict[str, int] = {
    "easy_review": 10,
    "normal_topic": 25,
    "hard_frq": 40,
    "timed_mini_exam": 60,
}


def minutes_to_points(minutes: float) -> int:
    tiers = MINUTE_POINT_TIERS

    if minutes <= tiers[0][0]:
        # Below the first anchor: interpolate from the origin (0 minutes, 0
        # points) up to the first tier, rather than a flat floor.
        m1, p1 = tiers[0]
        return round(minutes * (p1 / m1)) if minutes > 0 else 0

    for (m1, p1), (m2, p2) in zip(tiers, tiers[1:]):
        if m1 <= minutes <= m2:
            fraction = (minutes - m1) / (m2 - m1)
            return round(p1 + fraction * (p2 - p1))

    # Beyond the last anchor: extrapolate using the final segment's slope.
    m1, p1 = tiers[-2]
    m2, p2 = tiers[-1]
    slope = (p2 - p1) / (m2 - m1)
    return round(p2 + slope * (minutes - m2))
