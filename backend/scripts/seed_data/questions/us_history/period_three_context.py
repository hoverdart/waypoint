"""Original instructional stimulus and questions about the imperial crisis."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Contextualizing Period 3', code='3.1',
    source_url='https://history.state.gov/milestones/1750-1775/french-indian-war',
    source_kind='original instructional summary',
    stimulus='In the mid-eighteenth century, British and French ambitions collided in the Ohio Valley. The conflict grew into a wider imperial war. Britain emerged with expanded territorial claims in 1763 but also substantial expenses. Disagreements over how to govern and finance the enlarged empire helped strain relations between Britain and its mainland colonists. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('contextualization', 2, 'Which broader setting best explains the conflict described?', 2, [
            ('A contest between independent United States political parties.', 'The conflict began before American independence and before the formation of national political parties.'),
            ('A struggle over reconstruction after the American Civil War.', 'Reconstruction followed the Civil War in the nineteenth century.'),
            ('Competition among European empires over territory and influence.', 'British and French expansion brought competing imperial claims into conflict.'),
            ('An effort by the United States to annex Mexican territory.', 'The United States did not yet exist, and the conflict concerned British and French imperial claims.'),
        ]),
        ('causation', 3, 'Which development best explains how a British victory could contribute to conflict with British colonists?', 0, [
            ('Efforts to make colonists help finance imperial expenses raised disputes over parliamentary authority.', 'Victory left costs to meet, and revenue policies intensified disagreement over how the colonies should be governed.'),
            ('Britain transferred all its mainland colonies to France.', 'British victory expanded British claims rather than transferring all mainland colonies to France.'),
            ('The war immediately established an independent American national government.', 'Independence followed a later imperial crisis; it was not an immediate institutional result of the 1763 settlement.'),
            ('Parliament permanently renounced authority to legislate for the colonies.', 'The subsequent crisis involved assertions of parliamentary authority rather than its permanent renunciation.'),
        ]),
        ('argumentation', 4, 'Which claim best captures the relationship between the war and the later American Revolution?', 1, [
            ('The war made independence inevitable regardless of later political choices.', 'A contributing condition is not proof that subsequent decisions and events could have had only one outcome.'),
            ('The war altered imperial circumstances in ways that helped produce later disputes over authority.', 'This connects the changed empire to later conflict without treating a complex revolution as an automatic result.'),
            ('The war and the Revolution were unrelated because they involved different immediate disputes.', 'Postwar finances and governance provided important connections between the conflicts.'),
            ('The Revolution caused the territorial settlement reached in 1763.', 'The 1763 settlement preceded the Revolution, so this reverses the chronology.'),
        ]),
    ],
)
