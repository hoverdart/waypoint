"""Foundation curriculum; comprehensive topic expansion remains in progress.

Weights checked against the official course page on 2026-10-04:
https://apcentral.collegeboard.org/courses/ap-united-states-history
"""
UNITS = [
    {
        "name": "Period 1: 1491-1607",
        "description": "Native American societies before European contact and the earliest patterns of European exploration and colonization in the Americas.",
        "ap_weight_min": 4.0,
        "ap_weight_max": 6.0,
        "display_order": 1,
        "topics": [
            {
                "name": "Native American Societies Before European Contact",
                "description": "The diversity and complexity of Native American societies across North America prior to 1492.",
                "skill_tags": ["contextualization"],
                "display_order": 1,
            },
            {
                "name": "European Exploration in the Americas",
                "description": "The motivations and technological developments that enabled European exploration and conquest.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "Columbian Exchange",
                "description": "The exchange of plants, animals, diseases, and ideas between the Old and New Worlds.",
                "skill_tags": ["comparison"],
                "display_order": 3,
            },
            {
                "name": "Labor, Slavery, and Caste in the Spanish Colonial System",
                "description": "The development of forced labor systems, including encomienda and early African slavery, in Spanish America.",
                "skill_tags": ["causation"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 2: 1607-1754",
        "description": "The founding and development of English, French, Dutch, and Spanish colonies, and the emergence of distinct regional colonial societies.",
        "ap_weight_min": 6.0,
        "ap_weight_max": 8.0,
        "display_order": 2,
        "topics": [
            {
                "name": "Europe and the Colonies: Political and Economic Rivalries",
                "description": "Competition among European powers for colonial territory, trade, and resources.",
                "skill_tags": ["comparison"],
                "display_order": 1,
            },
            {
                "name": "The English Colonies: Regional Development",
                "description": "The distinct economic and social development of the New England, Middle, and Southern colonies.",
                "skill_tags": ["comparison"],
                "display_order": 2,
            },
            {
                "name": "Transatlantic Trade and the Expansion of Slavery",
                "description": "The growth of the Atlantic slave trade and the entrenchment of chattel slavery in colonial economies.",
                "skill_tags": ["causation"],
                "display_order": 3,
            },
            {
                "name": "Interactions Between American Indians and Europeans",
                "description": "Patterns of cooperation, conflict, and cultural exchange between colonists and Native peoples.",
                "skill_tags": ["contextualization"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 3: 1754-1800",
        "description": "The causes and consequences of the American Revolution and the challenges of creating and ratifying a new national government.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 3,
        "topics": [
            {
                "name": "The Seven Years' War (French and Indian War)",
                "description": "The causes and imperial consequences of the war between Britain and France in North America.",
                "skill_tags": ["causation"],
                "display_order": 1,
            },
            {
                "name": "Taxation Without Representation and the Road to Revolution",
                "description": "British imperial policy after 1763 and colonial resistance leading to the Revolutionary War.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "The American Revolution's Effects",
                "description": "The social, political, and economic effects of the Revolution on different groups in American society.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 3,
            },
            {
                "name": "The Articles of Confederation and the Constitution",
                "description": "The weaknesses of the Articles of Confederation and the debates over ratifying the Constitution.",
                "skill_tags": ["comparison"],
                "display_order": 4,
            },
            {
                "name": "Washington, Hamilton, and the New Government",
                "description": "The establishment of federal authority and the emergence of the first political party divisions.",
                "skill_tags": ["causation"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Period 4: 1800-1848",
        "description": "The growth of American democracy, market and transportation revolutions, westward expansion, and the rise of sectional tension.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 4,
        "topics": [
            {
                "name": "The Rise of Political Parties and Democracy",
                "description": "The expansion of suffrage and the development of the second party system.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 1,
            },
            {
                "name": "Markets and Westward Expansion",
                "description": "The market revolution, transportation improvements, and territorial expansion west of the Appalachians.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "The Cotton Revolution and the Expansion of Slavery",
                "description": "The growth of the cotton economy and its effects on the expansion and entrenchment of slavery.",
                "skill_tags": ["causation"],
                "display_order": 3,
            },
            {
                "name": "Religious Revival and Reform Movements",
                "description": "The Second Great Awakening and reform movements including abolition, temperance, and women's rights.",
                "skill_tags": ["contextualization"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 5: 1844-1877",
        "description": "The intensification of sectional conflict over slavery, the Civil War, and the political and social transformations of Reconstruction.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 5,
        "topics": [
            {
                "name": "Manifest Destiny and Continued Expansion",
                "description": "Territorial expansion to the Pacific and the resulting conflicts with Mexico and Native nations.",
                "skill_tags": ["causation"],
                "display_order": 1,
            },
            {
                "name": "The Compromise of 1850 and Escalating Sectional Conflict",
                "description": "Political attempts to manage the expansion of slavery into new territories and their failure.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "The Civil War",
                "description": "The causes, key turning points, and course of the Civil War.",
                "skill_tags": ["causation"],
                "display_order": 3,
            },
            {
                "name": "Reconstruction",
                "description": "Competing plans for Reconstruction and their effects on the status of formerly enslaved people and the South.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 6: 1865-1898",
        "description": "The Gilded Age transformation of the United States through industrialization, urbanization, immigration, and the closing of the frontier.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 6,
        "topics": [
            {
                "name": "Industrialization and Big Business",
                "description": "The rise of large-scale industry, corporate consolidation, and new business practices after the Civil War.",
                "skill_tags": ["causation"],
                "display_order": 1,
            },
            {
                "name": "Immigration and Urbanization",
                "description": "The causes and effects of new immigration patterns and rapid urban growth.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "Labor and the Rise of Unions",
                "description": "Working-class responses to industrial capitalism, including strikes and the growth of labor organizations.",
                "skill_tags": ["contextualization"],
                "display_order": 3,
            },
            {
                "name": "The Western Frontier and Native American Displacement",
                "description": "Western settlement, farming and ranching economies, and U.S. policy toward Native Americans.",
                "skill_tags": ["causation"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 7: 1890-1945",
        "description": "The Progressive Era, American emergence as a world power, the Great Depression and New Deal, and World War II.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 7,
        "topics": [
            {
                "name": "The Progressive Movement",
                "description": "Reform efforts targeting political corruption, corporate power, and social ills in the early twentieth century.",
                "skill_tags": ["contextualization"],
                "display_order": 1,
            },
            {
                "name": "American Imperialism and World War I",
                "description": "The expansion of U.S. influence abroad and American involvement in the First World War.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "The Great Depression and the New Deal",
                "description": "The causes of the Great Depression and the federal government's expanded role under the New Deal.",
                "skill_tags": ["causation"],
                "display_order": 3,
            },
            {
                "name": "World War II",
                "description": "U.S. entry into and mobilization for World War II and its effects on American society.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 8: 1945-1980",
        "description": "The Cold War, postwar economic and social change, the civil rights movement, and the liberal-conservative political struggles of the 1960s-70s.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 17.0,
        "display_order": 8,
        "topics": [
            {
                "name": "The Cold War and Containment",
                "description": "The origins of the Cold War and the development of U.S. containment policy.",
                "skill_tags": ["causation"],
                "display_order": 1,
            },
            {
                "name": "Postwar Prosperity and Suburbanization",
                "description": "Economic growth, consumerism, and demographic shifts to the suburbs after World War II.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 2,
            },
            {
                "name": "The Civil Rights Movement",
                "description": "The strategies, successes, and limits of the movement for African American civil rights.",
                "skill_tags": ["causation"],
                "display_order": 3,
            },
            {
                "name": "The Vietnam War and Social Movements of the 1960s-70s",
                "description": "The escalation and consequences of the Vietnam War alongside the rise of new social and political movements.",
                "skill_tags": ["causation"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Period 9: 1980-Present",
        "description": "The conservative resurgence, the end of the Cold War, and the economic, technological, and demographic changes of the contemporary era.",
        "ap_weight_min": 4.0,
        "ap_weight_max": 6.0,
        "display_order": 9,
        "topics": [
            {
                "name": "The Reagan Revolution and Conservative Resurgence",
                "description": "The rise of modern conservatism and its effects on domestic and economic policy.",
                "skill_tags": ["contextualization"],
                "display_order": 1,
            },
            {
                "name": "The End of the Cold War",
                "description": "The diplomatic and political developments that led to the collapse of the Soviet Union.",
                "skill_tags": ["causation"],
                "display_order": 2,
            },
            {
                "name": "Globalization and the Technological Revolution",
                "description": "The economic and social effects of globalization, deindustrialization, and new information technology.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 3,
            },
            {
                "name": "Demographic and Cultural Change Since 1980",
                "description": "Changing immigration patterns, cultural debates, and political polarization in contemporary America.",
                "skill_tags": ["continuity-and-change"],
                "display_order": 4,
            },
        ],
    },
]

# Preserve existing topic names/IDs while aligning the first period to CED 1.1–1.7.
_period_one_existing = {topic['name']: topic for topic in UNITS[0]['topics']}
_period_one_sequence = [
    ('1.1', 'Contextualizing Period 1', 'Situate contact within diverse Indigenous societies and expanding Atlantic connections.', 'contextualization'),
    ('1.2', 'Native American Societies Before European Contact', None, 'comparison'),
    ('1.3', 'European Exploration in the Americas', None, 'causation'),
    ('1.4', 'Columbian Exchange', None, 'causation'),
    ('1.5', 'Labor, Slavery, and Caste in the Spanish Colonial System', None, 'comparison'),
    ('1.6', 'Cultural Interactions Before 1607', 'Analyze negotiation, coercion, and differing perspectives in early colonial encounters.', 'sourcing'),
    ('1.7', 'Causation in Period 1', 'Explain interacting causes and consequences of transatlantic contact.', 'causation'),
]
UNITS[0]['topics'] = []
for _order, (_code, _name, _description, _skill) in enumerate(_period_one_sequence, start=1):
    _topic = dict(_period_one_existing.get(_name, {'name': _name, 'description': _description}))
    _topic['display_order'] = _order
    _topic['skill_tags'] = list(dict.fromkeys([*_topic.get('skill_tags', []), _skill, f'ced:{_code}']))
    UNITS[0]['topics'].append(_topic)

_period_two_existing = {topic['name']: topic for topic in UNITS[1]['topics']}
_period_two_sequence = [
    ('Contextualizing Period 2', 'Place colonial development within Atlantic migration, imperial goals, and Indigenous societies.', 'contextualization'),
    ('Europe and the Colonies: Political and Economic Rivalries', None, 'comparison'),
    ('The English Colonies: Regional Development', None, 'comparison'),
    ('Transatlantic Trade and the Expansion of Slavery', None, 'causation'),
    ('Interactions Between American Indians and Europeans', None, 'sourcing'),
    ('Slavery in the British Colonies', 'Analyze racialized hereditary slavery, colonial law, and enslaved people’s experiences and resistance.', 'causation'),
    ('Colonial Society and Culture', 'Examine religious change, intellectual exchange, and social institutions in the colonies.', 'contextualization'),
    ('Comparison in Period 2', 'Compare colonial institutions using specific evidence and qualified claims.', 'comparison'),
]
UNITS[1]['topics'] = []
for _order, (_name, _description, _skill) in enumerate(_period_two_sequence, start=1):
    _topic = dict(_period_two_existing.get(_name, {'name': _name, 'description': _description}))
    _topic['display_order'] = _order
    _topic['skill_tags'] = list(dict.fromkeys([*_topic.get('skill_tags', []), _skill, f'ced:2.{_order}']))
    UNITS[1]['topics'].append(_topic)

# Period 3 expansion is incremental; retain the combined legacy topic until its
# existing questions and mastery records can be mapped without discarding IDs.
UNITS[2]['topics'] += [
    {'name': 'Political Ideas of the Revolution', 'description': 'Analyze rights, consent, and arguments justifying independence.',
     'skill_tags': ['sourcing', 'claims-evidence', 'ced:3.4'], 'display_order': 6},
    {'name': 'Constitutional Structure and Federal Power', 'description': 'Explain constitutional institutions, federalism, and the limits of using legal texts as evidence of practice.',
     'skill_tags': ['comparison', 'claims-evidence', 'ced:3.9'], 'display_order': 7},
]

UNITS[2]['topics'].append({
    'name': 'Movement in the Early Republic',
    'description': 'Analyze territorial government, western migration, and competing claims to land and political authority.',
    'skill_tags': ['contextualization', 'sourcing', 'ced:3.12'], 'display_order': 8,
})
