"""Original reform questions based on the public-domain Declaration of Sentiments."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='An Age of Reform', code='4.11', set_id='seneca-falls',
    source_url='https://www.nps.gov/wori/learn/historyculture/declaration-of-sentiments.htm',
    source_kind='primary excerpt',
    stimulus='Declaration of Sentiments, Seneca Falls Convention, 1848: “We hold these truths to be self-evident; that all men and women are created equal”',
    items=[
        ('sourcing', 2, 'The authors’ adaptation of the Declaration of Independence chiefly served to', 1, [
            ('announce renewed allegiance to the British monarchy.', 'The authors invoked an American founding text to demand rights, not allegiance to Britain.'),
            ('ground claims for women’s equality in familiar founding principles.', 'Adding women to the equality claim presented reform as an application of the nation’s stated ideals.'),
            ('reject the idea that people possess natural rights.', 'The equality language invokes rather than rejects natural-rights reasoning.'),
            ('establish a new national tax system.', 'The excerpt argues about equality, not fiscal administration.'),
        ]),
        ('contextualization', 3, 'Which wider development best situates this document in the antebellum era?', 3, [
            ('The disappearance of voluntary reform organizations.', 'Organized reform expanded rather than disappeared in the antebellum era.'),
            ('The immediate enactment of nationwide women’s suffrage in 1848.', 'The convention advocated rights; it did not enact nationwide women’s suffrage.'),
            ('The replacement of all state governments by royal governors.', 'The United States remained a republic with state governments.'),
            ('The growth of organized movements seeking changes in social institutions and individual rights.', 'The convention belonged to a wider era of reform activism, including abolition and other campaigns for social change.'),
        ]),
        ('continuity-and-change', 3, 'Compared with the founding-era assertion of equality, the excerpt illustrates', 0, [
            ('continued use of natural-rights language to challenge an additional form of exclusion.', 'The authors reused revolutionary language while explicitly including women in its claim.'),
            ('the abandonment of rights-based arguments by reformers.', 'Rights-based reasoning is central to the excerpt.'),
            ('proof that founding-era governments had already implemented full gender equality.', 'A demand for equality does not establish that equality had already been achieved.'),
            ('the end of all disagreement about citizenship.', 'The declaration expresses a position within an ongoing dispute, not universal agreement.'),
        ]),
        ('claims-evidence', 4, 'Which additional evidence would most directly help determine how far the declaration’s demands changed women’s legal position?', 2, [
            ('The number of words in the declaration.', 'Length does not demonstrate legal change.'),
            ('A second printing of the same statement.', 'Another printing shows circulation, not implementation.'),
            ('Changes in state property and voting laws, together with evidence of their application.', 'Legal changes and enforcement records connect reform demands to actual institutional outcomes.'),
            ('A claim that signing a declaration automatically changes the law.', 'Advocacy documents do not automatically enact their demands.'),
        ]),
    ],
)
