"""Original comparative questions on three distinct constitutional protections."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Comparison in Period 5', code='5.12', set_id='reconstruction-amendments',
    source_url='https://www.archives.gov/founding-docs/amendments-11-27',
    source_kind='original instructional summary',
    stimulus='The Thirteenth Amendment (1865) prohibited slavery and involuntary servitude, except as punishment for crime after conviction. The Fourteenth (1868) defined citizenship and constrained state actions through due process and equal protection. The Fifteenth (1870) prohibited the United States and states from denying or abridging citizens’ voting rights on account of race, color, or previous condition of servitude. Each granted Congress enforcement power. This is an original instructional summary of selected provisions.',
    items=[
        ('comparison', 2, 'Which comparison best distinguishes the amendments’ central protections?', 1, [
            ('The Thirteenth defined citizenship, while the Fourteenth ended slavery.', 'This reverses the central provisions of the two amendments.'),
            ('The Thirteenth addressed bondage, the Fourteenth citizenship and legal protection, and the Fifteenth specified prohibited grounds for voting discrimination.', 'This distinguishes the protections without treating emancipation, citizenship, and voting as interchangeable.'),
            ('The Fifteenth granted citizenship, while the Fourteenth applied only to labor contracts.', 'Citizenship is addressed in the Fourteenth, whose protections are not confined to labor contracts.'),
            ('All three established the same voting qualifications using different language.', 'The amendments addressed different dimensions of freedom and rights rather than identical voter qualifications.'),
        ]),
        ('claims-evidence', 3, 'Which conclusion exceeds what the Fifteenth Amendment’s listed grounds establish?', 3, [
            ('Racial discrimination in voting was made a constitutional issue.', 'Race is explicitly included among the prohibited grounds.'),
            ('Both federal and state governments were subject to the voting-rights restriction.', 'The summary identifies both the United States and the states.'),
            ('Previous enslavement could not lawfully be used as the specified basis for denying voting rights.', 'Previous condition of servitude is explicitly among the prohibited grounds.'),
            ('Every adult citizen received an unconditional right to vote regardless of sex or any other qualification.', 'The amendment specified prohibited grounds; it did not establish universal adult suffrage or prohibit sex discrimination in voting.'),
        ]),
        ('argumentation', 4, 'What does the inclusion of congressional enforcement powers most strongly support?', 0, [
            ('The amendments provided authority for legislation implementing their protections, rather than relying solely on declarations.', 'Enforcement clauses supplied a constitutional basis for congressional action, though effective implementation still depended on political and institutional choices.'),
            ('State compliance was automatic and required no further institutional action.', 'An enforcement power does not prove automatic compliance.'),
            ('Congress could exercise these powers only after each state separately approved every enforcement law.', 'The clauses grant congressional authority rather than a state-by-state veto over its exercise.'),
            ('The amendments were temporary wartime directives that expired when military operations ended.', 'Constitutional amendments and their enforcement powers were not temporary military orders.'),
        ]),
    ],
)
