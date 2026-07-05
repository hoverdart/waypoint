"""Scores a completed diagnostic: writes attempts, marks the session complete,
initializes topic mastery for every touched topic via the normal mastery
update path, then gives every OTHER topic in the subject an explicit
neutral-prior row (rather than leaving it absent) so it surfaces appropriately
in the very first daily plan - a condensed diagnostic can't cover every topic.
"""

from datetime import datetime, timezone

from sqlmodel import Session, select

from app.models.mastery import TopicMastery
from app.models.practice import PracticeSession, QuestionAttempt
from app.models.question import Question
from app.models.subject import Topic, Unit
from app.services.mastery.topic_mastery import AttemptSignal
from app.services.practice.mastery_sync import apply_session_attempts_to_mastery
from app.services.practice.scoring import score_frq_attempt, score_mcq_attempt
from app.services.practice.types import AnswerSubmission
from app.services.xp.badge_service import evaluate_and_award_badges
from app.services.xp.xp_service import award_xp

# Topics the diagnostic didn't cover get a neutral prior, not an absent row:
# mastery=0.5 (genuinely unknown, not "bad"), confidence=0.0 (no evidence at
# all), retention=1.0 (nothing to have forgotten yet), and a high starting
# timer so low-confidence topics still surface soon via the planner.
UNTESTED_TOPIC_MASTERY = 0.5
UNTESTED_TOPIC_CONFIDENCE = 0.0
UNTESTED_TOPIC_RETENTION = 1.0
UNTESTED_TOPIC_STARTING_TIMER = 50.0
XP_DIAGNOSTIC_AWARD = 30


def score_diagnostic(
    db: Session,
    session_id: int,
    answers: list[AnswerSubmission],
    now: datetime | None = None,
) -> PracticeSession:
    now = now or datetime.now(timezone.utc)
    session = db.get(PracticeSession, session_id)

    attempts_by_topic: dict[int, list[AttemptSignal]] = {}
    correct_count = 0
    touched_topic_ids: set[int] = set()

    for ans in answers:
        question = db.get(Question, ans.question_id)
        if question.type == "mcq":
            is_correct, score, max_score = score_mcq_attempt(db, question, ans.selected_option_id)
        else:
            is_correct, score, max_score = score_frq_attempt(question, ans.free_response_text)

        db.add(
            QuestionAttempt(
                user_id=session.user_id,
                session_id=session.id,
                question_id=question.id,
                selected_option_id=ans.selected_option_id,
                free_response_text=ans.free_response_text,
                is_correct=is_correct,
                score=score,
                max_score=max_score,
                time_seconds=ans.time_seconds,
                hints_used=ans.hints_used,
                confidence_rating=ans.confidence_rating,
            )
        )
        if is_correct:
            correct_count += 1
        touched_topic_ids.add(question.topic_id)
        attempts_by_topic.setdefault(question.topic_id, []).append(
            AttemptSignal(
                is_correct=is_correct,
                difficulty=question.difficulty,
                hints_used=ans.hints_used,
                time_seconds=ans.time_seconds,
            )
        )

    session.completed_at = now
    session.correct_count = correct_count
    session.score = correct_count / session.total_questions if session.total_questions else 0.0
    db.add(session)
    db.flush()

    apply_session_attempts_to_mastery(db, session.user_id, session.subject_id, attempts_by_topic, now)

    all_topics = db.exec(
        select(Topic).join(Unit, Topic.unit_id == Unit.id).where(Unit.subject_id == session.subject_id)
    ).all()
    for topic in all_topics:
        if topic.id in touched_topic_ids:
            continue
        if db.get(TopicMastery, (session.user_id, topic.id)) is not None:
            continue
        db.add(
            TopicMastery(
                user_id=session.user_id,
                topic_id=topic.id,
                mastery_score=UNTESTED_TOPIC_MASTERY,
                confidence_score=UNTESTED_TOPIC_CONFIDENCE,
                retention_score=UNTESTED_TOPIC_RETENTION,
                topic_timer=UNTESTED_TOPIC_STARTING_TIMER,
            )
        )

    award_xp(
        db, session.user_id, source="diagnostic", amount=XP_DIAGNOSTIC_AWARD, metadata={"session_id": session.id}
    )
    db.flush()

    newly_earned_badges = evaluate_and_award_badges(db, session.user_id, session=session)
    session.session_metadata = {
        **session.session_metadata,
        "xp_earned": XP_DIAGNOSTIC_AWARD,
        "newly_earned_badge_ids": [b.id for b in newly_earned_badges],
    }
    db.add(session)

    return session
