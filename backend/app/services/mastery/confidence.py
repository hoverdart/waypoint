"""Confidence = how reliable a mastery estimate is, not how good it is.

The exact formula is not specified by the product spec beyond naming the inputs
(attempts count, consistency, question difficulty, hint usage, time taken,
recentness). This module implements a documented, tunable heuristic: a weighted
composite of sub-factors, dominated by attempt volume so a handful of lucky
answers can never look as reliable as a long track record.
"""

import math
import statistics

from app.core.mathutils import clamp

# Baseline expected time-to-answer per difficulty tier, in seconds. Tunable.
EXPECTED_TIME_SECONDS_BY_DIFFICULTY = {1: 30, 2: 45, 3: 60, 4: 90, 5: 120}

# Attempts beyond this count no longer add to confidence.
VOLUME_SATURATION_ATTEMPTS = 20

# Consistency is judged over at most this many of the most recent attempts.
CONSISTENCY_WINDOW = 10


def volume_factor(attempts_count: int) -> float:
    return clamp(attempts_count / VOLUME_SATURATION_ATTEMPTS, 0.0, 1.0)


def consistency_factor(recent_results: list[bool]) -> float:
    """1.0 = perfectly consistent (all correct or all incorrect), 0.0 = maximally
    erratic (50/50 split). Under 2 data points is treated as neutral (0.5)."""
    window = recent_results[-CONSISTENCY_WINDOW:]
    if len(window) < 2:
        return 0.5
    values = [1.0 if r else 0.0 for r in window]
    stdev = statistics.pstdev(values)
    max_possible_stdev = 0.5  # stdev of a 0/1 series maxes out at 0.5 (50/50 split)
    return clamp(1.0 - (stdev / max_possible_stdev), 0.0, 1.0)


def difficulty_factor(avg_difficulty: float) -> float:
    return clamp(avg_difficulty / 5.0, 0.0, 1.0)


def hint_penalty(hints_used_ratio: float) -> float:
    return clamp(1.0 - (0.3 * hints_used_ratio), 0.0, 1.0)


def time_factor(avg_time_seconds: float, expected_time_seconds: float) -> float:
    """Answering at or above the expected time is fully reliable; answering
    much faster than expected is treated as a mild guessing risk and scales
    the factor down toward 0.5 as time-taken approaches zero."""
    if expected_time_seconds <= 0:
        return 1.0
    return clamp(avg_time_seconds / expected_time_seconds, 0.5, 1.0)


def recency_decay(days_since_last_practice: float) -> float:
    return math.exp(-days_since_last_practice / 30)


def compute_confidence_score(
    attempts_count: int,
    recent_results: list[bool],
    avg_difficulty: float,
    hints_used_ratio: float,
    avg_time_seconds: float,
    expected_time_seconds: float,
    days_since_last_practice: float,
) -> float:
    vf = volume_factor(attempts_count)
    composite = (
        0.4
        + 0.2 * consistency_factor(recent_results)
        + 0.15 * difficulty_factor(avg_difficulty)
        + 0.15 * hint_penalty(hints_used_ratio)
        + 0.10 * time_factor(avg_time_seconds, expected_time_seconds)
    )
    return clamp(vf * composite * recency_decay(days_since_last_practice), 0.0, 1.0)
