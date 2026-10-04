"""Original military-strategy questions grounded in the Mississippi campaign."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='The Civil War', code='5.8', set_id='mississippi-campaign',
    source_url='https://www.nps.gov/vick/planyourvisit/park-maps-and-brochure.htm',
    source_kind='original instructional summary',
    stimulus='Vicksburg surrendered to Union forces on July 4, 1863. Port Hudson surrendered five days later. Together these victories removed the remaining major Confederate strongholds blocking Union control of the Mississippi River. This is an original instructional summary.',
    items=[
        ('causation', 2, 'Why was control of this river strategically significant?', 1, [
            ('It placed the Confederate capital directly under Union occupation.', 'Richmond was far from the Mississippi; river control did not capture the capital.'),
            ('It opened a major Union transportation route while disrupting Confederate connections across the river.', 'River control supported movement and supply while dividing Confederate territory.'),
            ('It ended the need to maintain Union naval operations along southern coasts.', 'River control did not make coastal operations or the blockade unnecessary.'),
            ('It transferred command of all Confederate field armies to Union officers.', 'Surrender of these strongholds did not transfer command of other Confederate armies.'),
        ]),
        ('claims-evidence', 3, 'Which interpretation most accurately preserves the sequence described?', 2, [
            ('Port Hudson had surrendered before the Vicksburg campaign ended.', 'The summary places Port Hudson’s surrender five days after Vicksburg’s.'),
            ('Vicksburg’s surrender alone removed every remaining major Confederate river stronghold that day.', 'Port Hudson remained until its later surrender.'),
            ('Vicksburg was a major victory, followed by another surrender that completed removal of the principal river obstacles.', 'This recognizes both victories and their order rather than collapsing them into one event.'),
            ('Both strongholds surrendered only after the Confederate national government had ended the war.', 'These surrenders occurred during the ongoing war, not after a national settlement.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess how river control affected military logistics after July 1863?', 0, [
            ('Transport logs and supply correspondence tracing movements, delays, and changed routes before and after the surrenders.', 'These records can test the proposed logistical consequences rather than simply establish that the victories occurred.'),
            ('A commemorative speech describing the victory as glorious without discussing transport.', 'Celebratory language is evidence of commemoration but does not directly measure logistical effects.'),
            ('A list of officers’ ranks at the time of the surrender.', 'Ranks identify command hierarchy but do not establish how supply movements changed.'),
            ('The assumption that control of the river immediately eliminated every Confederate supply route.', 'The loss disrupted connections but did not itself eliminate all other routes; the assumption needs testing.'),
        ]),
    ],
)
