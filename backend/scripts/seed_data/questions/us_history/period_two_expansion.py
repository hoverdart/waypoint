"""Original questions with verified sources; the 1662 statutory excerpt is public domain."""
from .builders import source_set

PERIOD = 'Period 2: 1607-1754'
RELIGION = 'https://www.loc.gov/exhibits/religion/rel01.html'
AWAKENING = 'https://www.loc.gov/exhibits/religion/rel02.html'
LAW = 'https://encyclopediavirginia.org/primary-documents/negro-womens-children-to-serve-according-to-the-condition-of-the-mother-1662/'

QUESTIONS = source_set(period=PERIOD, topic='Contextualizing Period 2', code='2.1', source_url=RELIGION,
 source_kind='original instructional summary', stimulus='English colonization joined religious projects with economic ventures. Seeking a refuge for one community did not necessarily mean granting equal religious freedom to everyone who arrived. Colonies differed in their religious institutions and rules.', items=[
 ('contextualization',2,'Which conclusion best follows from the summary?',1,[
 ('All colonies began with identical religious laws.','The summary explicitly identifies differing institutions and rules.'),
 ('A colony’s founding purposes must be examined alongside its actual policies.','A refuge for one group does not establish universal toleration.'),
 ('Economic ventures had no connection to religion.','The summary identifies overlapping projects rather than an absolute separation.'),
 ('English settlers had already established federal religious protections.','The later United States constitutional framework did not yet exist.'),
 ]),
 ('claims-evidence',3,'Which source would best test whether a colony protected religious dissenters in practice?',2,[
 ('A promotional claim that the colony offered opportunity.','Promotion alone cannot establish how dissenters were treated.'),
 ('A map showing the colony’s coastline.','Physical boundaries do not establish enforcement of religious rules.'),
 ('Court records concerning people accused of violating religious requirements.','These provide evidence of how authorities applied rules to specific cases.'),
 ('A list of crops exported from the colony.','Exports do not directly demonstrate treatment of dissenters.'),
 ]),
 ('comparison',4,'Which comparison avoids an unsupported generalization?',0,[
 ('Compare specific colonies’ legal provisions and enforcement rather than assuming one colonial policy.','Variation requires comparison at the relevant institutional level.'),
 ('Treat every colony founded for religious reasons as equally tolerant.','A religious motive does not establish identical toleration.'),
 ('Assume a commercial colony had no religious institutions.','Economic purposes do not exclude religious institutions.'),
 ('Infer every resident’s beliefs from the established church alone.','Official institutions do not establish uniform private belief.'),
 ]),
]) + source_set(period=PERIOD, topic='Slavery in the British Colonies', code='2.6', source_url=LAW,
 source_kind='primary excerpt', stimulus='Virginia General Assembly, December 1662, excerpt (original spelling): “all children borne in this country shalbe held bond or free only according to the condition of the mother.”', items=[
 ('claims-evidence',2,'Under this provision, what determined a child’s legal status?',3,[
 ('The father’s place of birth.','The quoted rule specifies the mother’s condition, not the father’s birthplace.'),
 ('The child’s future occupation.','The statute assigns status through birth rather than occupation.'),
 ('A fixed term negotiated when the child became an adult.','The rule is not a contract for a limited term of service.'),
 ('The mother’s status as enslaved or free.','The statute explicitly ties the child’s condition to that of the mother.'),
 ]),
 ('causation',3,'Which consequence did the rule facilitate?',1,[
 ('Automatic emancipation of children whose fathers were free.','The rule disregards that basis for freedom by specifying maternal status.'),
 ('The reproduction of enslavement across generations through enslaved mothers.','Children inherited an enslaved mother’s condition under the rule.'),
 ('The elimination of all distinctions between indentured service and slavery.','The excerpt does not make every labor arrangement identical.'),
 ('The abolition of slavery throughout British North America.','The rule reinforced hereditary enslavement rather than abolishing it.'),
 ]),
 ('sourcing',4,'Which limitation matters when using this statute as evidence?',2,[
 ('A law cannot reveal anything about a society’s power relationships.','Rules assigning status provide important evidence of institutional power.'),
 ('It establishes that every British colony used precisely the same rule in 1662.','A Virginia statute cannot alone establish other colonies’ laws.'),
 ('It expresses a legal rule but does not alone reveal every affected person’s experience or its enforcement.','Legal prescription must be examined alongside evidence of practice and experience.'),
 ('Because it is old, its wording cannot be analyzed.','Age calls for context, not abandonment of analysis.'),
 ]),
]) + source_set(period=PERIOD, topic='Colonial Society and Culture', code='2.7', source_url=AWAKENING,
 source_kind='original instructional summary', stimulus='The Great Awakening connected religious revivals in the American colonies and Britain during the 1730s and 1740s. Preachers emphasized conversion and renewed religious experience; sermons and printed writings circulated across the Atlantic.', items=[
 ('contextualization',2,'The circulation described most directly challenges which interpretation?',0,[
 ('Colonial religious life developed in complete isolation from Britain.','Transatlantic preaching and print demonstrate continuing connections.'),
 ('Religious ideas could move between communities.','Circulation supports rather than challenges this interpretation.'),
 ('Printed material could help spread religious debate.','The summary explicitly identifies circulated writings.'),
 ('Colonial society included religious activity.','Revivals are evidence for this statement, not against it.'),
 ]),
 ('sourcing',3,'A revival sermon is especially useful for investigating which question?',3,[
 ('Exactly what every listener privately believed afterward.','The sermon cannot establish each listener’s response.'),
 ('The total population of all colonies.','A sermon is not a population enumeration.'),
 ('The precise profits of all printers distributing it.','Its text does not establish financial records.'),
 ('How a preacher sought to persuade an audience about religious experience.','Language, appeals, and emphasis offer evidence of persuasive purpose.'),
 ]),
 ('causation',4,'Which claim requires additional evidence beyond the summary?',1,[
 ('The revivals had a transatlantic dimension.','Connections between Britain and the colonies support this claim.'),
 ('The revivals directly caused every participant to support independence decades later.','A universal later political consequence cannot be inferred from religious circulation.'),
 ('Print was one means of exchanging religious ideas.','Circulated writings directly support this claim.'),
 ('Conversion was an important concern of revival preaching.','The summary explicitly identifies that emphasis.'),
 ]),
]) + source_set(period=PERIOD, topic='Comparison in Period 2', code='2.8', source_url=RELIGION,
 source_kind='original instructional summary', stimulus='Some English colonies were organized as religious refuges, while Virginia began as a commercial venture whose leaders also supported a church. A colony’s economic purpose and religious commitments were not mutually exclusive categories.', items=[
 ('comparison',2,'Which thesis is best supported by this comparison?',2,[
 ('Religious and commercial motives never appeared together.','Virginia’s example contradicts an absolute separation.'),
 ('All colonial institutions were determined by one motive.','Overlapping purposes make this explanation too simple.'),
 ('Founding motives varied, but economic and religious purposes could overlap.','This accommodates both variation and the shared presence of multiple purposes.'),
 ('Religious commitments ended when colonies began trading.','No such sequence is established.'),
 ]),
 ('claims-evidence',3,'Which evidence would strengthen a comparison of these colonies’ institutions?',0,[
 ('Charters and laws identifying who could govern and how churches were supported.','Comparable institutional records allow specific similarities and differences to be evaluated.'),
 ('One modern travel advertisement describing scenery.','Scenery does not establish colonial institutional arrangements.'),
 ('An assumption that a colony’s name explains all of its laws.','A name is not sufficient evidence of governance.'),
 ('A statement that all colonies eventually joined the same country.','A later shared outcome does not establish earlier institutional similarity.'),
 ]),
 ('making-connections',4,'Why would it be misleading to use “religious” and “economic” as exclusive categories for this comparison?',3,[
 ('Historical comparisons cannot use categories.','Categories can be useful if they fit the evidence.'),
 ('Every colonial resident held the same priorities.','The summary does not establish uniform individual priorities.'),
 ('Economic records are always less reliable than religious records.','Reliability depends on specific sources and questions, not this universal ranking.'),
 ('The categories would hide institutions and goals that existed together in the same colony.','Exclusive categories would obscure the overlap the example demonstrates.'),
 ]),
])
