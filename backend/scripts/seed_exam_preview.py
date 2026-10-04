"""Seed candidate exam content only into an explicitly allowlisted disposable test DB.

For real-auth browser QA before course activation. Never use a production database.
"""
from sqlalchemy.engine import make_url
from sqlmodel import Session

from app.db.session import engine
from scripts.seed import SUBJECT_MODULES, seed_subject


def main():
    if make_url(engine.url).database not in {'waypoint_test', 'waypoint_migration_test', 'waypoint_exam_test'}:
        raise RuntimeError('Candidate browser seed requires an allowlisted disposable WayPoint test database')
    SUBJECT_MODULES['english-language'] = ('units_topics.english_language', 'questions.english_language_questions')
    with Session(engine) as db:
        seed_subject(db, {'name': 'AP English Language and Composition', 'ap_exam_code': 'english-language',
            'description': 'Original reading, revision, and essay practice. Candidate course for browser verification.', 'display_order': 1})
        db.commit()
    print('Candidate exam content seeded in disposable test database.')


if __name__ == '__main__':
    main()
