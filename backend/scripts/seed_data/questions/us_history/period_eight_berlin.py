"""Original containment practice on the Berlin crisis and alternative responses."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Cold War and Containment', code='8.2', set_id='berlin-airlift',
    source_url='https://history.state.gov/milestones/1945-1952/berlin-airlift',
    source_kind='original instructional summary',
    stimulus='Berlin lay inside the Soviet occupation zone of Germany but was itself divided among the occupying powers. In 1948, disputes over Germany’s future and Western currency reforms intensified tensions. Soviet authorities blocked surface access to western Berlin. The United States and Britain supplied the city through air corridors. The blockade ended in 1949, while the political division of Germany persisted.',
    items=[
        ('causation', 2, 'Why did Berlin’s location make the Soviet blockade an effective means of pressure on the Western Allies?', 2, [
            ('Berlin was located inside the American occupation zone, making the Americans responsible for supplying Soviet troops.', 'The city lay within the Soviet occupation zone, though its sectors were separately occupied.'),
            ('The Western Allies had already withdrawn from their Berlin sectors, leaving no continuing commitment to defend.', 'The crisis concerned maintaining the Western presence, not a completed withdrawal.'),
            ('Surface supply routes to the Western sectors crossed Soviet-controlled territory, exposing access to interruption.', 'The relationship between geography and supply explains how blocking routes could pressure the Western position.'),
            ('The city’s location made it dependent on direct ocean shipping from American ports.', 'Berlin was inland; the contested surface links crossed the surrounding Soviet zone.'),
        ]),
        ('causation', 3, 'Compared with sending an armed convoy through the blockade, how could the airlift support containment while reducing the immediate risk of a ground clash?', 0, [
            ('It sustained the Western position by supplying residents without forcing a ground passage through Soviet-controlled routes.', 'Air supply addressed the blockade’s pressure on the city while avoiding an attempt to break through the surface blockade by force.'),
            ('It required the Western Allies to surrender their sectors before delivering supplies.', 'The airlift aimed to sustain the Western position, not make withdrawal a precondition.'),
            ('It transferred control of surrounding Soviet territory to the Western Allies without negotiation.', 'Use of air corridors did not transfer territorial control of the surrounding zone.'),
            ('It made future confrontation impossible by ending all disputes about Germany’s political organization.', 'The airlift did not eliminate the underlying political division or guarantee an end to confrontation.'),
        ]),
        ('argumentation', 4, 'Which thesis best accounts for both the end of the blockade and the continued division of Germany?', 3, [
            ('The airlift failed in every respect because it did not reunify Germany.', 'This treats reunification as the only possible measure and ignores maintenance of the Western position.'),
            ('The blockade’s end demonstrates that Western and Soviet leaders had agreed on a common German political system.', 'The continuing division contradicts a claim that the crisis resolved the political-system dispute.'),
            ('The airlift had purely humanitarian significance because it transported civilian supplies.', 'Civilian assistance also sustained a strategic commitment; the cargo alone does not establish an exclusively humanitarian role.'),
            ('The response helped preserve the Western position in Berlin without resolving the broader conflict over Germany’s future.', 'This distinguishes a limited strategic outcome from settlement of the wider dispute.'),
        ]),
    ],
)
