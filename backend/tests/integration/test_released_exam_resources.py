from urllib.parse import urlsplit

from app.content.released_exams import COURSE_ARCHIVES, released_resources
from tests.factories import make_subject_with_units_topics


def test_catalog_links_only_to_verified_official_https_sources():
    assert len(COURSE_ARCHIVES) == 7
    for code in COURSE_ARCHIVES:
        resources = released_resources(code)
        assert resources[0].kind == 'archive'
        assert len({r.url for r in resources}) == len(resources)
        for resource in resources:
            url = urlsplit(resource.url)
            assert url.scheme == 'https' and url.netloc == 'apcentral.collegeboard.org'
            assert not url.query and not url.fragment
    assert released_resources('unknown-course') == []


def test_course_detail_returns_questions_and_matching_scoring_links(client, db_session):
    subject, _ = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    subject.ap_exam_code = 'english-language'
    db_session.add(subject)
    db_session.flush()
    response = client.get(f'/subjects/{subject.id}')
    assert response.status_code == 200
    resources = response.json()['released_exam_resources']
    assert len(resources) == 5
    assert [r['kind'] for r in resources] == ['archive', 'questions', 'scoring', 'questions', 'scoring']
    assert all(r['year'] == 2025 for r in resources[1:])
    assert resources[1]['url'].endswith('ap25-frq-english-language-set-1.pdf')
    assert resources[2]['url'].endswith('ap25-sg-english-language-set-1.pdf')
    assert client.get('/subjects/999999').status_code == 404


def test_history_detail_exposes_paired_released_papers_with_format_labels(client, db_session):
    subject, _ = make_subject_with_units_topics(db_session, n_units=1, n_topics_per_unit=1)
    subject.ap_exam_code = 'us-history'
    db_session.add(subject)
    db_session.flush()
    response = client.get(f'/subjects/{subject.id}')
    assert response.status_code == 200
    resources = response.json()['released_exam_resources']
    assert len(resources) == 11
    expected_papers = [
        (2026, 'ap26-frq-us-history.pdf'),
        (2025, 'ap25-frq-us-history-set-1.pdf'),
        (2025, 'ap25-frq-us-history-set-2.pdf'),
        (2024, 'ap24-frq-us-history-set-1.pdf'),
        (2024, 'ap24-frq-us-history-set-2.pdf'),
    ]
    for index, (year, filename) in enumerate(expected_papers):
        questions, scoring = resources[1 + 2 * index:3 + 2 * index]
        assert questions['kind'] == 'questions'
        assert scoring['kind'] == 'scoring'
        assert questions['url'].endswith('/' + filename)
        assert scoring['url'] == questions['url'].replace('-frq-', '-sg-')
        assert questions['year'] == scoring['year'] == year
        assert all('Pre-2027 format' in r['title'] for r in (questions, scoring))
        assert all(r['checked_on'] == '2026-10-03' for r in (questions, scoring))
