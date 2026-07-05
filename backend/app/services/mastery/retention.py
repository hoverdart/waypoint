"""Retention = likelihood the student has since forgotten a topic.

Tracked as its own decaying signal, deliberately not folded into the topic
timer. Modeled as a mastery-modulated exponential forgetting curve: weaker
topics decay in about a week, well-mastered topics take ~7-8 weeks to halve.
Recomputed fresh from current mastery and days-since-practice every time
(stateless), since the product spec doesn't call for a smoothed/blended signal.
"""

MIN_HALF_LIFE_DAYS = 7
MAX_HALF_LIFE_BONUS_DAYS = 45


def compute_retention_score(mastery_score: float, days_since_practiced: float) -> float:
    half_life_days = MIN_HALF_LIFE_DAYS + (mastery_score * MAX_HALF_LIFE_BONUS_DAYS)
    return 0.5 ** (days_since_practiced / half_life_days)
