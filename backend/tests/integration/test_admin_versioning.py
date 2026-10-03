import pytest
from sqlmodel import select
from app.models.question import Question, QuestionOption
from app.schemas.admin import AdminQuestionUpdate
from app.services.admin.question_service import update_question
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from tests.conftest import auth_header
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user
from tests.integration.test_api_admin import _sync_admin


def test_edit_preserves_completed_and_in_progress_sessions(client, db_session, monkeypatch):
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    user = make_user(db_session)
    completed, _ = start_practice_session(db_session, user.id, subject.id)
    submit_practice_session(db_session, completed.id, [AnswerSubmission(question_id=question.id, selected_option_id=options['B'].id)])
    pending, _ = start_practice_session(db_session, user.id, subject.id)
    admin = _sync_admin(client, monkeypatch)
    response = client.patch(f'/admin/questions/{question.id}', headers=admin, json={
        'prompt': 'Revised prompt', 'correct_answer': 'A',
        'options': [{'label': o.label, 'text': f'New {o.label}', 'is_correct': o.label == 'A'} for o in options.values()],
    })
    assert response.status_code == 200
    updated = response.json()
    assert updated['id'] != question.id
    assert updated['version'] == 2 and updated['validation_status'] == 'draft'
    db_session.expire_all()
    assert not db_session.get(Question, question.id).is_active
    assert db_session.get(QuestionOption, options['B'].id).text == 'Option B'
    old_result = client.get(f'/practice/{completed.id}/results', headers=auth_header(user.auth_provider_id)).json()
    assert old_result['breakdown'][0]['prompt'] == 'Sample MCQ prompt'
    assert old_result['breakdown'][0]['correct_answer'] == 'B'
    submit_practice_session(db_session, pending.id, [AnswerSubmission(question_id=question.id, selected_option_id=options['B'].id)])
    assert pending.correct_count == 1
    assert client.patch(f'/admin/questions/{question.id}', headers=admin, json={'prompt': 'Duplicate edit'}).status_code == 409
    assert client.post(f'/admin/questions/{question.id}/status', headers=admin, json={'status': 'approved'}).status_code == 409
    assert client.post(f'/admin/questions/{updated["id"]}/status', headers=admin, json={'status': 'approved'}).status_code == 200
    _, selected = start_practice_session(db_session, user.id, subject.id)
    assert [q.id for q in selected] == [updated['id']]


@pytest.mark.parametrize('patch', [
    {'correct_answer': 'Z'}, {'difficulty': 9}, {'prompt': None},
    {'options': [{'label': 'A', 'text': 'One', 'is_correct': True}]},
    {'explanations': [{'option_label': 'Z', 'explanation': 'Unknown'}]},
])
def test_invalid_edit_is_atomic(client, db_session, monkeypatch, patch):
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    headers = _sync_admin(client, monkeypatch)
    response = client.patch(f'/admin/questions/{question.id}', headers=headers, json=patch)
    assert response.status_code in (400, 422)
    db_session.expire_all()
    assert db_session.get(Question, question.id).is_active
    assert len(db_session.exec(select(Question)).all()) == 1


def test_seed_respects_archived_question(db_session):
    from scripts.seed import upsert_question
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, _ = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    updated = update_question(db_session, question.id, AdminQuestionUpdate(prompt='Edited version'))
    restored = upsert_question(db_session, subject.id, unit.id, topics[0].id, {'prompt': question.prompt})
    assert restored.id == question.id and not restored.is_active
    assert updated.is_active
