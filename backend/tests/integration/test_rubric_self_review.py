import pytest
from sqlmodel import select

from app.models.mastery import TopicMastery
from app.models.gamification import XPEvent
from app.models.question import Question
from app.services.practice.session_service import start_practice_session
from tests.conftest import auth_header
from tests.factories import make_user, make_subject_with_units_topics, make_mcq_question


def prepare(db, client, *, mixed=False, completed=True):
    user = make_user(db)
    subject, units = make_subject_with_units_topics(db, n_units=1, n_topics_per_unit=2)
    unit, topics = units[0]
    question = Question(subject_id=subject.id, unit_id=unit.id, topic_id=topics[0].id,
        type='frq', difficulty=3, prompt='Defend a position.', correct_answer='An example argument.',
        validation_status='approved', rubric_json={'scoring_method': 'self_review', 'checklist': [
            {'point': 'Thesis', 'points': 1, 'levels': ['No defensible position', 'Defensible position']},
            {'point': 'Evidence', 'points': 4, 'levels': ['None', 'General', 'Specific', 'Connected', 'Consistent']},
            {'point': 'Complexity', 'points': 1, 'levels': ['Absent', 'Sustained']},
        ]})
    db.add(question)
    db.flush()
    answers = [{'question_id': question.id, 'free_response_text': 'My argument with detailed evidence.'}]
    if mixed:
        mcq, options = make_mcq_question(db, subject.id, unit.id, topics[1].id)
        answers.append({'question_id': mcq.id, 'selected_option_id': options['B'].id})
    session, _ = start_practice_session(db, user.id, subject.id, session_type='timed' if mixed else 'frq', question_count=2)
    headers = auth_header(user.auth_provider_id)
    if completed:
        response = client.post(f'/practice/{session.id}/submit', headers=headers, json={'answers': answers})
        assert response.status_code == 200, response.text
    return user, session, question, headers


def test_essay_submission_does_not_fabricate_mastery_or_accuracy(client, db_session):
    _, session, question, headers = prepare(db_session, client)
    result = client.get(f'/practice/{session.id}/results', headers=headers).json()
    assert result['graded_count'] == 0
    assert result['self_review_count'] == 1
    row = result['breakdown'][0]
    assert row['scoring_method'] == 'self_review'
    assert row['self_review'] is None
    assert row['score'] is None and row['is_correct'] is None
    assert row['rubric'][1]['levels'][4] == 'Consistent'
    assert not db_session.exec(select(TopicMastery)).all()
    history = client.get('/practice', headers=headers).json()[0]
    assert history['graded_count'] == 0
    assert history['self_review_count'] == 1
    # Pre-submission detail must never expose model answers or grading rubrics.
    detail = client.get(f'/practice/{session.id}', headers=headers).json()['questions'][0]
    assert 'correct_answer' not in detail and 'rubric_json' not in detail


def test_self_review_is_persistent_editable_and_never_awards_accuracy_xp(client, db_session):
    _, session, question, headers = prepare(db_session, client)
    url = f'/practice/{session.id}/questions/{question.id}/self-review'
    xp_before = [e.amount for e in db_session.exec(select(XPEvent)).all()]
    for points in ([1, 2, 0], [1, 4, 1]):
        response = client.put(url, headers=headers, json={'points': points})
        assert response.status_code == 200, response.text
        assert response.json()['total'] == sum(points)
        row = client.get(f'/practice/{session.id}/results', headers=headers).json()['breakdown'][0]
        assert row['self_review']['points'] == points
    assert [e.amount for e in db_session.exec(select(XPEvent)).all()] == xp_before
    assert not db_session.exec(select(TopicMastery)).all()
    assert session.correct_count == 0


@pytest.mark.parametrize('points,status', [([1, 5, 1], 400), ([-1, 2, 0], 400), ([1, 2], 400), ([True, 2, 0], 422), ([1.5, 2, 0], 422), (['1', 2, 0], 422)])
def test_self_review_rejects_invalid_scores(client, db_session, points, status):
    _, session, question, headers = prepare(db_session, client)
    assert client.put(f'/practice/{session.id}/questions/{question.id}/self-review', headers=headers, json={'points': points}).status_code == status
    assert 'self_reviews' not in session.session_metadata


def test_self_review_requires_owned_completed_response(client, db_session):
    _, session, question, headers = prepare(db_session, client, completed=False)
    url = f'/practice/{session.id}/questions/{question.id}/self-review'
    assert client.put(url, headers=headers, json={'points': [1, 4, 1]}).status_code == 409
    other = make_user(db_session, 'other-reviewer', 'other@example.com')
    assert client.put(url, headers=auth_header(other.auth_provider_id), json={'points': [1, 4, 1]}).status_code == 404
    assert client.put(url, json={'points': [1, 4, 1]}).status_code == 401


def test_mixed_session_accuracy_only_counts_scored_questions(client, db_session):
    _, session, question, headers = prepare(db_session, client, mixed=True)
    result = client.get(f'/practice/{session.id}/results', headers=headers).json()
    assert (result['total_questions'], result['graded_count'], result['correct_count'], result['score']) == (2, 1, 1, 1.0)
    masteries = db_session.exec(select(TopicMastery)).all()
    assert len(masteries) == 1 and masteries[0].topic_id != question.topic_id
    mcq_id = next(q['question_id'] for q in result['breakdown'] if q['type'] == 'mcq')
    assert client.put(f'/practice/{session.id}/questions/{mcq_id}/self-review', headers=headers, json={'points': [1]}).status_code == 400
    assert client.put(f'/practice/{session.id}/questions/999999/self-review', headers=headers, json={'points': [1]}).status_code == 404


@pytest.mark.parametrize('levels,valid', [(['No claim', 'Defensible claim'], True), ([], False), (['Only one'], False), (['', 'Claim'], False)])
def test_admin_requires_score_level_descriptions_for_self_review(levels, valid):
    from app.core.exceptions import DomainError
    from app.schemas.admin import AdminQuestionCreate
    from app.services.admin.question_validation import validate_question_content
    question = AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1, type='frq', difficulty=3,
        prompt='Defend a claim', correct_answer='Model argument', rubric_json={
            'scoring_method': 'self_review', 'checklist': [{'point': 'Thesis', 'points': 1, 'levels': levels}]
        })
    if valid:
        validate_question_content(question)
    else:
        with pytest.raises(DomainError):
            validate_question_content(question)


def test_self_review_essays_do_not_enter_automatically_scored_diagnostics(client, db_session):
    from app.core.exceptions import DomainError
    from app.services.diagnostic.diagnostic_builder import build_diagnostic_session
    user, session, _, _ = prepare(db_session, client, completed=False)
    with pytest.raises(DomainError, match='No approved questions'):
        build_diagnostic_session(db_session, user.id, session.subject_id, 10)
