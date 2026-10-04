"""Original Allied strategy and diplomacy source sets."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='World War II', code='7.13', set_id='overlord-planning',
    source_url='https://www.archives.gov/milestone-documents/general-eisenhowers-order-of-the-day',
    source_kind='original instructional summary',
    stimulus='Planning for the Normandy invasion involved Allied negotiations, a unified commander, and extensive naval, air, and ground preparations. Eisenhower distributed an encouraging message to the expeditionary force before the June 1944 landings. He also prepared a separate statement accepting responsibility if the operation failed. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'The preparations described most directly illustrate which requirement of Allied warfare?', 2, [
            ('The replacement of ground operations by diplomacy alone.', 'The negotiations supported a major ground invasion rather than replacing it.'),
            ('The abandonment of naval transport in the European theater.', 'Cross-Channel operations depended on naval resources.'),
            ('Coordination of coalition decisions with combined military resources.', 'Allied negotiations and integrated preparations were necessary for the invasion.'),
            ('The use of a single national force without contributions from allies.', 'The expedition was a coalition undertaking.'),
        ]),
        ('sourcing', 3, 'Why should Eisenhower’s encouraging message be read differently from an after-action assessment?', 0, [
            ('It sought to strengthen resolve before an uncertain operation rather than report verified outcomes afterward.', 'Audience, purpose, and timing shape the message’s claims and tone.'),
            ('It was written after Germany surrendered to record the final peace terms.', 'The message preceded the landings and Germany’s surrender.'),
            ('It was addressed only to enemy commanders to negotiate a cease-fire.', 'Its intended audience was the Allied expeditionary force.'),
            ('It contained no connection to the impending military operation.', 'The operation provided the message’s immediate context.'),
        ]),
        ('argumentation', 4, 'What does the separate contingency statement most directly qualify?', 1, [
            ('The claim that the invasion required advance preparation.', 'Preparing for possible failure is consistent with advance planning.'),
            ('The claim that confident public language proves the commander considered success certain.', 'A prepared failure statement demonstrates that confident encouragement could coexist with awareness of risk.'),
            ('The claim that a commander bore responsibility for operational decisions.', 'The statement accepts such responsibility rather than contradicting it.'),
            ('The claim that troops received a message before the landings.', 'The existence of a second statement does not challenge the timing of the first.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 7: 1890-1945', topic='World War II', code='7.14', set_id='yalta-bargaining',
    source_url='https://history.state.gov/milestones/1937-1945/yalta-conf',
    source_kind='original instructional summary',
    stimulus='At Yalta in February 1945, Roosevelt, Churchill, and Stalin negotiated while the war continued. Discussions linked Soviet entry against Japan with concessions in Asia and addressed Germany, Eastern Europe, and voting in the proposed United Nations Security Council. Agreement on wartime and institutional questions did not eliminate later conflict over Eastern Europe. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Why did the Pacific war influence negotiations over postwar arrangements at Yalta?', 3, [
            ('Japan had already surrendered, leaving no military issues to discuss.', 'Japan’s surrender came later in 1945.'),
            ('The United States had formally joined the Soviet Union as a single country.', 'Cooperation between sovereign allies did not merge their governments.'),
            ('The conference concerned only European boundaries and excluded Asian questions.', 'The negotiations explicitly linked Soviet participation against Japan with Asian concessions.'),
            ('The Allies valued prospective Soviet military participation and bargained over conditions for it.', 'Anticipated military needs shaped diplomatic concessions before the war ended.'),
        ]),
        ('comparison', 3, 'Which interpretation best captures the relationship between wartime cooperation and postwar disagreement?', 1, [
            ('Cooperation proves that all allies held identical long-term political aims.', 'A shared enemy did not remove divergent interests concerning the postwar settlement.'),
            ('States could cooperate against common enemies while retaining conflicting interests about the peace.', 'Agreements and subsequent disputes can coexist within the same alliance.'),
            ('Later disputes prove that the leaders never reached any agreements at Yalta.', 'Later conflict does not erase the agreements described.'),
            ('Agreement on an international institution made future diplomatic conflict impossible.', 'Institutional agreement did not guarantee agreement on every regional issue.'),
        ]),
        ('argumentation', 4, 'Which evidence would best evaluate whether commitments concerning Eastern Europe were implemented as negotiators expected?', 0, [
            ('Conference records compared with subsequent political developments and contemporaneous diplomatic reports.', 'This comparison tests implementation and interpretations against the negotiated commitments.'),
            ('A photograph showing the three leaders seated together.', 'A photograph establishes presence but not the meaning or fulfillment of commitments.'),
            ('The date of the conference without its agreements.', 'Chronology alone cannot establish expectations or implementation.'),
            ('A later commentator’s conclusion without identifying supporting records.', 'An unsupported conclusion cannot substitute for evidence about commitments and subsequent actions.'),
        ]),
    ],
)
