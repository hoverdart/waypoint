"""Original labor-history questions using a public-domain Bagley letter excerpt."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Market Revolution: Society and Culture', code='4.6', set_id='bagley-labor',
    source_url='https://www.nps.gov/lowe/learn/historyculture/the-mill-girls-of-lowell.htm', source_kind='primary excerpt',
    stimulus='Sarah Bagley, Lowell labor reformer, letter to a friend, 1846, promoting Factory Tracts: “who are not willing to see our sex made into living machines to do the bidding of the incorporated aristocrats”',
    items=[
        ('claims-evidence', 2, 'Bagley’s description of workers as “living machines” chiefly criticizes', 1, [
            ('women’s lack of interest in paid employment.', 'Bagley criticizes how employers treat workers, not women’s supposed lack of interest in work.'),
            ('corporate treatment of workers as instruments of production.', 'The metaphor objects to reducing people to tools serving employers’ demands.'),
            ('the complete disappearance of corporations.', 'Her criticism presumes powerful corporations exist.'),
            ('the return of all manufacturing to household production.', 'She addresses corporate factory labor rather than a return to household manufacturing.'),
        ]),
        ('contextualization', 3, 'Which development best explains the setting of Bagley’s criticism?', 3, [
            ('The New Deal’s establishment of federal labor protections.', 'The New Deal came in the 1930s, long after this letter.'),
            ('The elimination of wage labor in northern cities.', 'Factory wage labor expanded during the market revolution.'),
            ('The replacement of industrial employment by universal landownership.', 'Industrial workers did not universally become landowners.'),
            ('The growth of factories employing women under demanding schedules and corporate supervision.', 'Industrial expansion created wage opportunities alongside discipline and conditions that provoked labor reform.'),
        ]),
        ('sourcing', 3, 'Bagley’s role as a labor reformer makes this passage particularly useful as evidence of', 0, [
            ('the language activists used to challenge employers’ authority.', 'Her phrasing reveals how a worker-activist framed corporate power as an affront to workers’ dignity.'),
            ('the unanimous views of every woman in Lowell.', 'One reformer’s statement cannot establish universal agreement.'),
            ('the exact productivity of each textile machine.', 'The metaphor contains no production measurements.'),
            ('an official corporate endorsement of labor reform.', 'Bagley speaks as a reformer criticizing corporations, not as their authorized spokesperson.'),
        ]),
        ('argumentation', 4, 'Which claim best accommodates both women’s access to factory wages and the criticism expressed here?', 2, [
            ('Paid employment eliminated all constraints on women’s lives.', 'Earning wages did not remove corporate discipline or other legal and social constraints.'),
            ('Women had no capacity to organize or express political demands.', 'Bagley’s activism itself contradicts this claim.'),
            ('Industrial employment could create new opportunities while also producing conflicts over autonomy and working conditions.', 'Wage opportunities and collective criticism could coexist; neither alone describes every aspect of factory life.'),
            ('Every reform demand was immediately enacted into law.', 'A demand for reform does not demonstrate legislative success.'),
        ]),
    ],
)
