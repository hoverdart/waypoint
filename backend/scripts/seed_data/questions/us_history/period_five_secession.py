"""Original questions on secessionist justifications and source limitations."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='The Civil War', code='5.7', set_id='south-carolina-causes',
    source_url='https://home.nps.gov/articles/000/south-carolina-secession.htm',
    source_kind='original instructional summary',
    stimulus='South Carolina adopted its ordinance of secession on December 20, 1860, following Lincoln’s election. Four days later its convention issued a declaration explaining its action. The declaration emphasized perceived threats to slavery and complaints about northern resistance to the return of fugitives from slavery. This is an original summary of the convention’s stated justification, not a statement of every resident’s views.',
    items=[
        ('claims-evidence', 2, 'Which interpretation is most directly supported by the declaration as summarized?', 2, [
            ('The convention’s central complaint was that the federal government had abolished slavery nationwide before the election.', 'Nationwide abolition had not occurred; the declaration concerned perceived threats and resistance to slaveholders’ claims.'),
            ('The convention treated slavery as unrelated to its constitutional grievances.', 'The specified grievances directly concern protecting slavery.'),
            ('Protection of slavery was central to the convention’s justification for secession.', 'Both the perceived threat and the complaint about fugitive recovery connect secession to slavery.'),
            ('The convention sought to replace slavery with a uniform system of free labor.', 'The summary describes a defense of slavery, not a proposal to replace it.'),
        ]),
        ('sourcing', 3, 'Which use of the declaration best accounts for its authorship and purpose?', 0, [
            ('Use it to examine the convention’s public justification, while consulting other sources about residents’ varied positions.', 'An official declaration is strong evidence of the convention’s stated rationale, but not a survey of all residents.'),
            ('Treat it as direct testimony from enslaved residents explaining their preferred political future.', 'The convention did not speak as a representative body of enslaved residents.'),
            ('Treat its adoption as proof that all white residents held identical motives.', 'An institutional statement does not establish uniform individual reasoning.'),
            ('Dismiss it as irrelevant because a statement intended to persuade cannot reveal political priorities.', 'Persuasive purpose is a feature to analyze, not a reason to discard the source.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test the convention’s characterization of Lincoln’s immediate intentions?', 1, [
            ('A later monument repeating the declaration’s accusations.', 'Repetition in commemoration does not independently test the contemporary characterization.'),
            ('Lincoln’s contemporary speeches and the Republican platform, compared with the specific claims in the declaration.', 'These allow comparison between opponents’ portrayal and the positions publicly expressed by Lincoln and his party.'),
            ('The declaration’s own assertions counted as independent corroboration of one another.', 'Assertions within the same document do not supply independent corroboration.'),
            ('The date of secession used as proof of the policies Lincoln had already enacted as president.', 'Lincoln had not yet taken office; the date cannot establish enacted presidential policy.'),
        ]),
    ],
)
