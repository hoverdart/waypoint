from sqlmodel import select
from app.content.lessons import FOUNDATIONS
from app.models.lesson import LessonCompletion
from tests.conftest import auth_header
from tests.factories import make_subject_with_units_topics, make_user


def setup(db):
    subject, units = make_subject_with_units_topics(db, code="english-language", n_units=2, n_topics_per_unit=1)
    for index, (unit, _) in enumerate(units, start=1):
        unit.display_order = index
        db.add(unit)
    user = make_user(db)
    other = make_user(db, "other", "other@example.com")
    db.commit()
    return subject, units[0][0], units[1][0], auth_header(user.auth_provider_id), auth_header(other.auth_provider_id)


def test_lessons_check_feedback_persistence_and_user_isolation(client, db_session):
    subject, unit, _, headers, other_headers = setup(db_session)
    path = f"/units/{unit.id}/lessons"
    assert client.get(path).status_code == 401
    lessons = client.get(path, headers=headers).json()
    assert len(lessons) == 3
    assert all(not row['completed'] and 'correct' not in row and 'feedback' not in row for row in lessons)
    assert client.get(f"/subjects/{subject.id}").json()['units'][0]['lesson_count'] == 3
    for lesson in FOUNDATIONS:
        check = f"{path}/{lesson.slug}/check"
        assert client.post(check, json={'option': lesson.correct, 'revision': 1}).status_code == 401
        wrong = client.post(check, headers=headers, json={'option': (lesson.correct + 1) % 3, 'revision': 1})
        assert wrong.json() == {'correct': False, 'feedback': lesson.feedback[(lesson.correct + 1) % 3]}
        assert not next(row for row in client.get(path, headers=headers).json() if row['slug'] == lesson.slug)['completed']
        for _ in range(2):
            response = client.post(check, headers=headers, json={'option': lesson.correct, 'revision': 1})
            assert response.json() == {'correct': True, 'feedback': lesson.feedback[lesson.correct]}
    assert all(row['completed'] for row in client.get(path, headers=headers).json())
    assert all(not row['completed'] for row in client.get(path, headers=other_headers).json())
    assert len(db_session.exec(select(LessonCompletion)).all()) == 3


def test_lessons_validate_scope_revision_and_payload(client, db_session):
    subject, unit, unavailable, headers, _ = setup(db_session)
    path = f"/units/{unit.id}/lessons"
    check = f"{path}/{FOUNDATIONS[0].slug}/check"
    assert client.get(f"/units/{unavailable.id}/lessons", headers=headers).json() == []
    assert client.post(f"/units/{unavailable.id}/lessons/{FOUNDATIONS[0].slug}/check", headers=headers, json={'option': 1, 'revision': 1}).status_code == 404
    assert client.post(check, headers=headers, json={'option': 1, 'revision': 2}).status_code == 409
    for payload in ({'option': -1, 'revision': 1}, {'option': 3, 'revision': 1}, {'option': True, 'revision': 1}, {'option': 1, 'revision': 1, 'user_id': 99}):
        assert client.post(check, headers=headers, json=payload).status_code == 422
    assert not db_session.exec(select(LessonCompletion)).all()
    unit.is_active = False
    db_session.add(unit); db_session.commit()
    assert client.get(path, headers=headers).status_code == 404
    assert client.post(check, headers=headers, json={'option': 1, 'revision': 1}).status_code == 404
    unit.is_active = True
    subject.is_active = False
    db_session.add(unit); db_session.add(subject); db_session.commit()
    assert client.get(path, headers=headers).status_code == 404
