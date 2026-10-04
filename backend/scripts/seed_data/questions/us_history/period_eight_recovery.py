"""Original practice on economic recovery as an instrument of containment."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Cold War and Containment', code='8.2', set_id='marshall-recovery',
    source_url='https://history.state.gov/milestones/1945-1952/marshall-plan',
    source_kind='original instructional summary',
    stimulus='Marshall called for European reconstruction in 1947, and Congress funded the European recovery program in 1948. Supporters connected economic stabilization with resisting Communist influence. Aid ultimately went to Western Europe rather than the Soviet bloc. Recovery also expanded markets for American products, while historians debate the precise contribution of aid to European economic growth. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Which reasoning best explains the connection supporters drew between economic aid and containment?', 1, [
            ('Economic recovery would remove the need for any further diplomatic decisions.', 'Supporters linked recovery to political stability, not an end to diplomacy.'),
            ('Improved economic conditions could strengthen governments and reduce the appeal of Communist movements.', 'This connects economic reconstruction to the political objective of limiting Communist influence.'),
            ('Reconstruction was intended to make European governments dependent on Soviet trade alone.', 'The program supported Western European recovery and American trade, not exclusive Soviet dependence.'),
            ('American security depended on keeping European industrial production permanently low.', 'The program promoted reconstruction rather than permanent industrial weakness.'),
        ]),
        ('comparison', 3, 'Which distinction best separates the Marshall Plan’s central instrument from a mutual-defense alliance?', 2, [
            ('The plan addressed only domestic American infrastructure, while alliances concerned foreign affairs.', 'The recovery program supplied aid abroad and was itself foreign policy.'),
            ('The plan rejected international cooperation, while alliances required it.', 'Reconstruction aid involved substantial international cooperation.'),
            ('The plan used reconstruction assistance, while an alliance formalized security commitments among members.', 'Economic assistance and collective-defense commitments are different instruments even when they serve related strategic goals.'),
            ('The plan transferred European sovereignty to the United States, while alliances required territorial annexation.', 'Neither economic aid nor a mutual-defense alliance inherently entails annexation or transfer of sovereignty.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly qualify the claim that the recovery program was motivated exclusively by humanitarian concern?', 0, [
            ('Policy deliberations connecting reconstruction funding to Communist influence and markets for American exports.', 'Evidence of strategic and economic objectives would challenge an exclusively humanitarian explanation without denying humanitarian effects.'),
            ('Records showing that European communities suffered severe wartime destruction.', 'These establish humanitarian need but do not test whether it was the only policy motive.'),
            ('Accounts of recipients using aid to restore essential production.', 'These demonstrate reconstruction activity rather than the full range of American motives.'),
            ('A chronology placing the aid program after the war.', 'Timing alone cannot distinguish humanitarian, strategic, and commercial motives.'),
        ]),
    ],
)
