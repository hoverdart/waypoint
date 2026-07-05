from app.dependencies import get_ai_provider
from app.main import app
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


class FakeAIProvider:
    def explain(self, context):
        return f"fake explanation for {context.action.value}"


def _sync_user(client, provider_user_id):
    client.post("/auth/sync-user", headers=auth_header(provider_user_id))


def test_ai_explain_and_usage_roundtrip(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="ai-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("ai-user")
    _sync_user(client, "ai-user")
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
    app.dependency_overrides[get_ai_provider] = lambda: FakeAIProvider()

    from app.config import get_settings

    monkeypatch.setattr(get_settings(), "ai_free_weekly_cap", 1)

    payload = {"question_id": question.id, "action": "analogy"}
    first = client.post("/ai/explain", json=payload, headers=headers)
    assert first.status_code == 200

    second = client.post("/ai/explain", json=payload, headers=headers)
    assert second.status_code == 429
