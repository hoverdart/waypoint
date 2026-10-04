"""Original conservative economic-policy sourcing practice."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 9: 1980-Present', topic='The Reagan Revolution and Conservative Resurgence', code='9.2', set_id='recovery-proposal',
    source_url='https://www.reaganlibrary.gov/archives/speech/white-house-report-program-economic-recovery',
    source_kind='original instructional summary',
    stimulus='A February 1981 White House report proposed slower growth of federal spending, lower tax rates, regulatory relief, and a compatible monetary policy by the independent Federal Reserve. It argued that changing incentives would encourage private investment and production. These were the administration’s proposals and predicted effects, not a retrospective measurement of results. This is an original instructional summary.',
    items=[
        ('contextualization', 2, 'Which policy rationale is most clearly expressed in the report?', 1, [
            ('Public ownership of major industries would replace private investment.', 'The proposal emphasized private incentives rather than general nationalization.'),
            ('Reducing selected government burdens could encourage private economic activity.', 'Lower tax rates and regulatory relief were justified in terms of incentives for investment and production.'),
            ('Federal spending should increase at a faster rate in every program.', 'The report proposed restraining spending growth, not accelerating it across programs.'),
            ('Monetary policy should be set directly by the president without an independent central bank.', 'The report explicitly referred to the independent Federal Reserve.'),
        ]),
        ('sourcing', 3, 'What is the report best suited to establish on its own?', 2, [
            ('The exact change in household incomes during the entire decade.', 'A proposal cannot establish later measured income outcomes.'),
            ('The views of every member of the conservative coalition.', 'An administration report does not represent every supporter’s position.'),
            ('The administration’s proposed mechanisms and public justification for its program.', 'Its timing and purpose make it direct evidence of the program advocated in 1981.'),
            ('That every proposed measure was enacted without congressional revision.', 'A proposal does not establish the final legislative outcome.'),
        ]),
        ('argumentation', 4, 'Which evidence would best test whether the proposed tax changes increased investment as predicted?', 0, [
            ('Enacted tax provisions and investment trends, assessed alongside interest rates, demand, and other economic changes.', 'Testing the mechanism requires actual policy and outcomes while considering competing influences.'),
            ('The report’s prediction repeated in later campaign materials.', 'Repetition of a prediction is not independent evidence of its effects.'),
            ('A count of voters supporting Reagan without investment data.', 'Political support does not measure the economic mechanism.'),
            ('The date the report was released, assumed to be the date all proposals took effect.', 'Release, enactment, implementation, and outcomes are distinct events.'),
        ]),
    ],
)
