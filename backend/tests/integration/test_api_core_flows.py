from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


def _sync_user(client, provider_user_id="u1", email=None):
    email = email or f"{provider_user_id}@example.com"
    resp = client.post("/auth/sync-user", headers=auth_header(provider_user_id, email))
    assert resp.status_code == 200
    return resp.json()


def test_sync_user_creates_and_is_idempotent(client):
    first = _sync_user(client, "clerk_1", "a@example.com")
    second = _sync_user(client, "clerk_1", "a@example.com")
    assert first["id"] == second["id"]
    assert first["email"] == "a@example.com"


def test_unauthenticated_request_returns_401(client):
    resp = client.get("/dashboard")
    assert resp.status_code == 401


def test_authenticated_but_unsynced_user_returns_401(client):
    resp = client.get("/dashboard", headers=auth_header("never-synced"))
    assert resp.status_code == 401


def test_list_subjects_is_public(client, db_session):
    make_subject_with_units_topics(db_session, name="AP Chemistry", code="chem-test-1")
    db_session.commit()
    resp = client.get("/subjects")
    assert resp.status_code == 200
    codes = [s["ap_exam_code"] for s in resp.json()]
    assert "chem-test-1" in codes


def test_get_subject_detail_includes_nested_units_and_topics(client, db_session):
    subject, _ = make_subject_with_units_topics(db_session, name="AP Physics", code="physics-test-1")
    db_session.commit()

    resp = client.get(f"/subjects/{subject.id}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["ap_exam_code"] == "physics-test-1"
    assert len(body["units"]) == 2
    assert len(body["units"][0]["topics"]) == 2


def test_onboarding_creates_user_subjects(client, db_session):
    subject, _ = make_subject_with_units_topics(db_session, name="AP Onboard Test", code="onboard-test-1")
    db_session.commit()
    _sync_user(client, "onboard-user", "ob@example.com")

    resp = client.post(
        "/onboarding",
        json={
            "mode": "gamified",
            "subjects": [
                {
                    "subject_id": subject.id,
                    "target_score": 5,
                    "exam_date": "2027-05-10",
                    "study_minutes_per_day": 45,
                }
            ],
        },
        headers=auth_header("onboard-user", "ob@example.com"),
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["user"]["mode"] == "gamified"
    assert body["user_subjects"][0]["study_minutes_per_day"] == 45


def test_diagnostic_and_daily_plan_and_practice_end_to_end(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, name="AP E2E", code="e2e-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.commit()

    headers = auth_header("e2e-user", "e2e@example.com")
    _sync_user(client, "e2e-user", "e2e@example.com")
    client.post(
        "/onboarding",
        json={"mode": "professional", "subjects": [{"subject_id": subject.id, "study_minutes_per_day": 20}]},
        headers=headers,
    )

    # Diagnostic
    start_resp = client.post("/diagnostic/start", json={"subject_id": subject.id}, headers=headers)
    assert start_resp.status_code == 200
    diag_session_id = start_resp.json()["session_id"]

    submit_resp = client.post(
        f"/diagnostic/{diag_session_id}/submit",
        json={"answers": [{"question_id": question.id, "selected_option_id": options["A"].id, "time_seconds": 30}]},
        headers=headers,
    )
    assert submit_resp.status_code == 200
    assert submit_resp.json()["correct_count"] == 1

    # Mastery reflects the diagnostic
    mastery_resp = client.get(f"/mastery/subject/{subject.id}", headers=headers)
    assert mastery_resp.status_code == 200
    assert mastery_resp.json()["mastery_score"] > 0.0

    # Daily plan generation
    plan_resp = client.post("/daily-plan/generate", json={"subject_id": subject.id}, headers=headers)
    assert plan_resp.status_code == 200
    plan_body = plan_resp.json()
    assert plan_body["point_budget"] == 50  # 20 minutes -> 50 points

    today_resp = client.get("/daily-plan/today", headers=headers)
    assert today_resp.status_code == 200
    assert len(today_resp.json()) >= 1

    if plan_body["items"]:
        item_id = plan_body["items"][0]["id"]
        skip_resp = client.patch(f"/daily-plan/items/{item_id}", json={"status": "skipped"}, headers=headers)
        assert skip_resp.status_code == 200

    # Regular practice session
    practice_start = client.post(
        "/practice/start",
        json={"subject_id": subject.id, "topic_id": topics[0].id, "session_type": "mcq", "question_count": 1},
        headers=headers,
    )
    assert practice_start.status_code == 200
    practice_session_id = practice_start.json()["session_id"]

    practice_submit = client.post(
        f"/practice/{practice_session_id}/submit",
        json={"answers": [{"question_id": question.id, "selected_option_id": options["A"].id}]},
        headers=headers,
    )
    assert practice_submit.status_code == 200

    results_resp = client.get(f"/practice/{practice_session_id}/results", headers=headers)
    assert results_resp.status_code == 200
    assert results_resp.json()["breakdown"][0]["is_correct"] is True


def test_practice_results_not_visible_to_other_user(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, name="AP Isolation", code="isolation-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    owner_headers = auth_header("owner-user")
    other_headers = auth_header("other-user")
    _sync_user(client, "owner-user")
    _sync_user(client, "other-user")

    start_resp = client.post(
        "/practice/start",
        json={"subject_id": subject.id, "topic_id": topics[0].id, "question_count": 1},
        headers=owner_headers,
    )
    session_id = start_resp.json()["session_id"]

    forbidden_resp = client.get(f"/practice/{session_id}/results", headers=other_headers)
    assert forbidden_resp.status_code == 404


def test_update_user_mode(client):
    _sync_user(client, "mode-user")
    resp = client.patch("/users/me", json={"mode": "gamified"}, headers=auth_header("mode-user"))
    assert resp.status_code == 200
    assert resp.json()["mode"] == "gamified"
