"""Deterministic, free, instant scoring for both question types - consistent
with the product's "deterministic explanations/grading are the default"
philosophy. FRQ scoring is explicitly a rough MVP heuristic (rubric-driven
keyword-presence matching against `questions.rubric_json`), not human or AI
grading, since neither is in scope for the hot path.

`rubric_json` shape: {"checklist": [{"point": str, "keywords": [str], "points": int}]}
"""

from sqlmodel import Session

from app.models.question import Question, QuestionOption

# Fraction of a checklist item's keywords that must appear in the response for
# that item's points to be awarded.
KEYWORD_MATCH_THRESHOLD = 0.5

# A response scoring at or above this fraction of the max score is considered
# "correct" for the purposes of the boolean is_correct flag (which mastery
# logic consumes as a hit/miss signal).
FRQ_CORRECT_THRESHOLD = 0.8


def score_mcq_attempt(
    db: Session, question: Question, selected_option_id: int | None
) -> tuple[bool, float, float]:
    if selected_option_id is None:
        return False, 0.0, 1.0
    option = db.get(QuestionOption, selected_option_id)
    is_correct = bool(option and option.is_correct)
    return is_correct, (1.0 if is_correct else 0.0), 1.0


def score_frq_attempt(question: Question, free_response_text: str | None) -> tuple[bool, float, float]:
    rubric = question.rubric_json or {}
    checklist = rubric.get("checklist", [])
    max_score = sum(item.get("points", 0) for item in checklist) or 1.0

    if not free_response_text:
        return False, 0.0, max_score

    text_lower = free_response_text.lower()
    score = 0.0
    for item in checklist:
        keywords = item.get("keywords", [])
        points = item.get("points", 0)
        if not keywords:
            continue
        matches = sum(1 for kw in keywords if kw.lower() in text_lower)
        if matches / len(keywords) >= KEYWORD_MATCH_THRESHOLD:
            score += points

    is_correct = score >= max_score * FRQ_CORRECT_THRESHOLD
    return is_correct, score, max_score
