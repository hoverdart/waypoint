"""Original continuity/change questions based on a public-domain constitutional clause."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Continuity and Change in Period 3', code='3.13',
    source_url='https://www.archives.gov/founding-docs/constitution-transcript', source_kind='primary excerpt',
    stimulus='United States Constitution, 1787, Article I, section 9: “The Migration or Importation of such Persons as any of the States now existing shall think proper to admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight”',
    items=[
        ('contextualization', 2, 'This provision most directly accommodated the interests of those seeking to preserve', 2, [
            ('British authority to appoint American colonial governors.', 'The Constitution organized an independent republic, not a restored British colonial administration.'),
            ('a national ban on all voluntary European immigration.', 'The historical compromise protected the importation of enslaved people from an immediate congressional ban.'),
            ('the importation of enslaved people into states that permitted it.', 'The clause delayed Congress’s ability to prohibit the international slave trade into existing states.'),
            ('universal political participation regardless of legal status.', 'The clause concerns importation and does not grant political rights.'),
        ]),
        ('continuity-and-change', 3, 'Which interpretation best uses this provision to evaluate the effects of the Revolution?', 0, [
            ('Political independence and new institutions coexisted with protections for slavery.', 'The new national framework preserved an important protection for the slave trade, demonstrating continuity alongside political transformation.'),
            ('Independence immediately abolished slavery throughout the United States.', 'The provision’s accommodation of slave importation contradicts a claim of immediate national abolition.'),
            ('The Revolution left every political institution unchanged.', 'A new Constitution itself reflects institutional change; continuity in slavery does not mean all institutions remained unchanged.'),
            ('The Constitution guaranteed equal voting rights to enslaved people.', 'The clause does not confer voting rights or emancipation.'),
        ]),
        ('claims-evidence', 3, 'Which conclusion about 1808 follows from the wording of the clause?', 3, [
            ('Every enslaved person would automatically be emancipated that year.', 'The date concerns the restriction on congressional prohibition of importation, not automatic emancipation.'),
            ('Every state was required to import enslaved people until that year.', 'Permission and protection from a federal ban do not require states to allow importation.'),
            ('The Constitution itself imposed an immediate ban in 1787.', 'The clause explicitly prevented congressional prohibition before 1808.'),
            ('The specified constitutional barrier to a congressional prohibition would no longer apply.', 'The date ends the stated restriction on Congress; it does not itself establish universal freedom or describe enforcement.'),
        ]),
        ('argumentation', 4, 'A historian argues that revolutionary change was uneven. Which additional evidence would best complement this provision?', 1, [
            ('A second transcription of exactly the same clause.', 'A duplicate does not broaden the evidence about differing outcomes.'),
            ('State laws introducing gradual emancipation in some places while slavery persisted elsewhere.', 'Contrasting state developments would show uneven changes within a national framework that continued to accommodate slavery.'),
            ('A list of unrelated European monarchs’ coronation dates.', 'Those dates do not directly address changes in American slavery and freedom.'),
            ('A claim that no change can occur unless every institution changes simultaneously.', 'That assumption prevents rather than supports analysis of uneven historical change.'),
        ]),
    ],
)
