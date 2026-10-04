"""Verified external resources, not imported questions or mirrored exam files.

Discovered through https://apcentral.collegeboard.org/courses/past-exam-questions
and the linked course archives on 2026-10-04. Refresh editorially: no runtime
fetching of user-supplied URLs, no AP Classroom authentication or secure materials.
"""
from app.schemas.subject import ReleasedExamResource

COURSE_ARCHIVES = {
    'english-language': 'ap-english-language-and-composition',
    'us-history': 'ap-united-states-history',
    'calculus-ab': 'ap-calculus-ab',
    'biology': 'ap-biology',
    'psychology': 'ap-psychology',
    'chemistry': 'ap-chemistry',
    'computer-science-a': 'ap-computer-science-a',
}


def released_resources(code: str) -> list[ReleasedExamResource]:
    slug = COURSE_ARCHIVES.get(code)
    if slug is None:
        return []
    base = 'https://apcentral.collegeboard.org'
    resources = [ReleasedExamResource(
        title='Released questions, scoring guides, and student samples',
        url=f'{base}/courses/{slug}/exam/past-exam-questions', kind='archive',
        checked_on='2026-10-04',
    )]
    if code == 'english-language':
        for number in (1, 2):
            for prefix, kind, title in (('frq', 'questions', 'Questions'), ('sg', 'scoring', 'Scoring guide')):
                resources.append(ReleasedExamResource(
                    title=f'2025 · Set {number} · {title}', year=2025, kind=kind,
                    url=f'{base}/media/pdf/ap25-{prefix}-english-language-set-{number}.pdf',
                    checked_on='2026-10-04',
                ))
    if code == 'us-history':
        # Verified from the official course archive. The 2027 SAQ/LEQ format
        # differs; preserve the released papers as external historical practice.
        for year, number in ((2026, None), (2025, 1), (2025, 2), (2024, 1), (2024, 2)):
            suffix = '' if number is None else f'-set-{number}'
            label = str(year) if number is None else f'{year} · Set {number}'
            for prefix, kind, title in (('frq', 'questions', 'Questions'), ('sg', 'scoring', 'Scoring guide')):
                resources.append(ReleasedExamResource(
                    title=f'{label} · {title} · Pre-2027 format', year=year, kind=kind,
                    url=f'{base}/media/pdf/ap{year % 100}-{prefix}-us-history{suffix}.pdf',
                    checked_on='2026-10-03',
                ))
    return resources
