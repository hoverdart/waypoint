import pytest
from sqlmodel import select
from app.models.subject import UserSubject
from tests.factories import make_subject_with_units_topics
from tests.conftest import auth_header


def test_preferences_update_remove_restore_and_isolate_users(client, db_session):
    subject, _ = make_subject_with_units_topics(db_session)
    headers = auth_header("preferences-owner")
    other = auth_header("preferences-other")
    client.post("/auth/sync-user", headers=headers)
    client.post("/auth/sync-user", headers=other)
    payload = {"subjects": [{"subject_id": subject.id, "target_score": 5, "exam_date": "2027-05-10", "study_minutes_per_day": 35}]}
    response = client.patch("/users/me/subjects", json=payload, headers=headers)
    assert response.status_code == 200
    row_id = response.json()[0]["id"]
    plan_response = client.post("/daily-plan/generate", headers=headers, json={"subject_id": subject.id})
    assert plan_response.status_code == 200
    assert client.get("/users/me/subjects", headers=headers).json()[0]["study_minutes_per_day"] == 35
    assert client.get("/users/me/subjects", headers=other).json() == []
    assert client.patch("/users/me/subjects", json={"subjects": []}, headers=headers).status_code == 200
    assert client.get("/users/me/subjects", headers=headers).json() == []
    db_session.expire_all()
    assert db_session.get(UserSubject, row_id).is_active is False
    assert client.get("/daily-plan/today", headers=headers).json() == []
    assert client.get("/dashboard", headers=headers).json()["today_plan"] is None
    response = client.patch("/users/me/subjects", json=payload, headers=headers)
    assert response.json()[0]["id"] == row_id
    assert len(client.get("/daily-plan/today", headers=headers).json()) == 1
    assert len(db_session.exec(select(UserSubject)).all()) == 1


@pytest.mark.parametrize("field,value", [("target_score", 6), ("target_score", 0), ("study_minutes_per_day", 0), ("study_minutes_per_day", 181)])
def test_preference_bounds(client, field, value):
    headers = auth_header("bounds")
    client.post("/auth/sync-user", headers=headers)
    response = client.patch("/users/me/subjects", headers=headers, json={"subjects": [{"subject_id": 1, field: value}]})
    assert response.status_code == 422


def test_invalid_and_duplicate_courses_are_rejected(client, db_session):
    headers = auth_header("invalid-courses")
    client.post("/auth/sync-user", headers=headers)
    response = client.patch("/users/me/subjects", headers=headers, json={"subjects": [{"subject_id": 999999}]})
    assert response.status_code == 400
    assert list(db_session.exec(select(UserSubject)).all()) == []
    response = client.post("/onboarding", headers=headers, json={"subjects": [{"subject_id": 1}, {"subject_id": 1}]})
    assert response.status_code == 422


@pytest.mark.parametrize("mode", ["admin", None])
def test_user_mode_validation(client, mode):
    headers = auth_header("mode-user")
    client.post("/auth/sync-user", headers=headers)
    assert client.patch("/users/me", headers=headers, json={"mode": mode}).status_code == 422
    assert client.patch("/users/me", headers=headers, json={"display_name": "Ada"}).status_code == 200
