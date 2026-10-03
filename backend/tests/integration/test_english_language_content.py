from collections import Counter

from app.schemas.admin import AdminQuestionCreate
from app.services.admin.question_validation import validate_question_content
from scripts.seed_data.questions.english_language.form_a_reading import QUESTIONS as READING
from scripts.seed_data.questions.english_language.form_a_writing import QUESTIONS as WRITING
from scripts.seed_data.units_topics.english_language import UNITS, SKILLS


def test_first_english_language_form_has_real_passage_sets_and_individual_rationales():
    questions = READING + WRITING
    assert len(READING) == 24 and len(WRITING) == 21
    groups = Counter(next(tag for tag in q['skill_tags'] if tag.startswith('stimulus:')) for q in questions)
    assert sorted(groups.values()) == [8, 8, 8, 10, 11]
    assert len({q['prompt'] for q in questions}) == 45
    topics = {(u['name'], t['name']) for u in UNITS for t in u['topics']}
    keys = Counter()
    for question in questions:
        assert (question['unit_name'], question['topic_name']) in topics
        assert len(question['prompt'].split()) > 200
        assert len({e['explanation'] for e in question['explanations']}) == 4
        assert question['source'] == 'generated'
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in question.items() if k not in ('unit_name', 'topic_name')}))
        keys[question['correct_answer']] += 1
    assert set(keys) == set('ABCD') and min(keys.values()) >= 9
    assert {q['difficulty'] for q in questions} == {2, 3, 4}


def test_first_form_covers_all_framework_skill_categories_without_fake_unit_weights():
    questions = READING + WRITING
    skills = {tag.removeprefix('ap-skill:') for q in questions for tag in q['skill_tags'] if tag.startswith('ap-skill:')}
    assert skills == set(SKILLS)
    assert len(UNITS) == 9
    assert all(u['ap_weight_min'] == u['ap_weight_max'] == 0 for u in UNITS)


def test_coverage_report_exposes_missing_depth_instead_of_equating_counts_with_completion():
    from scripts.content_audit import audit_bank, report
    coverage = audit_bank(UNITS, READING + WRITING)
    assert coverage['questions'] == 45
    assert coverage['independent_stimuli'] == 5
    assert coverage['topics_below_three_questions'] > 0
    assert coverage['topics_without_difficulty_variety'] > 0
    courses = report()
    assert len(courses) == 43
    assert courses[0]['status'] == 'in_development'
    assert any(c['status'] == 'not_started' for c in courses)


def test_essay_set_has_all_response_types_and_reviewable_rubrics():
    from scripts.seed_data.questions.english_language.form_a_essays import QUESTIONS, SYNTHESIS_SOURCES
    assert len(QUESTIONS) == 3
    assert {tag for q in QUESTIONS for tag in q['skill_tags'] if tag.startswith('format:')} == {
        'format:synthesis', 'format:rhetorical-analysis', 'format:argument'}
    assert all(f'Source {letter} —' in SYNTHESIS_SOURCES for letter in 'ABCDEF')
    for q in QUESTIONS:
        assert len(q['correct_answer'].split()) >= 350
        assert q['rubric_json']['scoring_method'] == 'self_review'
        assert sum(row['points'] for row in q['rubric_json']['checklist']) == 6
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_candidate_course_seeds_idempotently_and_supports_essay_review(client, db_session, monkeypatch):
    from sqlmodel import select
    from app.models.question import Question, QuestionOption
    from app.models.subject import Subject
    from scripts.seed import SUBJECT_MODULES, seed_subject
    from tests.factories import make_user
    from tests.conftest import auth_header
    monkeypatch.setitem(SUBJECT_MODULES, 'english-language', ('units_topics.english_language', 'questions.english_language_questions'))
    subject_data = {'name': 'AP English Language and Composition', 'ap_exam_code': 'english-language',
        'description': 'Candidate course under test', 'display_order': 1}
    seed_subject(db_session, subject_data)
    ids = {q.id for q in db_session.exec(select(Question)).all()}
    option_ids = {q.id for q in db_session.exec(select(QuestionOption)).all()}
    seed_subject(db_session, subject_data)
    assert {q.id for q in db_session.exec(select(Question)).all()} == ids
    assert {q.id for q in db_session.exec(select(QuestionOption)).all()} == option_ids
    assert len(ids) == 48
    subject = db_session.exec(select(Subject).where(Subject.ap_exam_code == 'english-language')).one()
    user = make_user(db_session)
    headers = auth_header(user.auth_provider_id)
    started = client.post('/practice/start', headers=headers, json={'subject_id': subject.id, 'session_type': 'frq', 'question_count': 3}).json()
    assert len(started['questions']) == 3
    answers = [{'question_id': q['id'], 'free_response_text': 'My argument and evidence.'} for q in started['questions']]
    sid = started['session_id']
    assert client.post(f'/practice/{sid}/submit', headers=headers, json={'answers': answers}).status_code == 200
    results = client.get(f'/practice/{sid}/results', headers=headers).json()
    assert results['graded_count'] == 0 and results['self_review_count'] == 3
    for row in results['breakdown']:
        saved = client.put(f'/practice/{sid}/questions/{row["question_id"]}/self-review', headers=headers, json={'points': [1, 3, 0]})
        assert saved.status_code == 200 and saved.json()['total'] == 4
    assert len(client.get(f'/practice/{sid}/results', headers=headers).json()['breakdown']) == 3
