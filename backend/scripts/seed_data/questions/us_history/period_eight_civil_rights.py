"""Original civil-rights practice on constitutional rights and enforcement."""
from .builders import source_set

TOPIC = 'The Civil Rights Movement'
QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic=TOPIC, code='8.6', set_id='brown-schools',
    source_url='https://www.archives.gov/milestone-documents/brown-v-board-of-education',
    source_kind='original instructional summary',
    stimulus='In Brown v. Board of Education (1954), the Supreme Court held state-sanctioned racial segregation in public schools unconstitutional under the Fourteenth Amendment. The decision challenged the application of separate-but-equal reasoning to public education. Resistance and disputes over implementation continued after the ruling. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'Which constitutional principle supplied the central basis for the decision described?', 1, [
            ('Congressional authority to negotiate trade agreements.', 'Trade authority does not explain the constitutional challenge to racial segregation in schools.'),
            ('Equal protection against discriminatory state action.', 'The Fourteenth Amendment constrained state-sanctioned racial separation in public education.'),
            ('Executive authority to enter military alliances.', 'Foreign military commitments were not the constitutional basis for the ruling.'),
            ('State discretion to override federal constitutional protections.', 'The decision applied a federal constitutional limit to state policy.'),
        ]),
        ('comparison', 3, 'Which distinction is most important when comparing the ruling with subsequent school enrollment patterns?', 2, [
            ('A judicial ruling records only popular opinion, while enrollment records establish constitutional meaning.', 'A ruling establishes a legal judgment; enrollment records measure conditions rather than define the Constitution.'),
            ('The ruling and local enrollment records necessarily describe the same change at the same speed.', 'Resistance and implementation disputes could produce a gap between law and local practice.'),
            ('The ruling changed the legal standard, while enrollment records can reveal the pace and extent of implementation.', 'Legal change and institutional outcomes require different evidence and may follow different timelines.'),
            ('Enrollment records are irrelevant once a constitutional ruling has been issued.', 'Such records are important for evaluating whether institutions changed in practice.'),
        ]),
        ('argumentation', 4, 'Which evidence most directly qualifies a claim that Brown immediately ended segregated schooling everywhere?', 0, [
            ('District records showing continued racial separation alongside litigation over compliance after 1954.', 'Continued separation and compliance disputes challenge a claim of immediate universal implementation.'),
            ('The unanimous vote of the justices in the 1954 decision.', 'Unanimity describes the Court’s agreement, not nationwide implementation.'),
            ('The decision’s reliance on the Fourteenth Amendment.', 'The constitutional basis does not establish the speed of local change.'),
            ('The existence of plaintiffs challenging school segregation before the decision.', 'Earlier litigation explains the case’s context but does not directly measure post-decision compliance.'),
        ]),
    ],
)
QUESTIONS += source_set(
    period='Period 8: 1945-1980', topic=TOPIC, code='8.10', set_id='voting-enforcement',
    source_url='https://www.archives.gov/milestone-documents/voting-rights-act',
    source_kind='original instructional summary',
    stimulus='The Voting Rights Act of 1965 sought to enforce the Fifteenth Amendment against discriminatory practices that obstructed Black voting. Organizers seeking registration faced intimidation, economic retaliation, and violence as well as administrative barriers. The law expanded federal enforcement rather than creating the constitutional prohibition on racial discrimination in voting for the first time. This is an original instructional summary of the 1965 context.',
    items=[
        ('causation', 2, 'Why was additional legislation sought despite the Fifteenth Amendment?', 3, [
            ('The amendment had been ratified only after 1965.', 'The amendment dated to Reconstruction, long before the act.'),
            ('The amendment expressly required discriminatory literacy tests.', 'The amendment prohibited racial discrimination; discriminatory tests obstructed its promise.'),
            ('Federal constitutional protections applied only to presidential candidates.', 'The protection concerned voting rights, not only qualifications of presidential candidates.'),
            ('A constitutional protection could remain ineffective where discriminatory practices obstructed its exercise.', 'The act addressed the gap between formal protection and access in practice.'),
        ]),
        ('comparison', 3, 'How did registration organizing and federal enforcement serve different but connected roles?', 0, [
            ('Organizing mobilized voters and exposed barriers; enforcement could challenge discriminatory official practices.', 'Collective action and federal intervention could reinforce one another without being identical strategies.'),
            ('Organizing determined constitutional meaning, while courts could only distribute campaign literature.', 'This reverses and misstates the functions of organizers and courts.'),
            ('Federal enforcement required that local organizing stop before rights could be protected.', 'The described connection does not impose such a condition.'),
            ('Registration organizing concerned only economic wages, while federal enforcement concerned only school curricula.', 'Both activities in this context addressed access to voting.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess the act’s effects on access rather than merely its enactment?', 2, [
            ('The date of the signing ceremony and the number of pens used.', 'Ceremonial details do not measure voting access.'),
            ('A national population total with no information about registration.', 'Population totals alone do not measure changes in access to voting.'),
            ('Registration and turnout by race and locality before and after enforcement, considered with reports of remaining barriers.', 'These records test practical change and its limits across affected communities.'),
            ('The original text of the Fifteenth Amendment treated as a complete account of conditions in 1965.', 'A constitutional text does not by itself establish later lived conditions or enforcement outcomes.'),
        ]),
    ],
)
