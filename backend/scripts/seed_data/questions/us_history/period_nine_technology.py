"""Original technology-adoption and historical evidence questions."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 9: 1980-Present', topic='Globalization and the Technological Revolution', code='9.4', set_id='household-computing',
    source_url='https://www.census.gov/library/publications/2013/demo/p20-569.html',
    source_kind='original instructional summary',
    stimulus='The Census Bureau’s Current Population Survey began asking about computer use in 1984 and Internet use in 1997. Its historical tables track household adoption over time and differences among population groups. Computer ownership, home Internet use, and individual use are distinct measures. This is an original instructional summary of the report’s evidence, not a claim that the technologies originated when survey questions began.',
    items=[
        ('sourcing', 2, 'What can the start date of a survey question establish most directly?', 1, [
            ('The exact date the technology was invented.', 'A survey’s measurement history is not the technology’s invention history.'),
            ('When that survey began collecting evidence on the specified measure.', 'The date identifies the beginning of that measurement series.'),
            ('The date every household first obtained the technology.', 'Survey timing does not establish universal adoption.'),
            ('The point after which differences among households disappeared.', 'Collecting data does not eliminate differences in access or use.'),
        ]),
        ('comparison', 3, 'Which comparison would best measure change in household adoption without confusing different measures?', 2, [
            ('Computer ownership in one year compared with individual Internet use in another, treated as identical categories.', 'Different units and definitions make this an unreliable direct adoption comparison.'),
            ('The year a survey began compared with a single company’s founding date.', 'Those dates do not measure household adoption.'),
            ('Household computer-use estimates across years, after checking question wording and population definitions.', 'Comparable measures and awareness of methodological changes support a valid historical comparison.'),
            ('One household’s account treated as a complete national time series.', 'An individual account cannot substitute for national estimates.'),
        ]),
        ('argumentation', 4, 'A historian argues that digital technology changed every household’s opportunities equally. Which evidence would most directly test that claim?', 0, [
            ('Group-level access and use data combined with evidence about affordability, available services, and uses of the technology.', 'Disaggregated access and experience can reveal differences concealed by national adoption totals.'),
            ('A rising national ownership total alone.', 'Aggregate growth does not establish equal access or equal effects.'),
            ('An advertisement promising that a new computer would transform society.', 'Promotional claims reveal expectations rather than uniform lived outcomes.'),
            ('The name of the first survey containing a computer question.', 'A survey title does not measure the distribution of opportunities.'),
        ]),
    ],
)
