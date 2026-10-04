"""Original practice on interwar diplomatic engagement and enforcement."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 7: 1890-1945', topic='Interwar Foreign Policy', code='7.11', set_id='peace-pact',
    source_url='https://history.state.gov/milestones/1921-1936/kellogg',
    source_kind='original instructional summary',
    stimulus='Briand initially proposed a bilateral peace agreement with the United States. American officials preferred a wider agreement, concerned that a special commitment to France could draw them into a future conflict. The resulting Kellogg-Briand Pact of 1928 renounced war as national policy and endorsed peaceful settlement. U.S. participation preserved self-defense and did not obligate military enforcement against violators. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Why did American officials favor widening the proposed agreement?', 1, [
            ('They wanted to make the United States the sole guarantor of French security.', 'Their concern was precisely that a bilateral arrangement could imply such an obligation.'),
            ('They sought cooperation for peace while avoiding a special commitment that could draw them into war.', 'The multilateral proposal reflected both diplomatic engagement and resistance to a binding bilateral alliance.'),
            ('They opposed every form of diplomatic contact with European governments.', 'Helping negotiate the wider pact contradicts complete diplomatic disengagement.'),
            ('They wanted France to acquire exclusive authority over American military deployments.', 'The described concerns point toward preserving American discretion, not transferring it.'),
        ]),
        ('comparison', 3, 'Which distinction best explains the limits of the pact as a peacekeeping mechanism?', 2, [
            ('The pact required every signatory to disarm immediately but permitted unlimited territorial conquest.', 'The summary describes renunciation of war, not that combination of requirements.'),
            ('The pact prohibited peaceful negotiation but required military intervention.', 'It endorsed peaceful settlement and did not impose the stated U.S. military obligation.'),
            ('Agreement on a norm against war differed from agreement on an enforceable response to violations.', 'Renunciation and enforcement are separate commitments; the latter was limited.'),
            ('The pact prevented governments from invoking self-defense under any circumstances.', 'Self-defense was preserved, creating a significant question about the scope of renunciation.'),
        ]),
        ('argumentation', 4, 'Which claim about the United States in the 1920s is most directly qualified by its role in negotiating the pact?', 0, [
            ('Avoiding certain security commitments meant withdrawing from all international diplomacy.', 'The United States participated actively in this international agreement while limiting its obligations.'),
            ('Officials worried about being drawn into another European war.', 'Those worries help explain the American negotiating position rather than being contradicted by it.'),
            ('Peace advocates sought alternatives to another world war.', 'The pact is consistent with such efforts.'),
            ('An agreement’s stated aims need to be distinguished from its practical results.', 'The pact’s enforcement limits reinforce rather than qualify this distinction.'),
        ]),
    ],
)
