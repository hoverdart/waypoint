from sqlmodel import select
from app.models.user import User
from app.models.ai import AIUsage
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from app.dependencies import get_ai_provider
from app.main import app
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


class FakeAIProvider:
    def explain(self, context):
        return f"fake explanation for {context.action.value}"


def _sync_user(client, provider_user_id):
    client.post("/auth/sync-user", headers=auth_header(provider_user_id))


def _attempt_question(db, provider_id, question, option_id):
    user = db.exec(select(User).where(User.auth_provider_id == provider_id)).one()
    session, _ = start_practice_session(db, user.id, question.subject_id, topic_id=question.topic_id)
    submit_practice_session(db, session.id, [AnswerSubmission(question_id=question.id, selected_option_id=option_id)])
    db.commit()


def test_ai_explain_and_usage_roundtrip(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="ai-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("ai-user")
    _sync_user(client, "ai-user")
    _attempt_question(db_session, "ai-user", question, options["A"].id)
    app.dependency_overrides[get_ai_provider] = lambda: FakeAIProvider()

    resp = client.post(
        "/ai/explain",
        json={"question_id": question.id, "action": "explain_differently", "selected_option_id": options["A"].id},
        headers=headers,
    )
    assert resp.status_code == 200
    assert "fake explanation" in resp.json()["explanation"]
    assert resp.json()["free_used"] == 1

    usage_resp = client.get("/ai/usage", headers=headers)
    assert usage_resp.status_code == 200
    assert usage_resp.json()["free_used"] == 1


def test_ai_explain_returns_429_once_cap_exceeded(client, db_session, monkeypatch):
    subject, units = make_subject_with_units_topics(db_session, code="ai-test-cap-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("ai-cap-user")
    _sync_user(client, "ai-cap-user")
    _attempt_question(db_session, "ai-cap-user", question, options["A"].id)
    app.dependency_overrides[get_ai_provider] = lambda: FakeAIProvider()

    from app.config import get_settings

    monkeypatch.setattr(get_settings(), "ai_free_weekly_cap", 1)

    payload = {"question_id": question.id, "action": "analogy"}
    first = client.post("/ai/explain", json=payload, headers=headers)
    assert first.status_code == 200

    second = client.post("/ai/explain", json=payload, headers=headers)
    assert second.status_code == 429


def test_ai_does_not_expose_unattempted_questions_or_charge_usage(client, db_session):
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    _sync_user(client, "owner")
    _attempt_question(db_session, "owner", question, options["A"].id)
    _sync_user(client, "other")
    response = client.post("/ai/explain", headers=auth_header("other"), json={"question_id": question.id, "action": "analogy"})
    assert response.status_code == 404
    assert list(db_session.exec(select(AIUsage)).all()) == []


def test_ai_rejects_foreign_option_and_sends_full_answer_text(client, db_session):
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    other, foreign_options = make_mcq_question(db_session, subject.id, unit.id, topics[1].id)
    _sync_user(client, "owner")
    _attempt_question(db_session, "owner", question, options["A"].id)
    contexts = []
    class CapturingProvider:
        def explain(self, context):
            contexts.append(context)
            return "Explanation"
    app.dependency_overrides[get_ai_provider] = lambda: CapturingProvider()
    payload = {"question_id": question.id, "action": "why_wrong", "selected_option_id": foreign_options["A"].id}
    assert client.post("/ai/explain", headers=auth_header("owner"), json=payload).status_code == 400
    assert contexts == []
    payload["selected_option_id"] = options["A"].id
    assert client.post("/ai/explain", headers=auth_header("owner"), json=payload).status_code == 200
    assert contexts[0].correct_answer == "B. Option B"
    assert contexts[0].student_answer == "Option A"


def test_ai_bounds_request_text(client):
    _sync_user(client, "bounded")
    response = client.post("/ai/explain", headers=auth_header("bounded"), json={
        "question_id": 1, "action": "analogy", "free_response_text": "x" * 20001,
    })
    assert response.status_code == 422
