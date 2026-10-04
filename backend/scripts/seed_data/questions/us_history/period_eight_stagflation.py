"""Original interpretation of contemporaneous Census economic evidence."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='Society in Transition', code='8.14', set_id='stagflation-households',
    source_url='https://www.census.gov/library/publications/1977/demo/p60-104.html',
    source_kind='original instructional summary',
    stimulus='Selected figures reported by the Census Bureau in 1977 (1974 income figures revised for comparability): median household money income — 1974: $11,200; 1975: $11,800. Average annual unemployment rate — 1974: 5.6%; 1975: 8.5%. The report described a roughly 9% increase in consumer prices and a 2% decline in real gross national product between those years. Dollar income figures are not adjusted for inflation. These are historical estimates from the cited report.',
    items=[
        ('claims-evidence', 2, 'Which conclusion about median household purchasing power is best supported?', 1, [
            ('Purchasing power necessarily increased because the dollar income figure was higher.', 'Nominal income rose by about 5 percent, less than the reported price increase.'),
            ('Purchasing power declined despite a rise in dollar income because prices increased more rapidly.', 'Adjusting the income increase for the roughly 9 percent price rise yields a decline in real purchasing power.'),
            ('Purchasing power was unchanged because inflation affects businesses but not households.', 'Consumer price changes affect what household money income can buy.'),
            ('The median proves every household lost exactly the same dollar amount.', 'A national median does not establish identical changes for individual households.'),
        ]),
        ('contextualization', 3, 'Why are these figures consistent with the economic problem called stagflation?', 2, [
            ('They show falling consumer prices alongside uninterrupted growth in real production.', 'The source reports rising prices and declining real output.'),
            ('They show that higher nominal income necessarily eliminated unemployment.', 'The unemployment rate increased even though median nominal income rose.'),
            ('They combine substantial price increases with declining real output and rising unemployment.', 'Stagflation describes inflation occurring alongside economic stagnation or weakness, rather than a simple expansion-driven rise in prices.'),
            ('They show only a change in the number of dollars printed, with no evidence about prices or employment.', 'The report explicitly includes price and unemployment measures as well as output.'),
        ]),
        ('argumentation', 4, 'An essay claims that a single government policy fully explains the economic changes shown. What is the strongest evaluation?', 0, [
            ('The figures establish a pattern, but evaluating the causal claim requires evidence about policy timing, energy costs, and other economic influences.', 'Descriptive national measures do not isolate a sole cause; causal interpretation requires additional evidence and competing explanations.'),
            ('The claim is proven because two changes occurring in the same year must have the same single cause.', 'Coinciding changes do not identify a cause or establish that only one factor mattered.'),
            ('The claim is disproven because government decisions can never affect economic conditions.', 'The data do not justify ruling out policy effects altogether.'),
            ('The claim can be tested by replacing the unemployment rate with the median income and treating them as interchangeable.', 'Different measures describe different aspects of the economy; substitution would obscure rather than test causation.'),
        ]),
    ],
)
