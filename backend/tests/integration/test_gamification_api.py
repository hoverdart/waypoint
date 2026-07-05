from app.models.gamification import Badge
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


def _sync_user(client, provider_user_id, email=None):
    email = email or f"{provider_user_id}@example.com"
    resp = client.post("/auth/sync-user", headers=auth_header(provider_user_id, email))
    assert resp.status_code == 200
    return resp.json()


def test_practice_results_surface_xp_and_newly_earned_badges(client, db_session):
    db_session.add(Badge(name="First Steps", rule_json={"type": "first_session"}))
    db_session.flush()
    db_session.commit()

    subject, units = make_subject_with_units_topics(
        db_session, name="AP Gamified", code="gamified-test-1", n_units=1, n_topics_per_unit=1
    )
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.commit()

    headers = auth_header("gamified-user")
    _sync_user(client, "gamified-user")

    start_resp = client.post(
        "/practice/start",
        json={"subject_id": subject.id, "topic_id": topics[0].id, "question_count": 1},
        headers=headers,
    )
    session_id = start_resp.json()["session_id"]

    submit_resp = client.post(
        f"/practice/{session_id}/submit",
        json={"answers": [{"question_id": question.id, "selected_option_id": options["A"].id}]},
        headers=headers,
    )
    assert submit_resp.status_code == 200

    results_resp = client.get(f"/practice/{session_id}/results", headers=headers)
    assert results_resp.status_code == 200
    body = results_resp.json()
    assert body["xp_earned"] > 0
    assert [b["name"] for b in body["newly_earned_badges"]] == ["First Steps"]


def test_dashboard_reports_total_xp_streak_and_earned_badges(client, db_session):
    db_session.add(Badge(name="First Steps", rule_json={"type": "first_session"}))
    db_session.flush()
    db_session.commit()

    subject, units = make_subject_with_units_topics(
        db_session, name="AP Dashboard Gamified", code="dash-gamified-1", n_units=1, n_topics_per_unit=1
    )
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.commit()

    headers = auth_header("dash-gamified-user")
    _sync_user(client, "dash-gamified-user")

    start_resp = client.post(
        "/practice/start",
        json={"subject_id": subject.id, "topic_id": topics[0].id, "question_count": 1},
        headers=headers,
    )
    session_id = start_resp.json()["session_id"]
    client.post(
        f"/practice/{session_id}/submit",
        json={"answers": [{"question_id": question.id, "selected_option_id": options["A"].id}]},
        headers=headers,
    )

    dashboard_resp = client.get("/dashboard", headers=headers)
    assert dashboard_resp.status_code == 200
    body = dashboard_resp.json()
    assert body["total_xp"] > 0
    assert body["streak_days"] >= 1
    assert [b["name"] for b in body["earned_badges"]] == ["First Steps"]


def test_get_me_returns_current_user(client):
    _sync_user(client, "me-user")
    resp = client.get("/users/me", headers=auth_header("me-user"))
    assert resp.status_code == 200
    assert resp.json()["auth_provider_id"] == "me-user"
