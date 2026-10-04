"""Original questions using a public-domain Cherokee petition (NARA 2127291)."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Jackson and Federal Power', code='4.8', set_id='cherokee-petition',
    source_url='https://docsteach.org/document/cherokee-petition-protest-new-echota-treaty/',
    source_kind='primary excerpt',
    stimulus='Cherokee petition against the Treaty of New Echota, 1836, addressed to the U.S. Senate: “the persons who are represented as acting in behalf of the Cherokees in this matter, are wholly unauthorized.” National Archives Identifier 2127291.',
    items=[
        ('claims-evidence', 2, 'The petitioners most directly challenge the treaty on the grounds that', 0, [
            ('its negotiators lacked authority to represent the Cherokee people.', 'The excerpt expressly disputes the negotiators’ authorization to act for the Cherokee people.'),
            ('it had been negotiated by the British Parliament.', 'The dispute concerned an agreement with the United States, not an act of Parliament.'),
            ('it granted universal suffrage to all Americans.', 'The petition concerns representation in treaty making, not universal voting rights.'),
            ('it prohibited all western migration by white settlers.', 'The treaty enabled Cherokee removal and land cession, not a ban on all white migration.'),
        ]),
        ('sourcing', 3, 'Why was the Senate an important audience for this petition?', 2, [
            ('It alone elected the Cherokee national leadership.', 'Cherokee political authority did not derive from Senate elections.'),
            ('It served as the British colonial legislature.', 'The U.S. Senate was a federal institution of the independent United States.'),
            ('Its constitutional role in treaty approval offered a way to oppose the agreement.', 'Petitioners sought to influence a federal institution with authority to give advice and consent to treaties.'),
            ('It had no connection to federal treaty policy.', 'The Senate’s treaty role explains why petitioners appealed to it.'),
        ]),
        ('comparison', 3, 'Compared with Jackson’s emphasis on the benefits of removal to southern states, this petition foregrounds', 1, [
            ('agreement that economic growth overrides all questions of consent.', 'The petition contests representative authority rather than accepting growth as sufficient justification.'),
            ('the authority and consent of the people whose lands and government were affected.', 'The complaint centers on whether the negotiators could legitimately bind the Cherokee people.'),
            ('the need to restore European colonial control.', 'The petition challenges U.S. treaty policy without calling for European rule.'),
            ('unanimous Cherokee support for the treaty.', 'A protest against unauthorized negotiators contradicts a claim of unanimous support.'),
        ]),
        ('argumentation', 4, 'Which conclusion is supported by the petition without assuming that it represents every Cherokee individual?', 3, [
            ('All Cherokee people held identical views on removal.', 'A petition establishes its signers’ position, not unanimity among every member of a nation.'),
            ('Congress rejected the treaty because the petition existed.', 'The existence of opposition does not establish the outcome of federal deliberations.'),
            ('The treaty had no consequences for Cherokee sovereignty.', 'Contesting authority to negotiate indicates sovereignty was at issue; it does not prove an absence of consequences.'),
            ('Cherokee opponents used political appeals to contest the treaty’s legitimacy.', 'The petition itself is direct evidence of organized opposition through an appeal to the Senate.'),
        ]),
    ],
)
