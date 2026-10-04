"""Original questions on regional differences without assuming economic isolation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Sectional Conflict: Regional Differences', code='5.5', set_id='cotton-connections',
    source_url='https://home.nps.gov/blrv/learn/historyculture/cotton-economy.htm',
    source_kind='original instructional summary',
    stimulus='Before the Civil War, northern textile manufacturers purchased cotton produced by enslaved labor in the South. Some northern mills also sold cloth used to clothe enslaved workers on plantations. These commercial connections existed alongside major regional differences in labor institutions and economic development. This is an original instructional summary.',
    items=[
        ('comparison', 2, 'Which interpretation best accounts for both the connections and differences described?', 2, [
            ('Northern textile production and southern cotton cultivation operated without exchanging goods.', 'Purchases of raw cotton and sales of cloth demonstrate exchange between the regions.'),
            ('Participation in the same trade made wage labor and chattel slavery identical legal institutions.', 'Commercial connections did not erase the distinct legal status and coercion of enslavement.'),
            ('Distinct regional labor systems were linked through purchases of raw materials and manufactured goods.', 'The summary describes interdependence without equating the labor systems.'),
            ('Southern plantations sold only to foreign buyers while northern mills relied exclusively on foreign cotton.', 'The described transactions connect northern mills directly to southern production.'),
        ]),
        ('argumentation', 3, 'Which claim would require evidence beyond these commercial transactions?', 0, [
            ('Every northern textile worker supported the expansion of slavery into western territories.', 'Participation in an industry does not establish uniform political beliefs among its workers.'),
            ('Some northern manufacturers had business relationships with southern plantations.', 'The purchases and sales directly support this claim.'),
            ('Products of enslaved labor entered northern manufacturing supply chains.', 'Northern mills’ purchases of southern cotton directly support this claim.'),
            ('Regional economic differences did not prevent trade between the regions.', 'The described exchange alongside differences supports this claim.'),
        ]),
        ('sourcing', 4, 'Which evidence would best test whether these commercial ties affected a particular manufacturer’s political position?', 1, [
            ('A regional production total treated as proof of the manufacturer’s personal beliefs.', 'Aggregate output cannot establish one individual’s political reasoning.'),
            ('The manufacturer’s correspondence linking business concerns to political choices, compared with records of public activity.', 'These sources can connect stated motives with observable political behavior.'),
            ('The location of the factory treated as sufficient evidence of its owner’s position on slavery.', 'Geographic location alone cannot establish a specific political position.'),
            ('A cotton invoice treated as conclusive evidence of opposition to every antislavery proposal.', 'An invoice proves a transaction, not the full range of its purchaser’s political views.'),
        ]),
    ],
)
