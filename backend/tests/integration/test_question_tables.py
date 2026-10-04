from copy import deepcopy
import pytest
from pydantic import ValidationError
from app.schemas.stimulus import DataTable
from app.schemas.admin import AdminQuestionUpdate
from app.services.admin.question_service import update_question
from app.services.practice.session_service import start_practice_session, submit_practice_session
from app.services.practice.types import AnswerSubmission
from tests.factories import make_mcq_question, make_subject_with_units_topics, make_user
from tests.conftest import auth_header

TABLE = {'caption': 'Income by year', 'columns': ['Year', 'Income'], 'rows': [['1974', '$11,200']], 'note': 'Nominal dollars'}


@pytest.mark.parametrize('patch', [
    {'rows': [['1974']]}, {'rows': []}, {'rows': [['x', 'y']] * 31},
    {'columns': ['Year', 'Year']}, {'columns': ['Only']},
    {'rows': [['x', 'y' * 201]]}, {'caption': ' '}, {'script': 'alert(1)'},
])
def test_table_rejects_malformed_or_unbounded_evidence(patch):
    with pytest.raises(ValidationError):
        DataTable.model_validate({**TABLE, **patch})


def test_table_survives_question_revision_resume_and_results(client, db_session):
    subject, units = make_subject_with_units_topics(db_session)
    unit, topics = units[0]
    question, options = make_mcq_question(db_session, subject.id, unit.id, topics[0].id)
    question.data_table = deepcopy(TABLE)
    db_session.add(question)
    user = make_user(db_session)
    session, _ = start_practice_session(db_session, user.id, subject.id)
    replacement = update_question(db_session, question.id, AdminQuestionUpdate(data_table={**TABLE, 'caption': 'Revised evidence'}))
    db_session.commit()
    headers = auth_header(user.auth_provider_id)
    resumed = client.get(f'/practice/{session.id}', headers=headers)
    assert resumed.status_code == 200
    assert resumed.json()['questions'][0]['data_table'] == TABLE
    assert 'correct_answer' not in resumed.json()['questions'][0]
    assert replacement.data_table['caption'] == 'Revised evidence'
    submit_practice_session(db_session, session.id, [AnswerSubmission(question_id=question.id, selected_option_id=options['B'].id)])
    db_session.commit()
    assert client.get(f'/practice/{session.id}/results', headers=headers).json()['breakdown'][0]['data_table'] == TABLE
    cleared = update_question(db_session, replacement.id, AdminQuestionUpdate(data_table=None))
    assert cleared.data_table is None


def test_seeded_history_tables_are_idempotent_and_presented(client, db_session):
    from scripts.seed import seed_subject
    from scripts.seed_data.subjects import SUBJECTS
    from app.models.question import Question
    from sqlmodel import select
    source = next(row for row in SUBJECTS if row['ap_exam_code'] == 'us-history')
    seed_subject(db_session, source)
    rows = db_session.exec(select(Question).where(Question.data_table.is_not(None))).all()
    # JSON null can differ from SQL NULL; inspect deserialized values.
    rows = [q for q in rows if q.data_table]
    assert len(rows) == 3
    ids = {q.id for q in rows}
    seed_subject(db_session, source)
    db_session.expire_all()
    assert {q.id for q in db_session.exec(select(Question)).all() if q.data_table} == ids
    for q in rows:
        assert DataTable.model_validate(q.data_table).rows[1] == ['Average annual unemployment rate', '5.6%', '8.5%']
