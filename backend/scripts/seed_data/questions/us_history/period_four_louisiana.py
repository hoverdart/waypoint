"""Original questions on commerce, diplomacy, and territorial expansion."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Markets and Westward Expansion', code='4.2', set_id='louisiana',
    source_url='https://history.state.gov/milestones/1801-1829/louisiana-purchase', source_kind='original instructional summary',
    stimulus='Western American farmers relied on the Mississippi River and New Orleans to reach distant markets. Jefferson’s administration initially sought to acquire New Orleans, but France offered a much larger territory in 1803. Accepting the offer expanded American territorial claims and raised questions about constitutional authority. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Why was access to New Orleans especially important to western farmers?', 0, [
            ('It connected river transport with wider commercial markets.', 'The port provided an outlet for agricultural goods moving down the Mississippi.'),
            ('It was the only place where the Constitution permitted farming.', 'The Constitution did not restrict farming to New Orleans.'),
            ('It eliminated the need to transport agricultural products.', 'The port facilitated transportation rather than eliminating it.'),
            ('It was the seat of every western state government.', 'Its importance here was commercial, not that it housed every state government.'),
        ]),
        ('contextualization', 3, 'Which circumstance helps explain France’s decision to sell the larger territory?', 2, [
            ('The United States had conquered Paris.', 'The purchase was negotiated without an American conquest of Paris.'),
            ('France had ceased to have any strategic interests outside Europe.', 'France retained overseas interests; it reassessed a particular imperial project.'),
            ('Setbacks in Saint-Domingue and renewed prospects of war with Britain weakened Napoleon’s American plans.', 'Caribbean setbacks and European pressures helped make sale preferable to maintaining Louisiana.'),
            ('The American Civil War forced France to recognize the Confederacy.', 'The purchase occurred in 1803, long before the Civil War.'),
        ]),
        ('comparison', 3, 'The purchase created tension with which earlier position associated with Jefferson?', 1, [
            ('A demand to restore hereditary monarchy.', 'Jefferson advocated republican government rather than monarchy.'),
            ('A preference for a strict reading of federal constitutional powers.', 'The absence of an explicit territorial-purchase provision raised doubts for a leader associated with strict construction.'),
            ('A commitment to prevent all agricultural growth.', 'Jefferson valued agricultural development rather than opposing it categorically.'),
            ('A requirement that France govern the United States.', 'Jefferson did not advocate French government of the United States.'),
        ]),
        ('argumentation', 4, 'Which interpretation best integrates the developments described?', 3, [
            ('Territorial expansion was unrelated to commerce.', 'The importance of Mississippi trade demonstrates a commercial motive.'),
            ('Constitutional interpretation never changed in response to practical opportunities.', 'Jefferson’s response illustrates tension between prior principles and an opportunity for expansion.'),
            ('American expansion depended only on domestic events.', 'France’s offer and changing imperial priorities reveal an international dimension.'),
            ('Commercial needs, international circumstances, and flexible use of federal authority interacted in expansion.', 'This explanation connects the trade motive, France’s circumstances, and the constitutional question without reducing the purchase to one cause.'),
        ]),
    ],
)
