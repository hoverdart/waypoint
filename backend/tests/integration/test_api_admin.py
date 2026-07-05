from app.config import get_settings
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


def _sync_admin(client, monkeypatch, provider_user_id="admin-user"):
    monkeypatch.setattr(get_settings(), "admin_user_ids", [provider_user_id])
    client.post("/auth/sync-user", headers=auth_header(provider_user_id))
    return auth_header(provider_user_id)


def test_non_admin_cannot_access_admin_routes(client):
    client.post("/auth/sync-user", headers=auth_header("regular-user"))
    resp = client.get("/admin/questions", headers=auth_header("regular-user"))
    assert resp.status_code == 403


def test_admin_can_list_and_update_question_status(client, db_session, monkeypatch):
    subject, units = make_subject_with_units_topics(db_session, code="admin-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, _ = make_mcq_question(
        db_session, subject.id, unit.id, topics[0].id, validation_status="draft"
    )
    db_session.commit()

    headers = _sync_admin(client, monkeypatch)

    list_resp = client.get(f"/admin/questions?subject_id={subject.id}", headers=headers)
    assert list_resp.status_code == 200
    assert any(q["id"] == question.id for q in list_resp.json())

    detail_resp = client.get(f"/admin/questions/{question.id}", headers=headers)
    assert detail_resp.status_code == 200
    assert len(detail_resp.json()["options"]) == 4

    approve_resp = client.post(
        f"/admin/questions/{question.id}/status", json={"status": "approved"}, headers=headers
    )
    assert approve_resp.status_code == 200
    assert approve_resp.json()["validation_status"] == "approved"


def test_admin_cannot_skip_straight_from_rejected_to_approved(client, db_session, monkeypatch):
    subject, units = make_subject_with_units_topics(db_session, code="admin-test-2", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, validation_status="rejected")
    db_session.commit()

    headers = _sync_admin(client, monkeypatch)

    resp = client.post(f"/admin/questions/{question.id}/status", json={"status": "approved"}, headers=headers)
    assert resp.status_code == 409


def test_admin_create_question(client, db_session, monkeypatch):
    subject, units = make_subject_with_units_topics(db_session, code="admin-test-3", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    db_session.commit()
    headers = _sync_admin(client, monkeypatch)

    resp = client.post(
        "/admin/questions",
        json={
            "subject_id": subject.id,
            "unit_id": unit.id,
            "topic_id": topics[0].id,
            "type": "mcq",
            "difficulty": 2,
            "prompt": "New admin-created question?",
            "correct_answer": "A",
            "options": [
                {"label": "A", "text": "Right", "is_correct": True},
                {"label": "B", "text": "Wrong", "is_correct": False},
            ],
            "explanations": [
                {"option_label": "A", "explanation": "Because A is right."},
                {"option_label": "B", "explanation": "B is a distractor."},
            ],
        },
        headers=headers,
    )
    assert resp.status_code == 200
    assert resp.json()["prompt"] == "New admin-created question?"


def test_admin_units_and_topics_crud(client, db_session, monkeypatch):
    subject, _ = make_subject_with_units_topics(db_session, code="admin-curr-1", n_units=0, n_topics_per_unit=0)
    db_session.commit()
    headers = _sync_admin(client, monkeypatch)

    unit_resp = client.post(
        f"/admin/units?subject_id={subject.id}",
        json={"name": "New Unit", "ap_weight_min": 5.0, "ap_weight_max": 10.0, "display_order": 1},
        headers=headers,
    )
    assert unit_resp.status_code == 200
    unit_id = unit_resp.json()["id"]

    topic_resp = client.post(
        f"/admin/topics?unit_id={unit_id}",
        json={"name": "New Topic", "skill_tags": ["tag1"], "display_order": 1},
        headers=headers,
    )
    assert topic_resp.status_code == 200

    update_resp = client.patch(
        f"/admin/units/{unit_id}", json={"name": "Renamed Unit"}, headers=headers
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Renamed Unit"
