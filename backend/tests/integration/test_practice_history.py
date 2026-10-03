from sqlmodel import select

from app.models.gamification import XPEvent
from app.models.practice import QuestionAttempt
from app.services.practice.session_service import start_practice_session
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user


def setup_session(db):
    user = make_user(db)
    subject, units = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=1)
    unit, topics = units[0]
    question, options = make_mcq_question(db, subject.id, unit.id, topics[0].id)
    session, _ = start_practice_session(db, user.id, subject.id, question_count=1)
    return user, session, question, options


def test_saved_answers_survive_reload_without_scoring(client, db_session):
    user, session, question, options = setup_session(db_session)
    headers = auth_header(user.auth_provider_id)
    draft = {'answers': [{'question_id': question.id, 'selected_option_id': options['B'].id,
                           'time_seconds': 42}], 'current_index': 0}
    assert client.patch(f'/practice/{session.id}/draft', json=draft, headers=headers).status_code == 204
    detail = client.get(f'/practice/{session.id}', headers=headers).json()
    assert detail['draft_answers'][0]['selected_option_id'] == options['B'].id
    assert detail['draft_answers'][0]['time_seconds'] == 42
    assert not detail['is_completed']
    assert not db_session.exec(select(QuestionAttempt)).all()
    assert not db_session.exec(select(XPEvent)).all()
    history = client.get('/practice', headers=headers).json()
    assert history[0]['answered_count'] == 1
    assert history[0]['completed_at'] is None
    assert history[0]['subject_name'] == 'AP Calculus AB'


def test_history_and_drafts_are_private(client, db_session):
    user, session, question, _ = setup_session(db_session)
    other = make_user(db_session, 'another', 'another@example.com')
    headers = auth_header(other.auth_provider_id)
    assert client.get('/practice', headers=headers).json() == []
    assert client.patch(f'/practice/{session.id}/draft', headers=headers,
                        json={'answers': [], 'current_index': 0}).status_code == 404
    assert client.get('/practice').status_code == 401


def test_draft_rejects_foreign_questions_and_invalid_index(client, db_session):
    user, session, _, _ = setup_session(db_session)
    headers = auth_header(user.auth_provider_id)
    for draft in [{'answers': [{'question_id': 999999}], 'current_index': 0},
                  {'answers': [], 'current_index': 4}]:
        assert client.patch(f'/practice/{session.id}/draft', headers=headers, json=draft).status_code == 400


def test_completed_session_cannot_be_overwritten_by_late_draft(client, db_session):
    user, session, question, options = setup_session(db_session)
    headers = auth_header(user.auth_provider_id)
    answers = [{'question_id': question.id, 'selected_option_id': options['B'].id}]
    assert client.post(f'/practice/{session.id}/submit', headers=headers, json={'answers': answers}).status_code == 200
    assert client.patch(f'/practice/{session.id}/draft', headers=headers,
                        json={'answers': [], 'current_index': 0}).status_code == 409
    history = client.get('/practice', headers=headers).json()
    assert history[0]['completed_at'] is not None
    assert history[0]['score'] == 1


def test_history_pagination_and_bounds(client, db_session):
    user, session, _, _ = setup_session(db_session)
    newer, _ = start_practice_session(db_session, user.id, session.subject_id)
    headers = auth_header(user.auth_provider_id)
    first = client.get('/practice?limit=1', headers=headers).json()
    second = client.get('/practice?limit=1&offset=1', headers=headers).json()
    assert first[0]['session_id'] == newer.id
    assert second[0]['session_id'] == session.id
    assert client.get('/practice?limit=500', headers=headers).status_code == 422
