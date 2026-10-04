"""Original nonfiction reading sets. People, places, and statistics are fictional."""
from .builders import passage_questions

REPAIR_PASSAGE = """[1] At last month's budget hearing, the first photograph showed the proposed Eastbank Innovation Center: glass walls, a planted roof, students gathered around machines whose names most of us had never heard. The second photograph showed our existing repair workshop: a leaking ceiling, three scarred tables, and a volunteer teaching a child to mend a backpack. The center's supporters called the contrast self-explanatory. I agreed, though not in the way they intended.

[2] I coordinate the workshop on Saturday mornings. In that room, a retired machinist may teach a teenager to thread a bolt; an hour later, the teenager may help the machinist enlarge the text on his phone. Expertise changes hands without first asking whose name belongs on a certificate. Last winter, a family brought in a lamp that had stood in three generations of their kitchens. Its switch cost less than a bus fare. The conversation it started lasted the entire morning. We repaired a circuit, but we also made it possible for a story to remain in use.

[3] Such episodes do not establish that every broken object should be saved. Some repairs are unsafe, some parts unavailable, and some volunteers are understandably tired. Nor can goodwill substitute for wiring that meets the fire code. Indeed, these limits strengthen the case for paying a coordinator and renovating the room. They do not explain why the city should abandon the workshop to start again in a building with a more photogenic roof.

[4] A council member asked how many businesses the workshop had launched. It was a reasonable question about the new center's stated goal, but a poor measure of everything the workshop does. We count repairs and attendance; we should also ask whether residents who seldom meet elsewhere have begun to trust one another. That outcome is difficult to count. Difficulty, however, is not evidence of absence. The city does not demand that every tree produce a marketable crop before it calls the shade a public benefit.

[5] I would welcome new tools and the students who know how to use them. Let us first place them where relationships already exist. Renovating an ordinary room will not supply the mayor with a spectacular opening photograph. It may give the rest of us something more durable: a place where needing help is an invitation to belong."""

REPAIR = passage_questions(
    passage_id='lang-a-repair', title='An Ordinary Room', mode='reading',
    context='Original practice passage: a fictional workshop coordinator addresses a city council considering two funding proposals.',
    passage=REPAIR_PASSAGE, items=[
    (1, '1.A', 2, 'The immediate occasion for the argument is the city council’s consideration of which decision?', 1, [
        ('Whether residents should be required to repair household objects', 'The passage proposes public funding, not a requirement imposed on residents.'),
        ('Whether to prioritize a new innovation center over an existing workshop', 'The budget hearing, competing photographs, and concluding renovation proposal establish this funding choice.'),
        ('Whether volunteers should be prohibited from using advanced equipment', 'Safety limits support investment in the workshop; no prohibition is proposed.'),
        ('Whether to replace elected officials with technical specialists', 'The speaker addresses council members as decision makers rather than proposing to replace them.'),
    ]),
    (4, '1.A', 3, 'In the context of the budget hearing, which purpose most directly motivates the coordinator’s address to the council?', 3, [
        ('Public programs should be funded only when their outcomes cannot be counted.', 'The speaker accepts attendance and repair counts; uncountability is not a funding requirement.'),
        ('Repairing old possessions is always preferable to buying new ones.', 'Paragraph 3 explicitly acknowledges cases where repair is unsafe or impractical.'),
        ('New technology usually weakens relationships between generations.', 'The phone example and final welcome for new tools contradict a general rejection of technology.'),
        ('The city should invest in the existing workshop because its established relationships are a public resource.', 'The renovation proposal follows from the workshop’s practical and social benefits throughout the passage.'),
    ]),
    (3, '3.A', 2, 'The exchange between the machinist and teenager chiefly supports which idea?', 0, [
        ('Useful knowledge circulates among people who have different kinds of expertise.', 'The roles reverse: mechanical knowledge moves one way, digital knowledge the other.'),
        ('Older residents lack the skills necessary to contribute to city programs.', 'The machinist contributes technical skill before receiving help.'),
        ('Formal qualifications are never useful in deciding who should perform repairs.', 'The example describes reciprocal learning; it does not establish that all certification is useless.'),
        ('The workshop’s main purpose is to train residents for paid technology jobs.', 'Neither participant is shown seeking employment, and the passage questions employment as the sole metric.'),
    ]),
    (9, '3.C', 4, 'How does paragraph 3 affect the speaker’s argument?', 2, [
        ('It retracts the recommendation by admitting that volunteer programs cannot be safe.', 'The speaker recommends safe renovation and a paid coordinator rather than closing the program.'),
        ('It presents the council’s objections as too unreasonable to answer.', 'The limitations are acknowledged as real rather than dismissed.'),
        ('It limits the claims made for repair while turning practical shortcomings into reasons for investment.', 'Unsafe repairs and exhausted volunteers narrow the claim; needed improvements then support funding.'),
        ('It establishes that the innovation center would inevitably experience the same failures.', 'The paragraph makes no evidence-based prediction about that center’s operations.'),
    ]),
    (4, '5.C', 3, 'The comparison to a tree in paragraph 4 primarily serves to', 1, [
        ('demonstrate that environmental benefits are more important than social benefits.', 'The analogy concerns ways of valuing benefits, not a ranking of environmental and social outcomes.'),
        ('make a familiar public benefit illustrate why market output is an incomplete standard.', 'Shade is valuable without producing a saleable crop, just as relationships can matter without launching businesses.'),
        ('provide numerical evidence for the workshop’s economic efficiency.', 'An analogy supplies conceptual support, not a numerical cost comparison.'),
        ('suggest that workshop attendance will naturally increase without funding.', 'The tree comparison does not predict attendance or remove the need for renovation.'),
    ]),
    (8, '7.A', 3, 'The phrase “a story to remain in use” in paragraph 2 emphasizes that', 0, [
        ('repair can preserve an object’s role in a family’s continuing experience.', 'The lamp remains usable while carrying memories across generations, linking practical repair and shared history.'),
        ('stories are valuable only when they can be sold.', 'The example values continuity and conversation without assigning a market price.'),
        ('the family misunderstood the technical cause of the lamp’s failure.', 'The phrase interprets the meaning of the repair rather than describing a technical mistake.'),
        ('the coordinator prefers storytelling to completing necessary repairs.', 'The circuit is actually repaired; storytelling accompanies rather than replaces the work.'),
    ]),
    (5, '5.B', 4, 'Which description best accounts for the passage’s overall organization?', 3, [
        ('A chronological history of the city followed by a prediction of technological change', 'The passage opens at a hearing and uses examples; it does not recount the city’s history.'),
        ('A neutral comparison that leaves readers to choose between equally endorsed proposals', 'The speaker clearly endorses renovating the existing workshop.'),
        ('A scientific hypothesis followed by a controlled experiment and a reported result', 'Anecdotes and analogies support a civic argument; no experiment is conducted.'),
        ('A disputed comparison, concrete examples of value, acknowledged limits, and a recommendation using a broader standard', 'These steps follow the photographs, reciprocal repairs, qualifications, discussion of measurement, and final proposal.'),
    ]),
    (7, '7.C', 4, 'In “That outcome is difficult to count. Difficulty, however, is not evidence of absence,” the combination of the full stop and “however” primarily', 2, [
        ('equates a lack of measurement with proof that the workshop creates trust.', 'The statement rejects one inference; it does not claim that unmeasured trust has thereby been proved.'),
        ('makes the previous sentence an admission that social benefits do not exist.', 'It explicitly distinguishes difficulty counting an outcome from its nonexistence.'),
        ('interrupts a possible inference by sharply distinguishing measurement from existence.', 'The short sentence and “however” block the leap from hard-to-count to absent.'),
        ('changes the topic from public programs to the reliability of photographs.', 'The two sentences remain focused on measuring social benefits.'),
    ]),
])

UNCERTAINTY_PASSAGE = """[1] On the morning our coastal forecast appeared, the headline announced that the sea would reach the old freight depot within thirty years. Our report had said something less convenient: under one emissions pathway, with one set of assumptions about local land movement, the depot lay within the range of projected flooding. By afternoon, one reader accused us of predicting catastrophe; another accused us of refusing to predict anything at all.

[2] I understand both responses. A map shaded in red looks decisive even when the caption is cautious. People deciding whether to buy a home or repair a road need more than a cloud of possibilities. But replacing that cloud with a single bright number does not make a decision wiser. It merely makes the uncertainty harder to see. When a bridge engineer allows for several possible loads, we call the allowance prudence, not indecision. The same courtesy should extend to forecasts of water.

[3] A projection is a conditional statement about a world that may develop in different ways. Some uncertainty concerns the behavior of the ocean; some concerns choices that people have not yet made. Collapsing these sources into one margin of error can obscure an important distinction. Better instruments may narrow the first kind. The second requires public choices, not simply another instrument. Treating all uncertainty as a scientific defect asks a thermometer to decide whether we should open the window.

[4] This distinction does not excuse careless modeling. Our team discovered that one survey marker had shifted during construction, corrected the local elevation estimate, and published the change. Critics circulated the revision as proof that the original work had been worthless. Yet a forecast that cannot be revised is not more trustworthy; it is merely harder to improve. The relevant questions are why the estimate changed, whether the correction is documented, and how much the decision depends on it.

[5] For the depot, the practical response need not wait for a perfect map. The city can preserve access to higher ground, delay expensive equipment purchases for the lowest floor, and identify the observations that would trigger further action. These measures can be adjusted as evidence accumulates. To communicate uncertainty well is neither to whisper a warning nor to shout a prophecy. It is to show people which parts of the path are visible, which remain hidden, and where a different step is still possible."""

UNCERTAINTY = passage_questions(
    passage_id='lang-a-forecast', title='The Uses of an Unfinished Map', mode='reading',
    context='Original practice passage: a fictional coastal researcher writes for a general-interest science magazine after public discussion of a local flood forecast.',
    passage=UNCERTAINTY_PASSAGE, items=[
    (2, '1.B', 3, 'In paragraph 2, the writer acknowledges readers’ need for practical decisions primarily to', 2, [
        ('concede that conditional forecasts are of no use outside scientific research.', 'The passage later uses conditional forecasts to recommend practical, adjustable measures.'),
        ('suggest that readers are too impatient to understand scientific evidence.', '“I understand” and the concrete decisions acknowledge legitimate concerns, not intellectual inadequacy.'),
        ('establish common ground before explaining why certainty should not be manufactured.', 'The writer recognizes a real need, then explains why a single number can hide rather than resolve uncertainty.'),
        ('transfer responsibility for inaccuracies from researchers to the public.', 'Paragraph 4 accepts researchers’ responsibility for correction and documentation.'),
    ]),
    (1, '3.A', 2, 'The example of a bridge engineer supports the claim that', 0, [
        ('planning for a range of possible conditions can be responsible professional practice.', 'Allowing for several loads illustrates prudence under uncertain conditions.'),
        ('bridge design and coastal forecasting rely on identical mathematical models.', 'The analogy concerns decision making, not the identity of the models.'),
        ('engineers can remove all uncertainty before construction begins.', 'The example specifically retains several possible loads.'),
        ('public audiences usually understand coastal forecasts better than structural design.', 'No comparison of audience understanding is offered.'),
    ]),
    (3, '5.A', 4, 'Which assumption is most important to the reasoning in paragraph 3?', 3, [
        ('Future emissions choices can be measured with the same instruments as water temperature.', 'The paragraph separates choices from physical measurements.'),
        ('Any projection with more than one source of uncertainty must be abandoned.', 'The writer recommends distinguishing uncertainties, not abandoning projections.'),
        ('The ocean’s behavior is completely unrelated to human decisions.', 'The report’s emissions pathways imply a connection between human choices and physical outcomes.'),
        ('Different sources of uncertainty may require different kinds of response.', 'The contrast between better instruments and public choices depends on matching a response to the source of uncertainty.'),
    ]),
    (6, '7.A', 3, 'The thermometer comparison at the end of paragraph 3 is best understood as', 1, [
        ('a literal proposal for using household equipment in coastal research.', 'The household example is figurative and concerns the limits of measurement.'),
        ('an illustration of the mismatch between measuring conditions and choosing an action.', 'A thermometer reports temperature but does not decide whether opening a window serves people’s goals.'),
        ('an assertion that measurement has no role in public policy.', 'The writer supports better instruments while explaining why they cannot make public choices.'),
        ('a claim that climate projections are no more complex than indoor temperature readings.', 'The analogy isolates the measurement-choice distinction rather than equating complexity.'),
    ]),
    (7, '3.C', 3, '“This distinction does not excuse careless modeling” at the start of paragraph 4 primarily', 0, [
        ('prevents the discussion of uncertainty from being read as permission to neglect accuracy.', 'The sentence limits a possible overextension of the preceding defense of conditional projections.'),
        ('withdraws the writer’s claim that uncertainty can be communicated usefully.', 'The writer continues defending useful communication while insisting on quality controls.'),
        ('introduces evidence that all models are equally unreliable.', 'One documented correction does not establish equal unreliability across all models.'),
        ('rejects the earlier distinction between scientific uncertainty and public choices.', '“This distinction” refers back to and retains that distinction.'),
    ]),
    (4, '5.C', 4, 'Why does the writer recount the revision of the survey marker estimate?', 2, [
        ('To demonstrate that the freight depot is now known to be safe from flooding', 'The passage does not state the correction’s direction or establish the depot’s safety.'),
        ('To show that revisions should be kept private until critics agree with them', 'The team publishes the correction, and the writer calls for documentation.'),
        ('To distinguish accountable correction from the absolute unreliability critics infer', 'The example allows the writer to explain why reasons and magnitude of revisions matter more than their mere occurrence.'),
        ('To argue that researchers should never defend their findings publicly', 'The entire passage is a public explanation and defense of how findings should be used.'),
    ]),
    (8, '7.B', 4, 'The parallel clauses beginning “which parts,” “which,” and “where” in the final sentence emphasize', 3, [
        ('a progression toward eliminating all uncertainty before acting.', 'The final clause preserves the possibility of action while some parts remain hidden.'),
        ('the writer’s refusal to distinguish strong evidence from weak evidence.', 'Visible and hidden parts expressly distinguish what is and is not known.'),
        ('three competing forecasts from unrelated research teams.', 'The clauses describe tasks of communication, not separate forecasts.'),
        ('the connected responsibilities of stating knowledge, acknowledging limits, and preserving choices.', 'Each parallel clause adds one part of responsible communication rather than reducing it to a single prediction.'),
    ]),
    (5, '5.B', 3, 'Paragraph 5 contributes to the argument chiefly by', 1, [
        ('replacing the scientific discussion with an unrelated account of city finances.', 'The proposed purchases and access routes directly respond to the depot’s flood risk.'),
        ('showing how the preceding view of uncertainty can guide concrete, revisable decisions.', 'The proposed actions apply the earlier distinction between conditional knowledge and public choices.'),
        ('introducing an opposing view that the writer leaves unanswered.', 'The writer endorses these actions as the practical consequence of the argument.'),
        ('proving that the original thirty-year headline was accurate.', 'The actions do not validate the headline’s unqualified certainty.'),
    ]),
])

TRANSLATION_PASSAGE = """[1] When my grandmother asked me to translate a letter from the housing office, I began with the confidence of someone who had received excellent marks in English. I knew every word. I even knew the official phrase that made the request sound less like a request than a command. Then she asked, “Does the woman who wrote this sound angry?” My education had prepared me to translate the sentence, but not yet the encounter.

[2] I read it again. The letter required a form, gave a deadline, and offered a telephone number. None of those facts revealed whether the writer was irritated. I told my grandmother so, and she nodded. “Then do not give her my apology,” she said. “Give her my answer.” I had been adding politeness that the document did not demand, quietly turning unfamiliarity with its language into a reason to ask forgiveness.

[3] Years later, when I began translating notices at a neighborhood center, volunteers praised people like me as bridges between communities. The image was generous, and I accepted it for a while. But a bridge is expected to hold still while others cross. Translation required movement: asking what a phrase concealed, checking whether a deadline allowed any exception, and sometimes telling an official that the proposed wording was difficult even for people born into the language. I was not carrying an intact package from one shore to another. I was helping two people discover which parts of the package needed to be opened.

[4] This work can tempt a translator to speak for someone rather than with them. I have done that too. At one appointment, certain that I understood a neighbor's objection, I began explaining it before she finished. She waited, then supplied a reason I had never considered. My fluent version had been less accurate than her unfinished one. Since then, I try to treat a pause as room that belongs to the speaker, not a vacancy I am obliged to fill.

[5] I still admire precision. A mistranslated date can cost a family a hearing, and a softened warning can conceal a real danger. But precision is not exhausted by matching words. It includes preserving who gets to decide what is being said. My grandmother did not ask me to make her sound like someone else. She asked me to make it possible for someone else to hear her."""

TRANSLATION = passage_questions(
    passage_id='lang-a-translation', title='Whose Answer?', mode='reading',
    context='Original practice passage: a fictional community translator reflects on learning to translate institutional correspondence.',
    passage=TRANSLATION_PASSAGE, items=[
    (4, '1.A', 2, 'The opening episode chiefly establishes which tension?', 3, [
        ('The narrator’s dislike of English and desire to stop studying it', 'The narrator begins proud of strong English marks and never rejects the language.'),
        ('The grandmother’s inability to understand the purpose of any official letter', 'She understands enough to ask a precise question about tone and insist on her own answer.'),
        ('The housing office’s wish to apologize and the grandmother’s refusal to accept it', 'No apology from the office is described; the narrator was adding an apology on the grandmother’s behalf.'),
        ('The narrator’s command of vocabulary and incomplete understanding of the social interaction', 'Knowing each word does not settle tone or justify changing the grandmother’s stance.'),
    ]),
    (2, '3.A', 3, '“Give her my answer” in paragraph 2 most clearly reveals the grandmother’s desire to', 1, [
        ('avoid providing the information requested in the letter.', 'She wants to give an answer rather than withhold it.'),
        ('retain authority over her response without apologizing for needing translation.', 'The instruction contrasts her chosen answer with the translator’s unrequested apology.'),
        ('persuade the office to conduct all business in her first language.', 'The passage does not describe such a policy request.'),
        ('correct the narrator’s mistaken translation of the deadline.', 'No mistranslated deadline is identified in this scene.'),
    ]),
    (5, '7.A', 4, 'The writer complicates the image of a “bridge” primarily because it', 0, [
        ('makes translation seem passive when it often requires questioning and negotiation.', 'The bridge “holds still,” while the following examples describe active clarification and challenge.'),
        ('suggests that communities share no meaningful differences.', 'A bridge actually presumes a separation; the writer’s objection concerns passivity.'),
        ('implies that translators should acquire formal engineering qualifications.', 'The image is figurative and carries no recommendation about professional credentials.'),
        ('understates the importance of knowing vocabulary accurately.', 'The passage accepts vocabulary’s importance; the criticism is that word transfer alone is incomplete.'),
    ]),
    (3, '5.C', 3, 'The account of the interrupted neighbor in paragraph 4 functions mainly as', 2, [
        ('proof that inexperienced speakers should not attend appointments.', 'The neighbor has a reason the fluent narrator missed; the example supports listening to her.'),
        ('a counterexample intended to discredit all community translation services.', 'The writer uses the mistake to improve translation practice, not reject it.'),
        ('a self-critical example showing how helpful fluency can displace another person’s meaning.', 'The narrator’s premature explanation is fluent but inaccurate because it replaces rather than conveys the neighbor’s reason.'),
        ('a digression that shifts attention away from the essay’s central concern.', 'The example directly develops the concern with preserving a speaker’s agency.'),
    ]),
    (8, '7.A', 3, 'Describing a pause as “room that belongs to the speaker” encourages readers to view silence as', 1, [
        ('evidence that the translator has failed to prepare.', 'The comparison focuses on the speaker’s space to formulate meaning rather than translator preparedness.'),
        ('an opportunity for a speaker to complete an idea without being displaced.', 'The ownership metaphor argues against treating pauses as gaps the translator must fill.'),
        ('a refusal that should always end the conversation.', 'A pause may allow an unfinished idea to develop; the writer does not equate it with refusal.'),
        ('a technique for making an official feel guilty.', 'The passage discusses listening and ownership of speech, not manipulating officials.'),
    ]),
    (9, '3.C', 4, 'How does “I still admire precision” shape the conclusion?', 3, [
        ('It abandons the earlier claim that translation involves social relationships.', 'The paragraph combines accuracy with the speaker’s authority over meaning.'),
        ('It suggests that politeness is more important than accurate dates.', 'The examples warn that inaccurate dates and softened warnings can cause harm.'),
        ('It establishes literal word matching as the only defensible standard.', 'The next sentence explicitly says precision is not exhausted by matching words.'),
        ('It preserves the value of factual accuracy while expanding what accurate translation requires.', 'The writer affirms dates and warnings, then includes the speaker’s control over the message.'),
    ]),
    (6, '3.B', 3, 'Which statement best expresses the essay’s controlling idea?', 0, [
        ('Responsible translation combines linguistic accuracy with respect for the original speaker’s agency.', 'The grandmother’s reply, bridge critique, interrupted neighbor, and conclusion develop these paired requirements.'),
        ('Institutional writing is deliberately designed to prevent residents from understanding it.', 'The narrator identifies difficulty but does not establish deliberate obstruction as a universal motive.'),
        ('Family members are invariably better translators than trained professionals.', 'The essay offers no comparison of family translators with professionals and acknowledges the narrator’s errors.'),
        ('A translator should avoid intervening even when wording is unclear.', 'Paragraph 3 endorses asking questions and challenging unclear official wording.'),
    ]),
    (8, '1.B', 3, 'For readers who admire fluent translators, the narrator’s admissions of personal mistakes primarily serve to', 2, [
        ('replace their admiration with distrust of all community translation.', 'The narrator continues translating and identifies ways to improve the work, rather than urging wholesale distrust.'),
        ('assure them that technical accuracy has little practical importance.', 'The conclusion emphasizes that inaccurate dates and warnings can have serious consequences.'),
        ('encourage them to value attentive listening as part of competence rather than treating fluency as sufficient.', 'The narrator’s fluent but premature explanation shows why admired language skills must be paired with respect for the speaker.'),
        ('persuade them that only a speaker’s relatives can understand a message reliably.', 'The narrator makes mistakes both as a relative and in community work; kinship is not presented as a guarantee.'),
    ]),
])

QUESTIONS = REPAIR + UNCERTAINTY + TRANSLATION
