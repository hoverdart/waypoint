"""Original questions on violent opposition and Reconstruction enforcement."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 5: 1844-1877', topic='Reconstruction', code='5.11', set_id='enforcement-resistance',
    source_url='https://www.senate.gov/artandhistory/history/common/generic/EnforcementActs.htm',
    source_kind='original instructional summary',
    stimulus='During Reconstruction, white supremacist groups used violence and intimidation against Black citizens and their political allies. Congress responded with Enforcement Acts in 1870 and 1871 that expanded federal tools for protecting rights. Federal intervention could suppress organized violence, but lasting protection depended on enforcement as well as constitutional guarantees. This is an original instructional summary.',
    items=[
        ('causation', 2, 'How could intimidation undermine political rights without formally repealing a constitutional amendment?', 2, [
            ('It converted every act of violence into a lawful amendment to the Constitution.', 'Violence could obstruct rights without changing the constitutional text.'),
            ('It made participation in elections mandatory for the targeted citizens.', 'Intimidation sought to deter participation rather than compel the exercise of rights.'),
            ('It could deter voting, officeholding, and political organizing by making participation dangerous.', 'Threats and violence could prevent the effective exercise of formally guaranteed rights.'),
            ('It transferred the power to ratify amendments to local political clubs.', 'Local intimidation did not alter the constitutional amendment procedure.'),
        ]),
        ('contextualization', 3, 'The Enforcement Acts most clearly reflected which approach to Reconstruction?', 0, [
            ('Using national authority to protect rights when violence and local failures threatened their exercise.', 'Federal enforcement addressed obstacles that constitutional declarations or local institutions alone had not overcome.'),
            ('Leaving protection of constitutional rights entirely to private voluntary organizations.', 'The acts expanded governmental enforcement rather than relying entirely on private organizations.'),
            ('Treating the restoration of former Confederate political leaders as sufficient protection for freedpeople.', 'The legislation responded to threats against freedpeople rather than assuming political restoration alone would protect them.'),
            ('Postponing all federal action until states individually requested the repeal of Reconstruction amendments.', 'The acts were enforcement measures, not a process for repealing the amendments.'),
        ]),
        ('argumentation', 4, 'Which evidence would best assess the durability of an enforcement campaign’s effects?', 1, [
            ('The statute’s enactment date treated as proof that local intimidation ceased permanently.', 'Enactment establishes legal authority but does not demonstrate lasting local outcomes.'),
            ('Records of prosecutions, reported violence, and political participation over several years, with attention to reporting conditions.', 'These sources can reveal changes in protection and participation while accounting for underreporting or changing enforcement.'),
            ('A single official announcement of success without subsequent local evidence.', 'An announcement alone cannot establish whether effects persisted.'),
            ('The number of constitutional amendments ratified before the campaign.', 'The number of amendments does not directly measure the campaign’s practical effects.'),
        ]),
    ],
)
