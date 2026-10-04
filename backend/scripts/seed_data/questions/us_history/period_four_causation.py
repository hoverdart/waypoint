"""Original questions distinguishing causal mechanisms from correlation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Causation in Period 4', code='4.14', set_id='canal-markets',
    source_url='https://nysm.nysed.gov/research-collections/history/economic-history/news/transporting-grains-erie-canal',
    source_kind='original instructional summary',
    stimulus='The Erie Canal opened along its full Albany-to-Buffalo route in 1825. Cheaper transportation connected inland producers with distant buyers. Farmers could sell goods in markets that had previously been costly to reach, while merchants moved products through the canal corridor. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Which mechanism best explains how lower freight charges could encourage commercial farming?', 3, [
            ('They guaranteed that crop prices would remain stable in distant markets.', 'Cheaper transport improved access but did not guarantee stable prices.'),
            ('They reduced the importance of finding buyers beyond the household.', 'Commercial farming depended more on selling to buyers, not less.'),
            ('They made soil quality irrelevant to agricultural production.', 'Transportation costs affected marketing; soil remained important to production.'),
            ('They allowed farmers to reach more buyers while retaining more of a shipment’s sale value.', 'Lower delivery costs could make distant sales profitable and encourage production for exchange.'),
        ]),
        ('argumentation', 3, 'Which evidence would most directly support this proposed mechanism?', 1, [
            ('Speeches predicting that the canal would bring prosperity before it opened.', 'Predictions show expectations rather than the actual link between costs and sales.'),
            ('Farm accounts showing reduced shipping expenses and increased sales to distant purchasers after canal access became available.', 'These records connect the proposed cost change to producers’ marketing behavior.'),
            ('Architectural drawings showing that canal warehouses used similar designs.', 'Building designs do not directly establish shipping savings or changes in agricultural sales.'),
            ('A list of canal officials and their terms of service.', 'Administrative tenure does not directly demonstrate the commercial mechanism.'),
        ]),
        ('causation', 3, 'Which development would complicate an argument that canal construction alone caused agricultural expansion?', 0, [
            ('Population growth also increased demand for farm products during the same years.', 'Growing demand provides an additional cause that should be considered alongside transportation changes.'),
            ('Farmers used canal access to deliver goods to new purchasers.', 'This is evidence of the proposed canal mechanism rather than an independent competing cause.'),
            ('Merchants paid canal tolls when moving agricultural freight.', 'Tolls were part of the transportation system, not by themselves an alternative explanation of growth.'),
            ('Canal shipments increased as more farmers used the waterway.', 'Increased use is consistent with the proposed mechanism and does not alone identify another cause.'),
        ]),
        ('argumentation', 4, 'Which comparison would best help assess the canal’s contribution while recognizing the limits of historical evidence?', 2, [
            ('Compare one prosperous canal town with one impoverished town, without examining their earlier conditions.', 'Selecting towns by their outcomes risks attributing preexisting differences to canal access.'),
            ('Compare canal promoters’ most optimistic predictions with their later commemorative speeches.', 'Two sets of promotional claims do not provide a strong comparison of economic outcomes.'),
            ('Compare changes in similarly situated communities with and without canal access, checking earlier trends and other transport links.', 'This comparison can help distinguish canal access from other influences, though it cannot eliminate every difference.'),
            ('Compare total national farm output before and after 1825 and assign the entire change to the canal.', 'National totals include many regions and causes, so this attribution exceeds the evidence.'),
        ]),
    ],
)
