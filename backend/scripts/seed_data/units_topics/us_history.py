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

UNITS[2]['topics'] += [
    {'name': 'Government Under the Articles of Confederation',
     'description': 'Explain confederation institutions, fiscal limitations, and debates about state sovereignty.',
     'skill_tags': ['causation', 'comparison', 'ced:3.7'], 'display_order': 9},
    {'name': 'Constitutional Convention and Ratification',
     'description': 'Analyze constitutional compromises, competing arguments over ratification, and demands for a bill of rights.',
     'skill_tags': ['argumentation', 'sourcing', 'ced:3.8'], 'display_order': 10},
]

UNITS[2]['topics'].append({
    'name': 'Influence of Revolutionary Ideals',
    'description': 'Evaluate how revolutionary ideals inspired challenges to social hierarchies and the limits of resulting changes.',
    'skill_tags': ['argumentation', 'contextualization', 'ced:3.6'], 'display_order': 11,
})

UNITS[2]['topics'].append({
    'name': 'Developing an American Identity',
    'description': 'Analyze national belonging, regional attachments, and competing visions of the republic.',
    'skill_tags': ['sourcing', 'argumentation', 'ced:3.11'], 'display_order': 12,
})

UNITS[2]['topics'].append({
    'name': 'Contextualizing Period 3',
    'description': 'Situate the imperial crisis and early republic within changing Atlantic power relationships.',
    'skill_tags': ['contextualization', 'causation', 'ced:3.1'], 'display_order': 13,
})

UNITS[2]['topics'].append({
    'name': 'Continuity and Change in Period 3',
    'description': 'Develop qualified arguments about political transformation and persistent social hierarchies from 1754 to 1800.',
    'skill_tags': ['continuity-and-change', 'argumentation', 'ced:3.13'], 'display_order': 14,
})

UNITS[2]['topics'].append({
    'name': 'The American Revolutionary War',
    'description': 'Explain military and diplomatic factors in independence, including foreign alliances and competing wartime loyalties.',
    'skill_tags': ['causation', 'contextualization', 'ced:3.5'], 'display_order': 15,
})

# Framework sequence without renaming topics, which are stable seed identities.
# Keep the two overlapping foundation topics next to their expanded counterparts.
_period_three_sequence = [
    ('Contextualizing Period 3', ('3.1',)),
    ("The Seven Years' War (French and Indian War)", ('3.2',)),
    ('Taxation Without Representation and the Road to Revolution', ('3.3',)),
    ('Political Ideas of the Revolution', ('3.4',)),
    ('The American Revolutionary War', ('3.5',)),
    ('Influence of Revolutionary Ideals', ('3.6',)),
    ("The American Revolution's Effects", ('3.6',)),
    ('Government Under the Articles of Confederation', ('3.7',)),
    ('The Articles of Confederation and the Constitution', ('3.7', '3.8', '3.9')),
    ('Constitutional Convention and Ratification', ('3.8',)),
    ('Constitutional Structure and Federal Power', ('3.9',)),
    ('Washington, Hamilton, and the New Government', ('3.10',)),
    ('Developing an American Identity', ('3.11',)),
    ('Movement in the Early Republic', ('3.12',)),
    ('Continuity and Change in Period 3', ('3.13',)),
]
_period_three_existing = {topic['name']: topic for topic in UNITS[2]['topics']}
UNITS[2]['topics'] = []
for _order, (_name, _codes) in enumerate(_period_three_sequence, start=1):
    _topic = dict(_period_three_existing[_name])
    _topic['display_order'] = _order
    _topic['skill_tags'] = list(dict.fromkeys([
        *_topic['skill_tags'], *(f'ced:{code}' for code in _codes),
    ]))
    UNITS[2]['topics'].append(_topic)

UNITS[3]['topics'].append({
    'name': 'America on the World Stage',
    'description': 'Analyze diplomatic ambitions, European competition, and the limits of American power in the early nineteenth century.',
    'skill_tags': ['contextualization', 'sourcing', 'ced:4.4'], 'display_order': 5,
})

UNITS[3]['topics'].append({
    'name': 'An Age of Reform',
    'description': 'Analyze antebellum reform movements, their methods, and the relationship between rights claims and institutional change.',
    'skill_tags': ['continuity-and-change', 'sourcing', 'ced:4.11'], 'display_order': 6,
})

UNITS[3]['topics'].append({
    'name': 'Jackson and Federal Power',
    'description': 'Evaluate executive authority, conflicts over federal power, and policies affecting Native sovereignty.',
    'skill_tags': ['causation', 'sourcing', 'ced:4.8'], 'display_order': 7,
})

UNITS[3]['topics'].append({
    'name': 'Market Revolution: Industrialization',
    'description': 'Explain mechanized production, investment, transportation, and interregional economic connections.',
    'skill_tags': ['causation', 'comparison', 'ced:4.5'], 'display_order': 8,
})

UNITS[3]['topics'].append({
    'name': 'Market Revolution: Society and Culture',
    'description': 'Analyze wage labor, changing gender roles, migration, and worker responses to industrial discipline.',
    'skill_tags': ['contextualization', 'sourcing', 'ced:4.6'], 'display_order': 9,
})

UNITS[3]['topics'].append({
    'name': 'Contextualizing Period 4',
    'description': 'Situate nineteenth-century political and social change within the institutions and conflicts inherited from the founding era.',
    'skill_tags': ['contextualization', 'argumentation', 'ced:4.1'], 'display_order': 10,
})

UNITS[3]['topics'].append({
    'name': 'Politics and Regional Interests',
    'description': 'Explain sectional interests, economic policy disputes, and compromises over slavery and representation.',
    'skill_tags': ['causation', 'argumentation', 'ced:4.3'], 'display_order': 11,
})

UNITS[3]['topics'].append({
    'name': 'The Development of an American Culture',
    'description': 'Analyze distinctive literary and artistic movements, intellectual independence, and debates over cultural authority.',
    'skill_tags': ['contextualization', 'sourcing', 'ced:4.9'], 'display_order': 12,
})

UNITS[3]['topics'].append({
    'name': 'Expanding Democracy',
    'description': 'Analyze changes in voting qualifications and the racial, gender, and economic limits of political participation.',
    'skill_tags': ['contextualization', 'argumentation', 'ced:4.7'], 'display_order': 13,
})

UNITS[3]['topics'].append({
    'name': 'African Americans in the Early Republic',
    'description': 'Examine free and enslaved Black experiences, institution building, community autonomy, and resistance to racial oppression.',
    'skill_tags': ['comparison', 'argumentation', 'ced:4.12'], 'display_order': 14,
})

# Preserve broad legacy topics and their database identities while exposing all
# framework areas they span; narrower added topics remain separately available.
_period_four_legacy_codes = {
    'The Rise of Political Parties and Democracy': ['4.2', '4.7', '4.8'],
    'Markets and Westward Expansion': ['4.2', '4.5', '4.6'],
    'The Cotton Revolution and the Expansion of Slavery': ['4.13'],
    'Religious Revival and Reform Movements': ['4.10', '4.11'],
}
for _topic in UNITS[3]['topics']:
    for _code in _period_four_legacy_codes.get(_topic['name'], []):
        if f'ced:{_code}' not in _topic['skill_tags']:
            _topic['skill_tags'].append(f'ced:{_code}')

UNITS[3]['topics'].append({
    'name': 'Causation in Period 4',
    'description': 'Evaluate interacting causes of economic and social change, distinguishing mechanisms, evidence, and alternative explanations.',
    'skill_tags': ['causation', 'argumentation', 'ced:4.14'], 'display_order': 15,
})

UNITS[4]['topics'].append({
    'name': 'The Mexican-American War',
    'description': 'Analyze the war, territorial settlement, and consequences for sectional politics and residents of acquired lands.',
    'skill_tags': ['causation', 'sourcing', 'ced:5.3'], 'display_order': 5,
})

_period_five_legacy_codes = {
    'Manifest Destiny and Continued Expansion': ['5.2', '5.3'],
    'The Compromise of 1850 and Escalating Sectional Conflict': ['5.4', '5.6'],
    'The Civil War': ['5.7', '5.8'],
    'Reconstruction': ['5.10', '5.11'],
}
for _topic in UNITS[4]['topics']:
    for _code in _period_five_legacy_codes.get(_topic['name'], []):
        if f'ced:{_code}' not in _topic['skill_tags']:
            _topic['skill_tags'].append(f'ced:{_code}')

UNITS[4]['topics'].append({
    'name': 'Government Policies During the Civil War',
    'description': 'Analyze wartime federal authority, emancipation, mobilization, and the relationship between policy and implementation.',
    'skill_tags': ['causation', 'sourcing', 'ced:5.9'], 'display_order': 6,
})

UNITS[4]['topics'].append({
    'name': 'Contextualizing Period 5',
    'description': 'Connect territorial expansion and sectional conflict to earlier disputes over slavery, representation, and diplomacy.',
    'skill_tags': ['contextualization', 'argumentation', 'ced:5.1'], 'display_order': 7,
})

UNITS[4]['topics'].append({
    'name': 'Sectional Conflict: Regional Differences',
    'description': 'Compare regional labor systems and economic development while evaluating interdependence and diverse political interests.',
    'skill_tags': ['comparison', 'sourcing', 'ced:5.5'], 'display_order': 8,
})

UNITS[4]['topics'].append({
    'name': 'Comparison in Period 5',
    'description': 'Compare changing institutions, legal protections, and political outcomes across the Civil War and Reconstruction.',
    'skill_tags': ['comparison', 'argumentation', 'ced:5.12'], 'display_order': 9,
})

_period_six_legacy_codes = {
    'Industrialization and Big Business': ['6.5', '6.6'],
    'Immigration and Urbanization': ['6.8'],
    'Labor and the Rise of Unions': ['6.7'],
    'The Western Frontier and Native American Displacement': ['6.2', '6.3'],
}
for _topic in UNITS[5]['topics']:
    for _code in _period_six_legacy_codes.get(_topic['name'], []):
        if f'ced:{_code}' not in _topic['skill_tags']:
            _topic['skill_tags'].append(f'ced:{_code}')

UNITS[5]['topics'].extend([
    {'name': 'The New South',
     'description': 'Examine postwar economic change alongside unequal landownership, agricultural dependency, and racial coercion.',
     'skill_tags': ['comparison', 'causation', 'ced:6.4'], 'display_order': 5},
    {'name': 'Responses to Immigration',
     'description': 'Analyze exclusion, nativism, and the relationship between federal law and immigrant experiences.',
     'skill_tags': ['contextualization', 'sourcing', 'ced:6.9'], 'display_order': 6},
])

UNITS[5]['topics'].append({
    'name': 'Government and Economic Controversies',
    'description': 'Evaluate conflicts over federal economic authority, regulation, and the relationship between legislation and enforcement.',
    'skill_tags': ['causation', 'argumentation', 'ced:6.12'], 'display_order': 7,
})

UNITS[5]['topics'].extend([
    {'name': 'Reform in the Gilded Age',
     'description': 'Examine organized responses to urban and industrial conditions, including settlement work and social reform.',
     'skill_tags': ['contextualization', 'sourcing', 'ced:6.11'], 'display_order': 8},
    {'name': 'Politics in the Gilded Age',
     'description': 'Analyze political coalitions and competing proposals for addressing economic power and inequality.',
     'skill_tags': ['comparison', 'sourcing', 'ced:6.13'], 'display_order': 9},
])

UNITS[5]['topics'].extend([
    {'name': 'Contextualizing Period 6',
     'description': 'Connect postwar development to earlier federal policy, expansion, and economic change.',
     'skill_tags': ['contextualization', 'causation', 'ced:6.1'], 'display_order': 10},
    {'name': 'Development of the Middle Class',
     'description': 'Examine changing opportunities, cultural practices, and unequal access to consumption and leisure.',
     'skill_tags': ['comparison', 'argumentation', 'ced:6.10'], 'display_order': 11},
    {'name': 'Continuity and Change in Period 6',
     'description': 'Evaluate uneven economic and social transformation using evidence across time and regions.',
     'skill_tags': ['comparison', 'sourcing', 'ced:6.14'], 'display_order': 12},
])

# Preserve legacy topic identities while attaching verified curriculum mappings.
UNITS[6]['topics'][0]['skill_tags'] += ['ced:7.4']
UNITS[6]['topics'][1]['skill_tags'] += ['ced:7.2', 'ced:7.3', 'ced:7.5', 'ced:7.6']
UNITS[6]['topics'][2]['skill_tags'] += ['ced:7.9', 'ced:7.10']
UNITS[6]['topics'][3]['skill_tags'] += ['ced:7.12', 'ced:7.13', 'ced:7.14']

UNITS[6]['topics'].append({
    'name': 'Interwar Foreign Policy',
    'description': 'Examine diplomatic engagement, security commitments, and limits of peacekeeping between the world wars.',
    'skill_tags': ['causation', 'comparison', 'ced:7.11'], 'display_order': 5,
})

UNITS[6]['topics'].append({
    'name': '1920s Cultural and Political Controversies',
    'description': 'Analyze conflicts over national identity, immigration, religion, race, and social change in the 1920s.',
    'skill_tags': ['contextualization', 'argumentation', 'ced:7.8'], 'display_order': 6,
})

UNITS[7]['topics'][0]['skill_tags'] += ['ced:8.2']
