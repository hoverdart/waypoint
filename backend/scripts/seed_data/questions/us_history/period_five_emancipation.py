"""Original questions using public-domain presidential language."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Government Policies During the Civil War', code='5.9', set_id='emancipation',
    source_url='https://www.archives.gov/milestone-documents/emancipation-proclamation',
    source_kind='primary excerpt',
    stimulus='Abraham Lincoln, Emancipation Proclamation, January 1, 1863: “as a fit and necessary war measure for suppressing said rebellion”. Context: The proclamation declared enslaved people free in designated rebellious states and parts of states, exempted specified areas, and authorized receiving Black men into United States armed service.',
    items=[
        ('sourcing', 2, 'The quoted phrase most directly identifies which justification for presidential action?', 2, [
            ('A constitutional amendment already ratified by the states.', 'The quoted justification invokes wartime authority, not a ratified amendment.'),
            ('A peacetime agreement negotiated with Confederate state legislatures.', 'The measure was directed against rebellion rather than based on such an agreement.'),
            ('Military necessity in the exercise of wartime executive authority.', 'Lincoln explicitly framed the action as a measure for suppressing rebellion.'),
            ('A Supreme Court ruling requiring identical emancipation policies in every state.', 'The proclamation’s justification and territorial distinctions do not describe such a ruling.'),
        ]),
        ('claims-evidence', 3, 'Which interpretation best accounts for the proclamation’s designated areas and exemptions?', 0, [
            ('Its immediate legal scope was narrower than nationwide abolition, despite its major effect on Union war policy.', 'The designated areas and exemptions limited its scope while emancipation became part of the Union war effort.'),
            ('It ended slavery throughout every loyal border state on the date of issuance.', 'Loyal border states were outside the proclamation’s designated rebellious areas.'),
            ('It applied only to people who had already enlisted in the Union Army.', 'The emancipation declaration was geographically defined, not restricted to enlisted people.'),
            ('It guaranteed immediate enforcement in every place still controlled by Confederate forces.', 'A declaration could not guarantee immediate enforcement where federal power had not reached.'),
        ]),
        ('causation', 3, 'How could the military-service provision reinforce the proclamation’s stated purpose?', 3, [
            ('It made Confederate approval a prerequisite for Union recruitment.', 'The provision did not give Confederate authorities control over Union recruitment.'),
            ('It replaced the need for military victory with automatic recognition by Confederate courts.', 'The proclamation did not secure such recognition or eliminate military resistance.'),
            ('It guaranteed identical treatment and pay for all soldiers at once.', 'Authorization of service did not itself remove racial discrimination in military treatment.'),
            ('It enabled Black recruits to contribute directly to the military effort against the Confederacy.', 'Black military service strengthened the Union effort and connected emancipation with suppressing rebellion.'),
        ]),
        ('argumentation', 4, 'Which evidence would best help assess how emancipation became effective in a particular locality?', 1, [
            ('The proclamation’s title and date without records from the locality.', 'These establish the policy’s issuance, not local implementation.'),
            ('Accounts by formerly enslaved residents compared with military reports documenting arrival, recruitment, and enforcement.', 'These sources connect people’s actions and experiences with changes in military control and enforcement.'),
            ('An assumption that the date of the proclamation was the date every enslaved person learned of it.', 'Information and enforcement varied; the assumption needs evidence.'),
            ('A national count of printed copies treated as a measure of individual freedom.', 'Distribution totals do not establish local knowledge, control, or lived freedom.'),
        ]),
    ],
)
