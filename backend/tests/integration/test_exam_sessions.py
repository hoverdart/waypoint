from datetime import datetime, timedelta, timezone

import pytest
from sqlmodel import select

from app.models.gamification import XPEvent
from app.models.practice import PracticeSession, QuestionAttempt
from app.models.question import Question, QuestionOption
from app.models.subject import Subject
from app.services.exams import session_service as service
from scripts.seed import SUBJECT_MODULES, seed_subject
from tests.conftest import auth_header
from tests.factories import make_user


@pytest.fixture
def exam_setup(db_session, monkeypatch):
    monkeypatch.setitem(SUBJECT_MODULES, 'english-language', ('units_topics.english_language', 'questions.english_language_questions'))
    seed_subject(db_session, {'name': 'AP English Language', 'ap_exam_code': 'english-language', 'display_order': 1})
    subject = db_session.exec(select(Subject).where(Subject.ap_exam_code == 'english-language')).one()
    user = make_user(db_session)
    current = [datetime(2026, 10, 3, 12, tzinfo=timezone.utc)]
    monkeypatch.setattr(service, 'utc_now', lambda: current[0])
    return subject, user, auth_header(user.auth_provider_id), current


def start(client, setup, **changes):
    subject, _, headers, _ = setup
    response = client.post('/exams/start', headers=headers, json={
        'subject_id': subject.id, 'form_id': 'english-language-a', **changes})
    assert response.status_code == 200, response.text
    return response.json()


def save(client, exam, headers, answers, revision=0):
    return client.put(f'/exams/{exam["session_id"]}/sections/{exam["current_section"]}/draft', headers=headers,
        json={'answers': answers, 'current_index': 0, 'expected_revision': revision})


def test_catalog_and_exam_resolve_full_ordered_form_without_answer_leaks(client, exam_setup):
    subject, _, headers, _ = exam_setup
    catalog = client.get(f'/exams/subjects/{subject.id}', headers=headers).json()
    assert len(catalog) == 2 and all(form['available'] for form in catalog)
    assert [s['question_count'] for s in catalog[0]['sections']] == [45, 3]
    assert [s['duration_seconds'] for s in catalog[0]['sections']] == [3600, 8100]
    assert [s['score_weight'] for s in catalog[0]['sections']] == [.45, .55]
    exam = start(client, exam_setup)
    assert len(exam['questions']) == 45
    assert all(q['type'] == 'mcq' for q in exam['questions'])
    assert all('correct_answer' not in q and 'rubric_json' not in q for q in exam['questions'])
    assert exam['sections'][1]['status'] == 'ready' and exam['sections'][1]['deadline'] is None
    assert exam['answers'] == [] and exam['revision'] == 0


def test_exam_drafts_survive_reload_and_reject_stale_overwrites(client, exam_setup):
    _, _, headers, _ = exam_setup
    exam = start(client, exam_setup)
    q = exam['questions'][0]
    answers = [{'question_id': q['id'], 'selected_option_id': q['options'][0]['id']}]
    saved = save(client, exam, headers, answers)
    assert saved.status_code == 200, saved.text
    assert saved.json()['revision'] == 1
    history = client.get('/practice', headers=headers).json()[0]
    assert history['is_exam'] and history['answered_count'] == 1
    restored = client.get(f'/exams/{exam["session_id"]}', headers=headers).json()
    assert restored['answers'][0]['selected_option_id'] == q['options'][0]['id']
    assert save(client, exam, headers, [], revision=0).status_code == 409
    assert save(client, exam, headers, [], revision=1).status_code == 200


def test_expiration_uses_server_clock_and_does_not_accept_late_answers(client, exam_setup):
    _, _, headers, clock = exam_setup
    exam = start(client, exam_setup)
    sid = exam['session_id']
    q = exam['questions'][0]
    assert save(client, exam, headers, [{'question_id': q['id'], 'selected_option_id': q['options'][0]['id']}]).status_code == 200
    clock[0] += timedelta(hours=1)
    assert save(client, exam, headers, [], revision=1).status_code == 409
    expired = client.get(f'/exams/{sid}', headers=headers).json()
    assert expired['sections'][0]['status'] == 'expired' and expired['questions'] == []
    finished = client.post(f'/exams/{sid}/sections/0/finish', headers=headers)
    assert finished.status_code == 200 and finished.json()['current_section'] == 1
    assert finished.json()['questions'] == []
    clock[0] += timedelta(hours=2)
    opened = client.post(f'/exams/{sid}/sections/1/start', headers=headers).json()
    assert len(opened['questions']) == 3
    assert datetime.fromisoformat(opened['sections'][1]['deadline'].replace('Z', '+00:00')) == clock[0] + timedelta(minutes=135)
    assert client.post(f'/exams/{sid}/sections/1/start', headers=headers).status_code == 409
    assert client.post(f'/exams/{sid}/sections/0/finish', headers=headers).status_code == 409


def test_completion_scores_saved_work_once_and_keeps_essays_self_reviewed(client, db_session, exam_setup):
    _, _, headers, _ = exam_setup
    exam = start(client, exam_setup)
    sid = exam['session_id']
    q = exam['questions'][0]
    correct = db_session.exec(select(QuestionOption).where(QuestionOption.question_id == q['id'], QuestionOption.is_correct == True)).one()
    assert save(client, exam, headers, [{'question_id': q['id'], 'selected_option_id': correct.id}]).status_code == 200
    assert client.post(f'/exams/{sid}/sections/0/finish', headers=headers).status_code == 200
    assert not db_session.exec(select(QuestionAttempt)).all()
    assert not db_session.exec(select(XPEvent)).all()
    opened = client.post(f'/exams/{sid}/sections/1/start', headers=headers).json()
    answer = [{'question_id': opened['questions'][0]['id'], 'free_response_text': 'My thesis and evidence.'}]
    assert save(client, opened, headers, answer).status_code == 200
    finished = client.post(f'/exams/{sid}/sections/1/finish', headers=headers)
    assert finished.status_code == 200 and finished.json()['completed']
    detail = client.get(f'/practice/{sid}', headers=headers)
    assert detail.status_code == 200 and detail.json()['is_completed']
    assert finished.json()['questions'] == []
    results = client.get(f'/practice/{sid}/results', headers=headers).json()
    assert results['total_questions'] == 48 and results['correct_count'] == 1
    assert results['graded_count'] == 45 and results['score'] == pytest.approx(1 / 45)
    assert results['self_review_count'] == 3
    assert len(db_session.exec(select(QuestionAttempt)).all()) == 48
    assert len(db_session.exec(select(XPEvent)).all()) == 1
    assert client.post(f'/exams/{sid}/sections/1/finish', headers=headers).status_code == 409
    assert len(db_session.exec(select(XPEvent)).all()) == 1
    assert save(client, opened, headers, answer, revision=1).status_code == 409


def test_generic_practice_routes_cannot_bypass_exam_sections(client, db_session, exam_setup):
    _, _, headers, _ = exam_setup
    exam = start(client, exam_setup)
    sid = exam['session_id']
    session = db_session.get(PracticeSession, sid)
    all_answers = [{'question_id': qid} for qid in session.session_metadata['question_ids']]
    assert client.get(f'/practice/{sid}', headers=headers).status_code == 409
    assert client.post(f'/practice/{sid}/submit', headers=headers, json={'answers': all_answers}).status_code == 409
    assert client.patch(f'/practice/{sid}/draft', headers=headers, json={'answers': all_answers, 'current_index': 0}).status_code == 409
    assert client.get(f'/practice/{sid}/results', headers=headers).status_code == 409
    assert client.post(f'/exams/{sid}/sections/1/start', headers=headers).status_code == 409
    assert not db_session.exec(select(QuestionAttempt)).all()


def test_exam_rejects_foreign_future_duplicate_and_wrong_option_answers(client, db_session, exam_setup):
    _, _, headers, _ = exam_setup
    exam = start(client, exam_setup)
    session = db_session.get(PracticeSession, exam['session_id'])
    future_id = session.session_metadata['exam']['sections'][1]['question_ids'][0]
    q, other = exam['questions'][:2]
    for answers in ([{'question_id': future_id}], [{'question_id': 999999}],
                    [{'question_id': q['id']}, {'question_id': q['id']}],
                    [{'question_id': q['id'], 'selected_option_id': other['options'][0]['id']}]):
        assert save(client, exam, headers, answers).status_code == 400
    assert client.put(f'/exams/{exam["session_id"]}/sections/0/draft', headers=headers,
        json={'answers': [], 'current_index': 45, 'expected_revision': 0}).status_code == 400


def test_exam_is_private_at_every_transition(client, db_session, exam_setup):
    exam = start(client, exam_setup)
    other = make_user(db_session, 'exam-other', 'other@example.com')
    headers = auth_header(other.auth_provider_id)
    sid = exam['session_id']
    assert client.get(f'/exams/{sid}', headers=headers).status_code == 404
    for suffix in ('start', 'finish'):
        assert client.post(f'/exams/{sid}/sections/0/{suffix}', headers=headers).status_code == 404
    assert save(client, exam, headers, []).status_code == 404
    assert client.get(f'/exams/{sid}').status_code == 401


def test_incomplete_or_ambiguous_bank_cannot_silently_shorten_a_mock(client, db_session, exam_setup):
    subject, _, headers, _ = exam_setup
    question = next(q for q in db_session.exec(select(Question)).all() if 'item:lang-a-repair-01' in q.skill_tags)
    question.is_active = False
    db_session.add(question)
    db_session.flush()
    catalog = client.get(f'/exams/subjects/{subject.id}', headers=headers).json()
    assert not catalog[0]['available'] and catalog[1]['available']
    payload = {'subject_id': subject.id, 'form_id': 'english-language-a'}
    assert client.post('/exams/start', headers=headers, json=payload).status_code == 409
    assert not db_session.exec(select(PracticeSession)).all()
    question.is_active = True
    db_session.add(question)
    db_session.add(Question(**question.model_dump(exclude={'id', 'created_at', 'updated_at'})))
    db_session.flush()
    assert client.post('/exams/start', headers=headers, json=payload).status_code == 409


def test_extended_practice_time_is_bounded_and_fixed_at_start(client, exam_setup):
    subject, _, headers, clock = exam_setup
    exam = start(client, exam_setup, time_multiplier=1.5)
    assert exam['sections'][0]['duration_seconds'] == 5400
    assert exam['sections'][1]['duration_seconds'] == 12150
    assert datetime.fromisoformat(exam['sections'][0]['deadline'].replace('Z', '+00:00')) == clock[0] + timedelta(seconds=5400)
    for multiplier in (0, 1.1, 10):
        assert client.post('/exams/start', headers=headers, json={'subject_id': subject.id, 'form_id': 'english-language-a', 'time_multiplier': multiplier}).status_code == 422
