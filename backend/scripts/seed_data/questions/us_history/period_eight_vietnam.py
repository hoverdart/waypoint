"""Original Vietnam escalation and evidence-analysis practice."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Vietnam War and Social Movements of the 1960s-70s', code='8.8', set_id='tonkin-authority',
    source_url='https://www.archives.gov/milestone-documents/tonkin-gulf-resolution',
    source_kind='original instructional summary',
    stimulus='In August 1964, Congress passed the Tonkin Gulf Resolution, granting broad support for presidential military action in Southeast Asia. Johnson and Nixon relied on it in conducting the Vietnam War. Later evidence challenged the reported August 4 naval attack, though an August 2 attack had occurred. Congress repealed the resolution in 1971 amid growing controversy. This is an original instructional summary.',
    items=[
        ('causation', 2, 'How did the resolution contribute to escalation?', 1, [
            ('It required Congress to approve a separate declaration before every military operation.', 'The resolution instead supplied broad authority on which presidents relied.'),
            ('It provided congressional backing that presidents used to justify expanded military action.', 'The authorization linked legislative support with executive decisions about the war.'),
            ('It immediately ended American commitments in Southeast Asia.', 'It supported action rather than terminating involvement.'),
            ('It transferred operational command from the president to individual senators.', 'Congress authorized action without taking over operational command.'),
        ]),
        ('sourcing', 3, 'What is the strongest reason to compare the resolution’s account of attacks with operational records?', 2, [
            ('Legislative documents cannot reveal policymakers’ stated reasons.', 'They can reveal stated justifications, even when the underlying claims need corroboration.'),
            ('Operational records always supply complete and error-free descriptions.', 'Operational reports can also contain uncertainty and require comparison.'),
            ('A policy document can establish the justification offered without independently proving every event asserted.', 'Corroboration separates the stated basis for action from what the evidence establishes happened.'),
            ('Later evidence necessarily proves that neither reported incident occurred.', 'The summary distinguishes the confirmed August 2 attack from the disputed August 4 report.'),
        ]),
        ('argumentation', 4, 'Which interpretation best connects the initial resolution and its later repeal?', 0, [
            ('Congressional support for broad executive action could change as the war and its justification became more contested.', 'The two actions show a changing legislative response rather than an unchanging delegation.'),
            ('The repeal establishes that Congress had opposed the resolution unanimously in 1964.', 'A later reversal does not establish initial opposition.'),
            ('The initial resolution permanently removed Congress from debates over military policy.', 'Congress’s later repeal contradicts the claim of permanent removal.'),
            ('Repeal alone demonstrates that every military operation stopped immediately in 1971.', 'Ending this authorization does not by itself establish the timing of all operations or withdrawal.'),
        ]),
    ],
)
