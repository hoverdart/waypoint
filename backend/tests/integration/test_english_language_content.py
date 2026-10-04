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
    assert len(ids) == 141
    subject = db_session.exec(select(Subject).where(Subject.ap_exam_code == 'english-language')).one()
    user = make_user(db_session)
    headers = auth_header(user.auth_provider_id)
    started = client.post('/practice/start', headers=headers, json={'subject_id': subject.id, 'session_type': 'frq', 'question_count': 3}).json()
    assert len(started['questions']) == 3
    assert all(q['scoring_method'] == 'self_review' for q in started['questions'])
    answers = [{'question_id': q['id'], 'free_response_text': 'My argument and evidence.'} for q in started['questions']]
    sid = started['session_id']
    assert client.post(f'/practice/{sid}/submit', headers=headers, json={'answers': answers}).status_code == 200
    results = client.get(f'/practice/{sid}/results', headers=headers).json()
    assert results['graded_count'] == 0 and results['self_review_count'] == 3
    for row in results['breakdown']:
        saved = client.put(f'/practice/{sid}/questions/{row["question_id"]}/self-review', headers=headers, json={'points': [1, 3, 0]})
        assert saved.status_code == 200 and saved.json()['total'] == 4
    assert len(client.get(f'/practice/{sid}/results', headers=headers).json()['breakdown']) == 3


def test_second_form_adds_independent_stimuli_and_valid_curriculum_mappings():
    from scripts.seed_data.questions.english_language.form_b_reading import QUESTIONS as reading
    from scripts.seed_data.questions.english_language.form_b_writing import QUESTIONS as writing
    original_groups = {tag for q in READING + WRITING for tag in q['skill_tags'] if tag.startswith('stimulus:')}
    new_groups = {tag for q in reading + writing for tag in q['skill_tags'] if tag.startswith('stimulus:')}
    assert not original_groups & new_groups
    assert len(new_groups) == 5
    assert len(reading) == 24 and len(writing) == 21
    topics = {(u['name'], t['name']) for u in UNITS for t in u['topics']}
    for q in reading + writing:
        assert (q['unit_name'], q['topic_name']) in topics
        assert len(q['prompt'].split()) > 200
        assert len({e['explanation'] for e in q['explanations']}) == 4
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    assert len({q['prompt'] for q in READING + WRITING + reading + writing}) == 90


def test_second_essay_set_is_distinct_and_uses_valid_six_point_rubrics():
    from scripts.seed_data.questions.english_language.form_a_essays import QUESTIONS as first
    from scripts.seed_data.questions.english_language.form_b_essays import QUESTIONS, SOURCES
    assert not {q['prompt'] for q in first} & {q['prompt'] for q in QUESTIONS}
    assert all(f'Source {letter} —' in SOURCES for letter in 'ABCDEF')
    assert {tag for q in QUESTIONS for tag in q['skill_tags'] if tag.startswith('format:')} == {
        'format:synthesis', 'format:rhetorical-analysis', 'format:argument'}
    for q in QUESTIONS:
        assert len(q['correct_answer'].split()) >= 350
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))


def test_mock_form_skill_category_weights_match_the_published_ranges():
    from scripts.seed_data.questions.english_language import form_a_reading, form_a_writing, form_b_reading, form_b_writing, form_c_reading, form_c_writing
    # Official MCQ category ranges, not fabricated weights for spiraling units.
    ranges = {'1': (11, 14), '2': (11, 14), '3': (13, 16), '4': (11, 14),
              '5': (13, 16), '6': (11, 14), '7': (11, 14), '8': (11, 14)}
    for reading, writing in ((form_a_reading, form_a_writing), (form_b_reading, form_b_writing), (form_c_reading, form_c_writing)):
        questions = reading.QUESTIONS + writing.QUESTIONS
        counts = Counter(tag[len('ap-skill:')] for q in questions for tag in q['skill_tags'] if tag.startswith('ap-skill:'))
        assert len(questions) == 45
        for category, (minimum, maximum) in ranges.items():
            assert minimum <= counts[category] / len(questions) * 100 <= maximum, (category, counts)


def test_candidate_diagnostic_only_uses_mcqs_and_can_build_subject_mastery(client, db_session, monkeypatch):
    from sqlmodel import select
    from app.models.subject import Subject
    from app.models.mastery import SubjectMastery
    from app.models.question import QuestionOption
    from scripts.seed import SUBJECT_MODULES, seed_subject
    from tests.factories import make_user
    from app.services.diagnostic.diagnostic_builder import build_diagnostic_session
    from app.services.diagnostic.diagnostic_scorer import score_diagnostic
    from app.services.practice.types import AnswerSubmission
    monkeypatch.setitem(SUBJECT_MODULES, 'english-language', ('units_topics.english_language', 'questions.english_language_questions'))
    seed_subject(db_session, {'name': 'AP English Language', 'ap_exam_code': 'english-language', 'display_order': 1})
    subject = db_session.exec(select(Subject).where(Subject.ap_exam_code == 'english-language')).one()
    user = make_user(db_session)
    session, questions = build_diagnostic_session(db_session, user.id, subject.id, 60)
    assert len(questions) == 60 and all(q.type == 'mcq' for q in questions)
    answers = [AnswerSubmission(question_id=q.id, selected_option_id=db_session.exec(
        select(QuestionOption.id).where(QuestionOption.question_id == q.id, QuestionOption.is_correct == True)
    ).one()) for q in questions]
    score_diagnostic(db_session, session.id, answers)
    db_session.flush()
    mastery = db_session.get(SubjectMastery, (user.id, subject.id))
    assert mastery.mastery_score > 0 and mastery.confidence_score > 0


def test_third_mcq_form_adds_distinct_passages_and_closes_uncovered_topic():
    from scripts.seed_data.questions.english_language.form_c_reading import QUESTIONS as reading
    from scripts.seed_data.questions.english_language.form_c_writing import QUESTIONS as writing
    from scripts.seed_data.questions.english_language_questions import QUESTIONS
    from scripts.content_audit import audit_bank
    added = reading + writing
    existing = [q for q in QUESTIONS if q not in added]
    assert len(reading) == 24 and len(writing) == 21
    stimuli = Counter(next(t for t in q['skill_tags'] if t.startswith('stimulus:')) for q in added)
    assert sorted(stimuli.values()) == [8, 8, 8, 10, 11]
    assert not set(stimuli) & {t for q in existing for t in q['skill_tags'] if t.startswith('stimulus:')}
    assert len({q['prompt'] for q in QUESTIONS}) == len(QUESTIONS)
    item_keys = [t for q in QUESTIONS for t in q['skill_tags'] if t.startswith('item:')]
    assert len(item_keys) == len(set(item_keys)) == len(QUESTIONS)
    topics = {(u['name'], t['name']) for u in UNITS for t in u['topics']}
    for q in added:
        assert (q['unit_name'], q['topic_name']) in topics
        assert len(q['prompt'].split()) > 300
        assert len({e['explanation'] for e in q['explanations']}) == 4
        validate_question_content(AdminQuestionCreate(subject_id=1, unit_id=1, topic_id=1,
            **{k: v for k, v in q.items() if k not in ('unit_name', 'topic_name')}))
    assert {q['difficulty'] for q in added} == {2, 3, 4}
    assert min(Counter(q['correct_answer'] for q in added).values()) >= 9
    before, after = audit_bank(UNITS, existing), audit_bank(UNITS, QUESTIONS)
    assert before['uncovered_topics'] and not after['uncovered_topics']
    assert after['topics_below_three_questions'] < before['topics_below_three_questions']
    assert after['topics_without_difficulty_variety'] < before['topics_without_difficulty_variety']
    # Breadth alone must not hide the remaining course-depth work.
    assert after['topics_below_three_questions'] > 0
