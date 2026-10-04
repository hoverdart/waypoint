"""Original source-analysis questions about unequal suffrage qualifications."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Expanding Democracy', code='4.7', set_id='new-york-suffrage',
    source_url='https://en.wikisource.org/wiki/New_York_Constitution_of_1821',
    source_kind='original instructional summary',
    stimulus='New York’s 1821 constitution, Article II, specified several routes to voting eligibility for adult male citizens, subject to residence requirements, including taxation, militia service, and highway labor. It separately required Black men to meet a $250 net freehold-property qualification, pay tax on that estate, and satisfy a longer citizenship requirement. Women were excluded. This is an original summary of the legal provisions, not a quotation or a claim that all eligible people actually voted.',
    items=[
        ('claims-evidence', 2, 'Which interpretation best accounts for the combination of provisions?', 1, [
            ('Property ownership remained the same prerequisite for every male voter.', 'The general qualifications offered alternatives, while the racial provision imposed a distinct freehold requirement.'),
            ('Routes to participation for white men coexisted with more restrictive racial qualifications.', 'The alternatives and the separate property rule show unequal access within the male electorate.'),
            ('Militia service replaced every other qualification for voting.', 'Militia service was one route, not the exclusive qualification, and other restrictions remained.'),
            ('Tax payment gave women the same electoral eligibility as men.', 'The constitution limited these voting qualifications to male citizens.'),
        ]),
        ('contextualization', 3, 'These provisions most clearly qualify which claim about early nineteenth-century democratization?', 3, [
            ('State governments played a substantial role in determining electoral eligibility.', 'A state constitution defining qualifications supports this claim rather than qualifying it.'),
            ('Military and civic service could be invoked as grounds for political participation.', 'The militia and highway-labor routes support this claim.'),
            ('Economic status influenced access to the ballot.', 'The explicit property rule supports this claim.'),
            ('Expanding political participation meant equal access for adults regardless of race and sex.', 'The race-specific requirement and exclusion of women contradict a universal interpretation of democratization.'),
        ]),
        ('sourcing', 3, 'What can a historian establish most directly from this constitution, without additional records?', 0, [
            ('The formal criteria state officials were supposed to apply when assessing eligibility.', 'A constitutional provision prescribes legal qualifications; implementation requires separate evidence.'),
            ('The percentage of eligible citizens who cast ballots in the next election.', 'Turnout requires election and population records, not only legal qualifications.'),
            ('How frequently local officials ignored the stated qualifications.', 'A prescriptive legal text does not record departures from its rules.'),
            ('The principal motive of each delegate who supported the provision.', 'Individual motives require additional evidence such as speeches or correspondence.'),
        ]),
        ('argumentation', 4, 'Which research design would best test the effect of the separate property requirement on Black political participation?', 2, [
            ('Compare statewide totals for votes cast by all residents before and after the constitution.', 'Aggregate totals do not isolate Black participation or distinguish property restrictions from other changes.'),
            ('Count newspaper editorials endorsing property qualifications during the convention.', 'Editorials illuminate arguments, but do not directly show who could vote or did vote.'),
            ('Link local property assessments, eligibility records, and poll lists before and after implementation, accounting for residence and other rule changes.', 'Linked records can distinguish wealth-based exclusion, eligibility, and actual participation while checking competing explanations.'),
            ('Compare the wording of the suffrage article with the constitution’s provisions on legislative procedure.', 'Textual comparison cannot by itself measure the rule’s effect on the electorate.'),
        ]),
    ],
)
