"""Original questions on constitutional procedure and partisan interpretation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='The Rise of Political Parties and Democracy', code='4.7', set_id='election-1824',
    source_url='https://www.archives.gov/education/lessons/electoral-tally',
    source_kind='original instructional summary',
    stimulus='In the 1824 presidential election, Andrew Jackson received 99 electoral votes, John Quincy Adams 84, William Crawford 41, and Henry Clay 37. No candidate won an electoral majority. The House selected Adams under the constitutional procedure. Clay supported Adams and later became secretary of state. Jackson’s supporters alleged a corrupt bargain, an accusation that helped sustain opposition to Adams but was not proof of an agreement. This is an original instructional summary.',
    items=[
        ('claims-evidence', 2, 'Why did Jackson’s lead in the electoral tally not settle the election?', 2, [
            ('The Constitution required unanimous electoral support for a candidate.', 'Unanimity was not required; an electoral majority was the relevant threshold.'),
            ('The House could disregard any electoral majority whenever it preferred another candidate.', 'The contingent procedure applied because no candidate secured a majority.'),
            ('A plurality was insufficient when the required electoral majority had not been reached.', 'Jackson led the other candidates individually but had fewer votes than the others combined.'),
            ('Clay’s votes automatically transferred to Jackson when Clay finished fourth.', 'Electoral votes did not automatically transfer in that manner.'),
        ]),
        ('causation', 3, 'How could the accusation influence politics even without proof of an agreement?', 0, [
            ('It gave Jackson’s supporters a way to portray Adams’s victory as contrary to popular choice and mobilize opposition.', 'A politically persuasive interpretation can motivate organizing even when its factual allegation remains unproven.'),
            ('It legally invalidated the House vote as soon as supporters repeated it.', 'An accusation did not automatically overturn the constitutional result.'),
            ('It required Clay to surrender his former electoral votes to Adams retroactively.', 'The controversy concerned House support and an appointment, not a retroactive transfer of electoral votes.'),
            ('It established that every voter had supported Jackson rather than his rivals.', 'Jackson’s support did not amount to unanimity, and the accusation cannot establish voters’ individual preferences.'),
        ]),
        ('sourcing', 4, 'Which use of a Jackson campaign pamphlet repeating the allegation would be most defensible?', 1, [
            ('Treat it as conclusive proof of the terms of a private agreement between Adams and Clay.', 'A partisan allegation alone does not establish the existence or terms of a private agreement.'),
            ('Use it to analyze how supporters framed the result, then seek independent evidence for claims about negotiations.', 'The pamphlet directly documents political messaging; its factual allegations require corroboration.'),
            ('Discard it because partisan sources cannot reveal anything useful about political conflict.', 'Partisan sources can be valuable evidence of rhetoric, aims, and mobilization.'),
            ('Use its circulation as a precise count of voters who believed every claim it contained.', 'Distribution does not establish either individual belief or voting behavior.'),
        ]),
    ],
)
