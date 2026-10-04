"""Original instructional questions on industrial and plantation interdependence."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Market Revolution: Industrialization', code='4.5', set_id='cotton-connections',
    source_url='https://www.nps.gov/lowe/learn/historyculture/anti-slavery-in-lowell.htm',
    source_kind='original instructional summary',
    stimulus='In the early nineteenth century, Lowell’s textile mills processed cotton produced through enslaved labor. Northern manufacturing thus depended on a supply chain that connected wage labor in factories with coerced labor on southern plantations. Some people involved in Lowell’s economy nevertheless participated in antislavery activism. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('claims-evidence', 2, 'Which relationship does the summary most directly illustrate?', 2, [
            ('Northern factories operated without agricultural raw materials.', 'Cotton was an agricultural input essential to textile production.'),
            ('All northern industrial workers were enslaved.', 'Economic dependence on enslaved labor elsewhere did not make all northern workers enslaved.'),
            ('Distinct regional labor systems were linked through commercial production.', 'Cotton connected enslaved plantation labor with wage labor in textile manufacturing.'),
            ('Southern plantations produced only for local household use.', 'Cotton supplied distant manufacturers, demonstrating production for broader markets.'),
        ]),
        ('causation', 3, 'Growing textile production would most directly increase demand for', 0, [
            ('raw cotton supplied to mills.', 'Textile manufacturing required cotton inputs, linking industrial demand to agricultural production.'),
            ('the elimination of all commercial exchange.', 'Manufacturing depended on commercial exchange rather than its elimination.'),
            ('the immediate abandonment of plantations.', 'Cotton demand could strengthen plantation production rather than automatically end it.'),
            ('the replacement of all machinery with household handwork.', 'Industrial growth expanded mechanized production rather than requiring a return to household handwork.'),
        ]),
        ('argumentation', 4, 'Which interpretation best accounts for the antislavery activism mentioned?', 3, [
            ('Economic involvement in cotton proves every participant supported slavery.', 'The activism contradicts the inference that economic involvement always dictated an identical political position.'),
            ('Antislavery views prove Lowell had no economic connection to slavery.', 'Political opposition could coexist with economic participation in a cotton-dependent economy.'),
            ('All factory owners and workers held the same political views.', 'The summary does not establish uniform views across these groups.'),
            ('Economic connections and political convictions could exist in tension.', 'Participation in a slavery-dependent economy did not prevent some people from opposing slavery.'),
        ]),
        ('comparison', 3, 'Which distinction is essential when comparing the labor systems connected by this supply chain?', 1, [
            ('Factory workers and enslaved workers had identical legal status.', 'Their legal status and ability to control their labor differed fundamentally.'),
            ('Wage laborers were legally free, while enslaved people were held as property and denied freedom.', 'Economic interdependence does not erase the fundamental distinction between wage labor and slavery.'),
            ('Only factory labor produced goods for sale.', 'Plantation labor also produced commodities for sale.'),
            ('Plantation labor was unrelated to industrial output.', 'The cotton supply directly linked plantation labor to industrial production.'),
        ]),
    ],
)
