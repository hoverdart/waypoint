"""Original analysis of a public-domain letter, distinct from released AP items."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Influence of Revolutionary Ideals', code='3.6',
    source_url='https://www.battlefields.org/learn/primary-sources/abigail-adams-john-adams-remember-ladies',
    source_kind='primary excerpt',
    stimulus='Abigail Adams to John Adams, March 31, 1776 (letter completed April 5): “Do not put such unlimited power into the hands of the Husbands.”',
    items=[
        ('claims-evidence', 2, 'Adams’s request most directly challenges which relationship?', 2, [
            ('The power of Parliament over colonial merchants.', 'Although the letter was written during the imperial crisis, this sentence specifically addresses husbands’ power.'),
            ('The authority of military commanders over soldiers.', 'The sentence concerns marriage and gendered authority rather than military discipline.'),
            ('The legal and social authority husbands exercised over wives.', 'Adams explicitly asks that husbands not receive unlimited power, challenging a gendered hierarchy.'),
            ('The power of western territories over the original colonies.', 'The excerpt makes no claim about territorial government.'),
        ]),
        ('contextualization', 3, 'Which broader development made this request particularly timely in 1776?', 0, [
            ('Debates over independence created opportunities to question existing laws and political authority.', 'The prospect of creating new governments allowed Adams to urge reconsideration of women’s treatment under law.'),
            ('The Constitution had just established a national amendment process.', 'The Constitution was drafted in 1787, after this letter.'),
            ('The Nineteenth Amendment had extended voting protections to women.', 'The Nineteenth Amendment was ratified in 1920, not during the Revolution.'),
            ('The Civil War had ended and Reconstruction governments were being formed.', 'Reconstruction belongs to the period after the Civil War, nearly a century later.'),
        ]),
        ('sourcing', 3, 'How does the letter’s intended audience help explain the request?', 3, [
            ('Adams was issuing a binding ruling as a colonial judge.', 'This was a private letter, not a judicial decision, and Adams was not acting as a judge.'),
            ('Adams was instructing a British monarch on how to dissolve Parliament.', 'Her addressee was John Adams, not a British monarch, and the request concerns women’s legal position.'),
            ('Adams was reporting election results to a state electoral commission.', 'The letter advocated a change in treatment rather than reporting election returns.'),
            ('Adams addressed a politically influential husband who could participate in shaping new laws.', 'Her personal connection to John Adams offered a channel for urging changes during revolutionary political reconstruction.'),
        ]),
        ('argumentation', 4, 'Which historical claim can this excerpt support without additional evidence about subsequent legislation?', 1, [
            ('Independence immediately secured equal political rights for all women.', 'A request for reform does not establish that equal rights were enacted or enjoyed.'),
            ('At least some women used the revolutionary moment to question male authority.', 'Adams’s request supplies a specific example of a woman challenging a hierarchy during the Revolution.'),
            ('All women agreed on a single program for legal reform.', 'One writer’s request cannot establish agreement among all women.'),
            ('Every state abolished the legal disabilities of married women in 1776.', 'The letter is evidence of advocacy, not proof of enacted changes across all states.'),
        ]),
    ],
)
