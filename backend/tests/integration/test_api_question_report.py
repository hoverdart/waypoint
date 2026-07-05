from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics


def test_student_can_report_a_question(client, db_session):
    subject, units = make_subject_with_units_topics(db_session, code="report-test-1", n_units=1, n_topics_per_unit=1)
    (unit, topics) = units[0]
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    db_session.commit()

    headers = auth_header("reporter-user")
    client.post("/auth/sync-user", headers=headers)

    resp = client.post(
        f"/questions/{question.id}/report",
        json={"reason": "wrong_answer", "details": "The correct answer should be B, not A."},
        headers=headers,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["question_id"] == question.id
    assert body["status"] == "pending"
