from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


def test_get_practice_session_reconstructs_question_set(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="detail-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("detail-user")
    client.post("/auth/sync-user", headers=headers)

    start_resp = client.post(
        "/practice/start",
        json={"subject_id": subject.id, "topic_id": topics[0].id, "question_count": 1},
        headers=headers,
    )
    session_id = start_resp.json()["session_id"]

    get_resp = client.get(f"/practice/{session_id}", headers=headers)
    assert get_resp.status_code == 200
    body = get_resp.json()
    assert body["is_completed"] is False
    assert body["questions"][0]["id"] == question.id


def test_get_practice_session_reflects_completion(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="detail-test-2", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id, correct_label="A")
    db_session.commit()

    headers = auth_header("detail-user-2")
    client.post("/auth/sync-user", headers=headers)

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

    get_resp = client.get(f"/practice/{session_id}", headers=headers)
    assert get_resp.json()["is_completed"] is True


def test_diagnostic_session_is_also_reconstructible(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="detail-test-3", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("detail-user-3")
    client.post("/auth/sync-user", headers=headers)

    start_resp = client.post("/diagnostic/start", json={"subject_id": subject.id}, headers=headers)
    session_id = start_resp.json()["session_id"]

    get_resp = client.get(f"/practice/{session_id}", headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["session_type"] == "diagnostic"
