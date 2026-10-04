"""Original questions using a public-domain presidential message."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='America on the World Stage', code='4.4',
    source_url='https://www.archives.gov/milestone-documents/monroe-doctrine', source_kind='primary excerpt',
    stimulus='James Monroe, annual message to Congress, December 2, 1823: “the American continents ... are henceforth not to be considered as subjects for future colonization by any European powers.” Ellipsis indicates omitted words.',
    items=[
        ('claims-evidence', 2, 'The excerpt most directly expresses opposition to', 1, [
            ('all commerce between American and European countries.', 'The passage concerns colonization, not a prohibition on commerce.'),
            ('new European colonial expansion in the Americas.', 'Monroe explicitly rejects future European colonization of the American continents.'),
            ('independence for former Spanish colonies.', 'The message opposed renewed European domination rather than independence.'),
            ('the existence of any government in the Western Hemisphere.', 'The statement concerns external colonization, not the abolition of government.'),
        ]),
        ('contextualization', 3, 'Which development most directly helps explain this declaration?', 3, [
            ('The United States had just entered World War I.', 'American entry into World War I occurred in 1917.'),
            ('The thirteen colonies were negotiating their first declaration of independence.', 'The Declaration dates to 1776, decades before Monroe’s message.'),
            ('European colonial empires had already disappeared worldwide.', 'European empires persisted; concern about their expansion helped motivate the declaration.'),
            ('Newly independent Latin American countries faced the possibility of European intervention.', 'The message addressed the political future of the hemisphere after independence movements challenged European colonial rule.'),
        ]),
        ('sourcing', 3, 'As evidence, the excerpt is most directly useful for studying', 0, [
            ('the position the American president publicly asserted toward European expansion.', 'A presidential message directly records a declared policy position.'),
            ('the unanimous views of every Latin American government.', 'Monroe spoke for his administration, not every government in Latin America.'),
            ('the exact number of American warships ready for combat.', 'The declaration contains no inventory of naval strength.'),
            ('the private motives of every European ruler.', 'A statement by Monroe cannot directly establish all European rulers’ private intentions.'),
        ]),
        ('argumentation', 4, 'Which evidence would be most necessary to evaluate whether the United States could enforce the policy independently in 1823?', 2, [
            ('The length of the printed presidential message.', 'Document length is not a measure of military or diplomatic capacity.'),
            ('A later politician’s repetition of the same sentence.', 'Later repetition does not establish American capabilities in 1823.'),
            ('Contemporary military capabilities and the policies of other major Atlantic powers.', 'Enforcement depended on material capacity and the international balance of power, which a declaration alone cannot demonstrate.'),
            ('A claim that announcing a policy guarantees compliance.', 'This assumes the very outcome that historical evidence must establish.'),
        ]),
    ],
)
