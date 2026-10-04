"""Original historical interpretation of Census nativity data."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 9: 1980-Present', topic='Demographic and Cultural Change Since 1980',
    code='9.5', set_id='nativity-series',
    source_url='https://www.census.gov/library/working-papers/2006/demo/POP-twps0081.html',
    source_kind='original instructional summary',
    stimulus='Selected decennial Census figures, foreign-born residents as a percentage of the total U.S. population: 1970 — 4.7%; 1980 — 6.2%; 1990 — 7.9%; 2000 — 11.1%. These figures describe the resident population at each census, not the number of people arriving during that year. Source: Census Bureau, Historical Census Statistics on the Foreign-Born Population, 1850–2000 (2006).',
    items=[
        ('continuity-and-change', 2, 'Which interpretation of the figures is best supported?', 2, [
            ('The foreign-born share grew by the same number of percentage points in each decade.', 'The increases were 1.5, 1.7, and 3.2 percentage points, so they were not constant.'),
            ('Immigration first became a significant demographic force after 1980.', 'The series documents an earlier foreign-born population and cannot establish when immigration first became significant.'),
            ('The foreign-born share increased throughout the series, with its largest percentage-point gain in the 1990s.', 'The 1990–2000 increase of 3.2 percentage points exceeds the preceding decade increases.'),
            ('More than one in ten residents immigrated to the United States during 2000.', 'The 11.1 percent figure includes foreign-born residents who arrived in earlier years.'),
        ]),
        ('contextualization', 3, 'Which earlier policy change most directly helps contextualize the immigration patterns underlying this series?', 0, [
            ('The 1965 replacement of national-origins quotas with a system emphasizing family relationships and employment qualifications.', 'The 1965 law changed admission priorities and helped reshape later migration; the table alone does not isolate its effects.'),
            ('The 1924 adoption of national-origins quotas favoring northern and western Europe.', 'That restriction shaped earlier migration but had been replaced before the period covered here.'),
            ('The wartime relocation and incarceration of Japanese Americans beginning in 1942.', 'That policy concerned wartime removal and confinement, rather than the later admission system.'),
            ('The 1887 division of tribal lands into individual allotments.', 'The Dawes Act concerned Native landholding and assimilation, not twentieth-century immigrant admissions.'),
        ]),
        ('claims-evidence', 4, 'A historian claims these percentages show that most immigrants arriving in the 1990s settled in the South. What additional evidence is most necessary to evaluate that claim?', 1, [
            ('A national count of foreign-born residents in 2000 without geographic detail.', 'A national total still does not show where recent arrivals settled.'),
            ('Regional residence data identifying foreign-born residents by their period of arrival.', 'Both location and arrival period are necessary to test a claim about the destinations of 1990s arrivals.'),
            ('The percentage of all U.S. residents living in the South in 2000.', 'This includes native-born residents and does not identify the destinations of recent immigrants.'),
            ('A comparison of the foreign-born share in 1970 and 1980.', 'Earlier national percentages do not establish regional settlement in the 1990s.'),
        ]),
    ],
)
