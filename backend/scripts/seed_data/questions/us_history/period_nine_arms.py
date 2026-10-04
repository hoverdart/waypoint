"""Original late Cold War questions on negotiated reductions and verification."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 9: 1980-Present', topic='The End of the Cold War', code='9.3', set_id='inf-verification',
    source_url='https://www.reaganlibrary.gov/archives/speech/white-house-statement-first-anniversary-intermediate-range-nuclear-forces-treaty',
    source_kind='original instructional summary',
    stimulus='Reagan and Gorbachev signed the INF Treaty in December 1987. It required elimination of a defined class of American and Soviet missiles and included data exchanges and on-site inspections. A White House anniversary statement emphasized these provisions as achievements. This is an original instructional summary of the agreement and the administration’s presentation of it, not a claim that all nuclear weapons were eliminated.',
    items=[
        ('causation', 2, 'What problem did data exchanges and inspections most directly address?', 1, [
            ('The need to replace negotiations with a unilateral public announcement.', 'Verification supported a negotiated agreement rather than replacing negotiation.'),
            ('Uncertainty about whether the other party was fulfilling its commitments.', 'Information and inspection mechanisms could help detect noncompliance rather than relying only on assurances.'),
            ('The absence of any distinction between conventional forces and nuclear arms.', 'The mechanisms concerned compliance with defined treaty obligations, not erasing categories of weapons.'),
            ('The requirement that each party surrender all authority over its domestic government.', 'Verification provisions did not transfer general governing authority.'),
        ]),
        ('sourcing', 3, 'How should a historian use the White House anniversary statement?', 2, [
            ('As conclusive evidence that Soviet leaders shared every American interpretation.', 'An American administration’s statement cannot establish the entire Soviet perspective.'),
            ('As evidence that can be dismissed entirely because it promotes a policy achievement.', 'A promotional purpose shapes interpretation but does not make the document useless.'),
            ('As evidence of how the administration presented the agreement, checked against treaty provisions and implementation records.', 'This preserves the source’s value while distinguishing public presentation from independent verification.'),
            ('As proof that the agreement had already ended every international security dispute.', 'The statement’s celebration does not establish such a sweeping outcome.'),
        ]),
        ('argumentation', 4, 'Which conclusion about the Cold War is most directly supported by the treaty described?', 0, [
            ('Negotiated reductions and reciprocal verification became possible between continuing strategic rivals.', 'The agreement shows cooperation on defined arms commitments without proving that every rivalry had ended.'),
            ('The treaty alone caused the Soviet Union’s dissolution.', 'The described provisions cannot establish a single-cause explanation for a later political collapse.'),
            ('All nuclear arsenals were eliminated when the leaders signed.', 'The treaty concerned a defined class of missiles, with implementation obligations rather than instantaneous universal abolition.'),
            ('Military competition prevented any diplomatic agreement during the 1980s.', 'The treaty itself contradicts the claim that agreement was impossible.'),
        ]),
    ],
)
