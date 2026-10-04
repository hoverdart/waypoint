"""Original questions using Washington's public-domain farewell text."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Developing an American Identity', code='3.11',
    source_url='https://www.senate.gov/artandhistory/history/resources/pdf/Washingtons_Farewell_Address.pdf',
    source_kind='primary excerpt',
    stimulus='George Washington, Farewell Address, published September 1796 (Senate transcription, spelling and punctuation modernized): “The name of American, which belongs to you, in your national capacity, must always exalt the just pride of patriotism more than any appellation derived from local discriminations.”',
    items=[
        ('claims-evidence', 2, 'Washington’s statement most directly encourages Americans to', 1, [
            ('replace the Union with independent regional republics.', 'Washington promotes attachment to the nation rather than its dissolution into regions.'),
            ('place national belonging above local divisions.', 'He explicitly ranks the national designation American above identities derived from local distinctions.'),
            ('abandon representative government for hereditary monarchy.', 'The statement addresses political identity, not the establishment of monarchy.'),
            ('give foreign governments control over domestic political debates.', 'National patriotism does not imply surrendering domestic authority to foreign powers.'),
        ]),
        ('contextualization', 3, 'Which development in the 1790s helps explain Washington’s emphasis?', 3, [
            ('The Confederate states had formally seceded from the Union.', 'Confederate secession occurred in 1860–1861, not during Washington’s presidency.'),
            ('The original colonies still lacked independence from Britain.', 'Independence had been secured before the 1790s.'),
            ('The federal government had permanently eliminated political disagreement.', 'Disputes over finance and foreign policy divided Americans in the 1790s.'),
            ('Disputes over federal policies and foreign affairs were strengthening rival political alignments.', 'Emerging party divisions made appeals to common national interests especially relevant.'),
        ]),
        ('sourcing', 3, 'Which feature of the source most affects how a historian should interpret its claim about national identity?', 0, [
            ('A departing president was seeking to shape the public’s political loyalties.', 'The address is persuasive advice from a political leader, so it reveals the identity he sought to encourage rather than measuring everyone’s loyalties.'),
            ('It records a confidential statistical survey of every American household.', 'The address is a public political text, not a household survey.'),
            ('It is a judicial ruling that legally prohibited regional identities.', 'Washington’s advice was not a judicial decision or a legal ban on regional attachments.'),
            ('It was written by a British official seeking colonial obedience.', 'Washington was the American president, not a British colonial official.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly complicate a claim that Americans had already adopted the hierarchy of loyalties Washington recommended?', 2, [
            ('A record showing that the address appeared in newspapers.', 'Publication establishes circulation, not whether readers prioritized national loyalties.'),
            ('A copy of the passage in Washington’s papers.', 'A surviving copy confirms his statement but does not test public acceptance.'),
            ('Regional political writings defending local interests even when they conflicted with national policies.', 'Such writings would show that local loyalties could compete with the national priority Washington advocated.'),
            ('A calendar identifying the date Washington left office.', 'The end of his term does not establish how Americans ranked political identities.'),
        ]),
    ],
)
