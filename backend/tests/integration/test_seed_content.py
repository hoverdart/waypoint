import importlib

from sqlmodel import select

from app.models.question import Question, QuestionOption
from scripts.seed import SUBJECT_MODULES, seed_subject
from scripts.seed_data.subjects import SUBJECTS


def test_all_seed_questions_have_consistent_answers_and_curriculum():
    for units_module, questions_module in SUBJECT_MODULES.values():
        units = importlib.import_module(f'scripts.seed_data.{units_module}').UNITS
        questions = importlib.import_module(f'scripts.seed_data.{questions_module}').QUESTIONS
        topics = {(unit['name'], topic['name']) for unit in units for topic in unit['topics']}
        seen = set()
        for question in questions:
            assert (question['unit_name'], question['topic_name']) in topics
            identity = (question['topic_name'], question['prompt'])
            assert identity not in seen
            seen.add(identity)
            assert 1 <= question['difficulty'] <= 5
            if question['type'] == 'mcq':
                options = question['options']
                correct = [option for option in options if option['is_correct']]
                assert len(correct) == 1
                assert correct[0]['label'] == question['correct_answer']
                assert len({option['label'] for option in options}) == len(options)
                assert len({option['text'] for option in options}) == len(options)
                explained = {e['option_label'] for e in question['explanations']}
                assert {option['label'] for option in options} <= explained
            else:
                assert question['rubric_json']['checklist']
                assert question['correct_answer']


def test_calculus_has_practice_for_every_topic():
    from scripts.seed_data.units_topics.calculus_ab import UNITS
    from scripts.seed_data.questions.calculus_ab_questions import QUESTIONS
    covered = {(q['unit_name'], q['topic_name']) for q in QUESTIONS}
    topics = {(u['name'], t['name']) for u in UNITS for t in u['topics']}
    assert topics <= covered
    assert len(QUESTIONS) == 50


def test_expanded_calculus_seed_is_idempotent(db_session):
    subject = next(s for s in SUBJECTS if s['ap_exam_code'] == 'calculus-ab')
    seed_subject(db_session, subject)
    first_questions = {q.id for q in db_session.exec(select(Question)).all()}
    first_options = {o.id for o in db_session.exec(select(QuestionOption)).all()}
    seed_subject(db_session, subject)
    assert {q.id for q in db_session.exec(select(Question)).all()} == first_questions
    assert {o.id for o in db_session.exec(select(QuestionOption)).all()} == first_options
    assert len(first_questions) == 50
