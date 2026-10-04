"""Original practice on educational equality in the expanding rights movement."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Civil Rights Movement Expands', code='8.11', set_id='title-ix-education',
    source_url='https://www.archives.gov/news/articles/title-ix',
    source_kind='original instructional summary',
    stimulus='Title IX, part of the Education Amendments signed in 1972, prohibited discrimination on the basis of sex in education programs and activities receiving federal financial assistance. Its scope concerned education, including academic opportunities and athletics, rather than athletics alone. The law became an important instrument for pursuing educational equality. This summary concerns the historical enactment, not later regulatory details.',
    items=[
        ('contextualization', 2, 'Which broader development best contextualizes this legislation?', 1, [
            ('The replacement of all federal civil-rights enforcement with voluntary local agreements.', 'Title IX established a federal prohibition tied to financial assistance rather than eliminating federal involvement.'),
            ('The expansion of organized demands for equal opportunity, including challenges to sex discrimination.', 'The legislation fits the widening rights agenda and efforts to address institutional barriers facing women.'),
            ('The first extension of voting rights to women through a constitutional amendment in the 1970s.', 'The Nineteenth Amendment was ratified in 1920; Title IX addressed education rather than initial constitutional suffrage.'),
            ('A policy of limiting federal involvement to military institutions and foreign affairs.', 'The statute addressed domestic educational programs receiving federal assistance.'),
        ]),
        ('comparison', 3, 'How did Title IX differ from the Nineteenth Amendment?', 2, [
            ('Title IX regulated voting eligibility, while the Nineteenth Amendment regulated college athletic budgets.', 'These descriptions reverse and misstate the measures’ subjects.'),
            ('Both measures were constitutional amendments adopted through state ratification.', 'Title IX was federal legislation; the Nineteenth Amendment changed the Constitution.'),
            ('Title IX addressed sex discrimination in federally assisted education, while the amendment prohibited denying voting rights on account of sex.', 'The comparison distinguishes institutional scope and legal form without assuming either measure eliminated every barrier.'),
            ('The amendment prohibited every form of sex discrimination, making any later education legislation legally redundant.', 'Its voting-rights provision did not itself establish a comprehensive prohibition covering all educational discrimination.'),
        ]),
        ('claims-evidence', 4, 'A historian claims Title IX immediately equalized all educational opportunities in 1972. Which evidence would best evaluate the claim?', 0, [
            ('Records of program access, resources, complaints, and enforcement before and after enactment across different institutions.', 'Evidence about implementation and outcomes can test both the timing and the universal scope of the claim.'),
            ('The statute’s enactment date without evidence of institutional practice.', 'An enactment date cannot establish immediate compliance or equal outcomes.'),
            ('The later success of one athlete treated as representative of all academic and athletic opportunities.', 'One experience cannot establish universal access across institutions and fields.'),
            ('A list of programs receiving federal funds without evidence of their treatment of students.', 'Funding identifies potential institutional scope but does not establish whether discrimination ceased.'),
        ]),
    ],
)
