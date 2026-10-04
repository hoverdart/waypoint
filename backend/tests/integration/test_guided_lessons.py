import pytest
from sqlmodel import select
from app.content.lessons import FOUNDATIONS, AUDIENCE_AND_THESIS, PURPOSE_AND_STRUCTURE, COHERENCE_AND_STYLE, SOURCES_AND_REFINEMENT, lessons_for
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
    unavailable.display_order = 7
    db_session.add(unavailable)
    db_session.commit()
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


@pytest.mark.parametrize('unit_order,sequence,skills', [
    (2, AUDIENCE_AND_THESIS, ['1.B', '2.B', '3.A', '4.A', '3.B', '4.B']),
    (4, PURPOSE_AND_STRUCTURE, ['1.A', '2.A', '3.B', '4.B', '5.C', '6.C']),
    (5, COHERENCE_AND_STYLE, ['5.A', '6.A', '5.B', '6.B', '7.A', '8.A']),
    (6, SOURCES_AND_REFINEMENT, ['3.A', '4.A', '3.B', '4.B', '7.A', '8.A']),
])
def test_published_sequences_persist_all_checks(client, db_session, unit_order, sequence, skills):
    subject, first, second, headers, other_headers = setup(db_session)
    second.display_order = unit_order
    db_session.add(second)
    db_session.commit()
    response = client.get(f"/subjects/{subject.id}").json()
    assert [unit['lesson_count'] for unit in response['units']] == [3, 6]
    path = f"/units/{second.id}/lessons"
    lessons = client.get(path, headers=headers).json()
    assert [lesson['skill'] for lesson in lessons] == skills
    assert len({lesson['slug'] for lesson in lessons}) == 6
    for lesson in sequence:
        assert client.post(f"/units/{first.id}/lessons/{lesson.slug}/check", headers=headers,
                           json={'option': lesson.correct, 'revision': lesson.revision}).status_code == 404
        for option in range(3):
            result = client.post(f"{path}/{lesson.slug}/check", headers=headers,
                                 json={'option': option, 'revision': lesson.revision})
            assert result.status_code == 200
            assert result.json() == {'correct': option == lesson.correct, 'feedback': lesson.feedback[option]}
    assert all(lesson['completed'] for lesson in client.get(path, headers=headers).json())
    assert not any(lesson['completed'] for lesson in client.get(path, headers=other_headers).json())
    assert not any(lesson['completed'] for lesson in client.get(f"/units/{first.id}/lessons", headers=headers).json())
    assert lessons_for('biology', 2) == ()
    assert lessons_for('english-language', 7) == ()


def test_published_lesson_skills_match_seeded_unit_topics():
    from scripts.seed_data.units_topics.english_language import UNITS
    for unit in UNITS:
        skills = {tag.removeprefix('ap-skill:') for topic in unit['topics'] for tag in topic['skill_tags']}
        lessons = lessons_for('english-language', unit['display_order'])
        assert all(lesson.skill in skills for lesson in lessons)
        for lesson in lessons:
            assert len(lesson.options) == len(lesson.feedback) == 3
            assert 0 <= lesson.correct < 3
            assert len(set(lesson.options)) == 3
            assert lesson.revision >= 1


def test_unit_three_reasoning_sequence_checks_and_versioned_progress(client, db_session):
    from app.content.lessons import REASONING_AND_DEVELOPMENT
    subject, first, third, headers, other_headers = setup(db_session)
    third.display_order = 3
    db_session.add(third)
    db_session.commit()
    path = f"/units/{third.id}/lessons"
    lessons = client.get(path, headers=headers).json()
    assert [lesson['skill'] for lesson in lessons] == ['3.A', '4.A', '5.A', '6.A', '5.C', '6.C']
    assert client.get(f"/subjects/{subject.id}").json()['units'][1]['lesson_count'] == 6
    for lesson in REASONING_AND_DEVELOPMENT:
        for option in range(3):
            result = client.post(f"{path}/{lesson.slug}/check", headers=headers,
                                 json={'option': option, 'revision': lesson.revision})
            assert result.status_code == 200
            assert result.json() == {'correct': option == lesson.correct, 'feedback': lesson.feedback[option]}
    assert all(lesson['completed'] for lesson in client.get(path, headers=headers).json())
    assert not any(lesson['completed'] for lesson in client.get(path, headers=other_headers).json())
    assert not any(lesson['completed'] for lesson in client.get(f"/units/{first.id}/lessons", headers=headers).json())
    # A historical version must not complete the current lesson revision.
    row = db_session.exec(select(LessonCompletion).where(LessonCompletion.unit_id == third.id)).first()
    row.revision = 0
    db_session.add(row)
    db_session.commit()
    current = client.get(path, headers=headers).json()
    assert sum(lesson['completed'] for lesson in current) == 5
