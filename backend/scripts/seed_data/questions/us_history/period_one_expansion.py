"""Original source-based questions; summaries are not historical quotations.

Research checked 2026-10-04 against the Library of Congress and NPS links below.
"""
SOURCES = {
    'diversity': 'https://www.loc.gov/exhibits/1492/america.html',
    'contact': 'https://www.nps.gov/peco/learn/historyculture/spanish-encounters.htm',
}


def group(topic, code, source, stimulus, items):
    result = []
    for index, (skill, difficulty, stem, correct, choices) in enumerate(items, 1):
        result.append(dict(unit_name='Period 1: 1491-1607', topic_name=topic,
            type='mcq', difficulty=difficulty,
            prompt=f'Original instructional summary, not a primary-source quotation:\n{stimulus}\n\nResearch reference: {SOURCES[source]}\n\n{stem}',
            correct_answer='ABCD'[correct], source='generated', validation_status='approved',
            skill_tags=[skill, f'ced:{code}', 'format:source-mcq', f'stimulus:ush-{code}', f'item:ush-{code}-{index}'],
            misconception_tags=[], rubric_json=None,
            options=[dict(label='ABCD'[i], text=text, is_correct=i == correct) for i, (text, _) in enumerate(choices)],
            explanations=[dict(option_label='ABCD'[i], explanation=reason, misconception_tag=None) for i, (_, reason) in enumerate(choices)]))
    return result


QUESTIONS = group('Contextualizing Period 1', '1.1', 'diversity',
    'Before 1492, societies in the Americas developed varied economies and political arrangements. Agriculture, exchange networks, and settlement patterns differed across environments; contact did not introduce social complexity to an otherwise uniform continent.', [
    ('contextualization', 2, 'Which approach best follows from this summary when studying European arrival?', 1, [
        ('Treat all Indigenous communities as one political unit.', 'Diverse political arrangements require attention to distinct communities.'),
        ('Examine the particular society and region involved in each encounter.', 'Regional variation makes local context necessary for interpreting contact.'),
        ('Assume agriculture began only after European settlement.', 'The summary identifies agriculture before 1492.'),
        ('Explain differences solely through European policies.', 'The differences described predate those policies.'),
    ]),
    ('claims-evidence', 3, 'Which evidence would most directly challenge a claim that precontact communities were entirely isolated?', 2, [
        ('A European map made after colonization.', 'A later map alone does not establish precontact exchange.'),
        ('The absence of a single continental government.', 'Political fragmentation does not imply absence of contact.'),
        ('Objects found far from the regions where their materials originated.', 'Movement of materials can provide evidence of exchange connections.'),
        ('Differences in local climates.', 'Climatic variation does not itself demonstrate communication.'),
    ]),
    ('comparison', 4, 'Which inference would go beyond the summary’s evidence?', 0, [
        ('Every society followed the same sequence toward a European-style state.', 'Diversity does not establish a universal developmental sequence or European endpoint.'),
        ('Environment is relevant to economic differences.', 'The summary explicitly links variation to environments.'),
        ('Political arrangements were not uniform.', 'The summary explicitly identifies varied arrangements.'),
        ('Some social structures existed before sustained European contact.', 'Pre-1492 economies and political arrangements support this inference.'),
    ]),
]) + group('Cultural Interactions Before 1607', '1.6', 'contact',
    'In 1540, Coronado’s expedition reached Pecos while pursuing Spanish colonial ambitions and reports of wealthy cities. The encounter brought an established Pueblo community into contact with outsiders seeking resources and influence.', [
    ('sourcing', 2, 'A report written by an expedition leader to royal officials would most need to be evaluated in light of which consideration?', 3, [
        ('Whether it uses modern spelling.', 'Spelling is less relevant than the writer’s institutional purpose.'),
        ('Whether all Pueblo residents shared its interpretation.', 'Agreement cannot be assumed; the report represents a particular perspective.'),
        ('Whether it was written after the United States gained independence.', 'The expedition occurred centuries before that event.'),
        ('The writer’s incentive to justify the expedition and seek continued support.', 'Audience and purpose may shape how resources and success are described.'),
    ]),
    ('contextualization', 3, 'Which broader development best contextualizes the expedition?', 0, [
        ('European competition for colonial resources and territorial influence.', 'The expedition fits expanding European imperial projects in the Americas.'),
        ('United States expansion under the doctrine of Manifest Destiny.', 'That nineteenth-century development cannot explain a 1540 expedition.'),
        ('Industrial demand for petroleum.', 'Industrial petroleum demand belongs to a much later context.'),
        ('The collapse of European overseas empires after World War II.', 'Decolonization after 1945 is chronologically unrelated.'),
    ]),
    ('claims-evidence', 4, 'Which additional evidence would best broaden an account based only on the expedition’s reports?', 1, [
        ('A second copy of the same report.', 'Duplicating a source does not supply another perspective.'),
        ('Pueblo oral histories and archaeological evidence considered with their own contexts and limits.', 'These can illuminate community experience while requiring appropriate source evaluation.'),
        ('A later novelist’s invented dialogue treated as a transcript.', 'Fictional dialogue cannot be treated as direct testimony.'),
        ('A modern map with no explanation of historical settlement.', 'Location alone would not add substantial evidence about community experience.'),
    ]),
]) + group('Causation in Period 1', '1.7', 'contact',
    'Coronado’s journey combined expectations of wealth with a project of Spanish expansion. Its destination was not an empty landscape: existing communities and their responses shaped what newcomers could do.', [
    ('causation', 2, 'Which explanation best accounts for the expedition’s motivations?', 2, [
        ('Only the preferences of Indigenous communities determined its departure.', 'The summary identifies Spanish ambitions and expectations as motivations.'),
        ('The journey had no economic dimension.', 'Expectations of wealth supply an economic dimension.'),
        ('Economic expectations and imperial ambitions operated together.', 'The summary explicitly connects these motivations.'),
        ('Its purpose was to defend an already independent United States.', 'No independent United States existed in 1540.'),
    ]),
    ('causation', 3, 'Why should a historian distinguish the expedition’s intentions from its outcomes?', 3, [
        ('Intentions are always irrelevant to historical explanation.', 'Intentions can help explain decisions even when outcomes differ.'),
        ('A leader’s goal guarantees that the goal was achieved.', 'An intended result does not establish an actual result.'),
        ('Outcomes can be reconstructed without any evidence.', 'Claims about outcomes require evidence.'),
        ('Local conditions and other people’s actions could alter what the expedition accomplished.', 'The summary identifies existing communities as participants affecting events.'),
    ]),
    ('making-connections', 4, 'Which generalization is most consistent with the summary?', 1, [
        ('Imperial expansion erased all local agency immediately.', 'Communities’ responses shaped newcomers’ actions.'),
        ('Explaining colonial encounters requires both external ambitions and local circumstances.', 'The account combines motives for expansion with the societies encountered.'),
        ('All encounters produced identical results because the travelers shared a nationality.', 'Nationality alone cannot establish identical local outcomes.'),
        ('An economic motive excludes political purposes.', 'The summary explicitly presents the two together.'),
    ]),
])
