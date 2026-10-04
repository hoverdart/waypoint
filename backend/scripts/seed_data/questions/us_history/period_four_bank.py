"""Original Bank War questions using Jackson's public-domain veto message."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='Jackson and Federal Power', code='4.8', set_id='bank-veto',
    source_url='https://avalon.law.yale.edu/19th_century/ajveto01.asp', source_kind='primary excerpt',
    stimulus='Andrew Jackson, veto of the bill to renew the Bank of the United States charter, July 10, 1832: “It is to be regretted that the rich and powerful too often bend the acts of government to their selfish purposes.”',
    items=[
        ('claims-evidence', 2, 'Jackson frames his opposition to the Bank chiefly as resistance to', 0, [
            ('government privileges benefiting powerful economic interests.', 'The statement portrays government action as vulnerable to manipulation by the wealthy.'),
            ('the complete absence of private wealth in the United States.', 'Jackson criticizes the influence of existing wealth rather than claiming it does not exist.'),
            ('the constitutional requirement that all banks be owned by Congress.', 'The Constitution contains no such requirement, and the excerpt concerns privilege.'),
            ('a British order requiring Americans to pay colonial taxes.', 'The Bank War concerned a U.S. institution after independence, not colonial taxation.'),
        ]),
        ('contextualization', 3, 'Which conflict provides the immediate context for this statement?', 2, [
            ('The debate over ratification of the Constitution in 1787–1788.', 'The statement dates to the later controversy over renewing the Second Bank’s charter.'),
            ('The establishment of the Federal Reserve in 1913.', 'The Federal Reserve was created decades after Jackson’s presidency.'),
            ('A dispute over renewing the charter of the Second Bank of the United States.', 'Jackson used the veto message to justify rejecting the recharter bill.'),
            ('The decision to finance the American Revolution through a French alliance.', 'Revolutionary financing preceded this nineteenth-century banking dispute.'),
        ]),
        ('sourcing', 3, 'How does the document’s purpose shape its usefulness to historians?', 1, [
            ('It provides a neutral audit of every Bank transaction.', 'A veto message is a political justification, not a comprehensive financial audit.'),
            ('It reveals how Jackson justified his veto and appealed to opponents of concentrated privilege.', 'The language shows the public argument used to defend executive action.'),
            ('It proves that every voter opposed the Bank.', 'A president’s argument cannot establish unanimous public agreement.'),
            ('It records the private views of every Bank shareholder.', 'Jackson was not documenting each shareholder’s private views.'),
        ]),
        ('argumentation', 4, 'Which evidence would most directly help assess an opponent’s claim that the Bank War expanded presidential power?', 3, [
            ('The number of times the word rich appears in this sentence.', 'Word frequency does not establish institutional changes in executive authority.'),
            ('A map of European borders in 1815.', 'European borders do not directly establish how Jackson exercised domestic executive powers.'),
            ('A list of unrelated state holidays.', 'State holidays provide no relevant evidence about the Bank War’s institutional effects.'),
            ('Records of Jackson’s veto, his administration’s deposit policy, and congressional objections.', 'These records allow comparison of executive actions and legislative challenges over control of federal policy.'),
        ]),
    ],
)
