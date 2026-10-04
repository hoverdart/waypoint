"""Checked exam formats; item keys refer to original WayPoint content.

English Language: official exam page checked 2026-10-03. Section II includes
its 15-minute reading period within the 135-minute allowance. Practice allows
an untimed break between sections, explicitly distinct from an official sitting.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class SectionBlueprint:
    title: str
    seconds: int
    weight: float
    item_keys: tuple[str, ...]
    instructions: str


@dataclass(frozen=True)
class ExamBlueprint:
    form_id: str
    title: str
    subject_code: str
    source_url: str
    sections: tuple[SectionBlueprint, ...]


def language_form(letter: str, groups: tuple[str, ...]) -> ExamBlueprint:
    prefix = f'lang-{letter}'
    mcq = tuple(f'{prefix}-{group}-{number:02d}' for group, size in zip(groups, (8, 8, 8, 10, 11)) for number in range(1, size + 1))
    essays = tuple(f'{prefix}-{kind}' for kind in ('synthesis', 'rhetorical-analysis', 'argument'))
    return ExamBlueprint(f'english-language-{letter}', f'English Language · Form {letter.upper()}',
        'english-language', 'https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam', (
            SectionBlueprint('Multiple choice', 3600, 0.45, mcq,
                '45 questions across five passages. You may revisit questions within this section. Unanswered questions receive no credit. Closing the section locks its answers.'),
            SectionBlueprint('Free response', 8100, 0.55, essays,
                'Three essays: synthesis, rhetorical analysis, and argument. The 135 minutes include 15 minutes for reading. Plan about 40 minutes per essay. Essays use rubric self-review after the entire exam is submitted.'),
        ))


BLUEPRINTS = {
    form.form_id: form for form in (
        language_form('a', ('repair', 'forecast', 'translation', 'garden', 'archive')),
        language_form('b', ('museum', 'clock', 'birds', 'recipe', 'sleep')),
    )
}
