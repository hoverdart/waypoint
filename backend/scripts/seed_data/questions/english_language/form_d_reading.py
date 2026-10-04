"""Original Form D reading stimuli; people, settings, and events are fictional."""
from .builders import passage_questions

STAGE_PASSAGE = """[1] At the first rehearsal, the director asked us to cross the stage as though we had somewhere to go. We obeyed with such determination that three of us arrived at the same chair. The audience, had there been one, might have admired our urgency. It would not have known what any of us wanted. I was seventeen and believed that acting consisted largely of making an emotion visible. That afternoon I learned that visibility and intelligibility were different problems.

[2] The director did not tell us to feel less. She asked each of us to name what the other person might refuse. One character needed a signature; another needed the conversation to end; mine needed to be forgiven without making an apology. Suddenly the chair ceased to be our common destination. A step toward it could be a challenge, a retreat, or an attempt to keep someone from leaving. We had not added furniture. We had added reasons.

[3] I went home convinced that every gesture needed a private explanation. For a week I filled a notebook with my character's imagined childhood. The director listened patiently to this biography and then asked why I turned away during the scene's only question. I explained that the character had distrusted questions since an invented incident at school. She asked me to stay facing my partner for one rehearsal. Without the turn, I heard the question differently. My carefully prepared history had been protecting me from what the other actor was doing.

[4] There is a familiar account of preparation in which one gathers enough knowledge and then delivers a finished performance. My notebook had followed that account. Rehearsal taught me a less comfortable sequence: prepare, encounter, revise. The preparation mattered. A person who brought nothing to the room gave a partner little to work with. But a person who could change nothing brought a locked room of a different kind. Neither made much space for a scene to happen between people.

[5] On opening night I forgot a line. My partner waited, then repeated the beginning of her question in a tone I had never heard before. I answered with words that were not in the script but returned us to it. I do not recommend forgetting lines. The recovery was possible because we knew the scene's structure well enough to recognize where we had lost it. Yet the moment I remember most clearly was not my improvised answer. It was the brief silence in which I realized that someone was still listening.

[6] I no longer act, but I sometimes recognize that first rehearsal in meetings where everyone speaks urgently and no one seems to be addressing anyone else. I cannot solve those meetings by assigning motives to strangers. What I can do is ask what the next sentence might change, and listen for an answer I have not already prepared. The stage did not teach me to display a larger version of myself. It taught me how much of a conversation begins outside me."""

STAGE = passage_questions(passage_id='lang-d-stage', title='Reasons to Cross a Room', mode='reading',
 context='Original fictional memoir essay by a former amateur actor for a general-interest magazine.', passage=STAGE_PASSAGE, items=[
 (1,'3.A',3,'The collision at the chair chiefly supports which distinction?',0,[
 ('Visible effort does not by itself communicate a clear purpose.','The actors look urgent, but the imagined audience cannot identify what they want.'),
 ('Physical comedy requires less rehearsal than serious drama.','The incident is not presented as a comparison between theatrical genres.'),
 ('An actor’s intention must always be explained aloud to the audience.','The director develops intentions to shape action, not to require spoken explanations.'),
 ('A shared destination necessarily produces a shared intention.','The later account reveals different intentions despite the initial shared destination.'),
 ]),
 (4,'3.B',2,'Which claim best encompasses the essay’s account of preparation?',2,[
 ('Inventing a character’s past is the most reliable way to respond to another actor.','The invented biography sometimes prevents the narrator from responding.'),
 ('A convincing performance depends on replacing written dialogue with spontaneous speech.','The narrator explicitly does not recommend forgetting lines and values the script’s structure.'),
 ('Preparation becomes productive when it supports responsiveness rather than protecting a fixed performance.','The notebook, rehearsal, and recovery all distinguish useful preparation from inflexibility.'),
 ('The most experienced performer should determine how every other actor responds.','The essay values an encounter between people rather than unilateral control.'),
 ]),
 (2,'1.B',4,'The admission “I do not recommend forgetting lines” most directly anticipates readers who might',1,[
 ('doubt that the narrator can recall the exact date of the performance.','The qualification concerns the lesson of the incident, not its date.'),
 ('interpret the successful recovery as a reason to dismiss disciplined preparation.','The next sentence credits knowledge of the scene’s structure for making recovery possible.'),
 ('assume that the partner deliberately caused the narrator’s mistake.','No deliberate interference is suggested or answered by the admission.'),
 ('expect the essay to rank amateur actors against professional actors.','The qualification makes no comparison of professional status.'),
 ]),
 (3,'5.A',4,'Paragraphs 2 and 3 together suggest that an explanation of a character’s behavior should be judged partly by whether it',3,[
 ('can account for every event in the character’s life.','The exhaustive biography is less useful than attending to the present exchange.'),
 ('remains unchanged across all rehearsals.','Revision is precisely what the narrator learns to allow.'),
 ('makes the actor’s preparation invisible to the director.','Concealing preparation is not the standard developed in the essay.'),
 ('helps the actor engage with the action occurring in the scene.','Reasons first clarify interaction, but an invented reason later obstructs listening.'),
 ]),
 (4,'5.C',3,'The account of opening night primarily functions as',0,[
 ('a concrete test of the relationship between preparation and responsiveness described earlier.','The actors use a known structure while adapting to an unexpected interruption.'),
 ('a counterexample showing that rehearsal is unnecessary.','The narrator explicitly credits prior knowledge of the scene.'),
 ('a chronological explanation of how the script was originally written.','The event concerns performing the script, not composing it.'),
 ('an analogy comparing audiences with directors.','Neither audience nor director is the focus of this incident.'),
 ]),
 (7,'7.B',2,'The compressed sequence “prepare, encounter, revise” emphasizes',2,[
 ('three interchangeable names for a single activity.','The verbs identify successive but related actions, not synonyms.'),
 ('the elimination of preparation once a performer gains experience.','Preparation remains the first action in the sequence.'),
 ('a process in which prior work remains open to change through interaction.','The sequence contrasts with gathering knowledge and delivering a finished product.'),
 ('the superiority of written notes to physical rehearsal.','Encounter and revision challenge that hierarchy.'),
 ]),
 (8,'7.A',4,'Calling an inflexible performer “a locked room of a different kind” suggests that',1,[
 ('private preparation inevitably reveals more than public rehearsal.','The image concerns restricted interaction, not the quantity of knowledge revealed.'),
 ('extensive preparation can exclude a partner as effectively as bringing nothing to the scene.','Both conditions leave little room for something to happen between performers.'),
 ('the theater lacks enough physical space for the cast.','The locked room is a metaphor for inflexibility.'),
 ('a convincing character must conceal all intentions from other actors.','The director’s questions make intentions useful to interaction rather than requiring concealment.'),
 ]),
 (1,'1.A',3,'The final paragraph extends the essay’s purpose by',3,[
 ('offering acting exercises as a guaranteed solution to workplace disagreements.','The narrator expressly limits what can be done in meetings.'),
 ('claiming that theatrical motives explain every stranger’s behavior.','The narrator rejects assigning motives to strangers.'),
 ('replacing the theater narrative with a criticism of all formal meetings.','Meetings provide an application, not a universal condemnation.'),
 ('inviting readers to consider how lessons about listening apply beyond performance.','The narrator connects rehearsal to conversations in which urgent speech lacks responsiveness.'),
 ]),
])

SEEDS_PASSAGE = """[1] My grandmother stored seeds in envelopes that had already carried other messages. A bill became a home for beans; a wedding invitation held marigolds. When I began helping her, I wanted a new packet for every variety, printed labels, a drawer that would close without catching a corner. She agreed to the drawer. About the packets she was less certain. Turn one over, she said.

[2] On the back of an envelope she had written: “From Lena; early, but not in the cold spring.” On another: “Good climbing the broken fence.” These were poor labels for a shop and useful notes for a garden. They named relationships between a plant and a season, a neighbor, an imperfect piece of ground. I had expected an inventory. She had kept a record of encounters.

[3] I do not wish to make disorder into a virtue. Two envelopes had lost their names altogether, and one held seeds too damp to keep. My grandmother discarded those seeds without ceremony. She was not preserving the past in every handful. She wanted something that would grow. When I offered waterproof labels, she accepted them, provided there was room for more than a name.

[4] Years later, after I moved, I planted beans from one of her envelopes against a clean new trellis. They grew badly. The soil, the light, and my watering were different; the envelope could not tell me which difference mattered most. I almost blamed the seeds. Instead I wrote a note and tried another position the following year. The words on the packet had not failed by leaving me a question. I had failed, briefly, by mistaking them for a guarantee.

[5] A seed catalog has uses that my grandmother's envelopes could not supply. A gardener choosing among unfamiliar varieties needs clear descriptions, and a seller should be accountable for what a packet contains. But the catalog's confident picture can invite a kind of impatience: plant this, obtain that. The envelope asks something slower. What happened here? What might happen where you are? Its record is particular enough to be useful and incomplete enough to require attention.

[6] Last autumn a neighbor asked for seeds from my own garden. I gave her a labeled packet and added the date, the corner where the plant had grown, and a warning about a dry week. The packet was tidier than my grandmother's. I have not inherited her handwriting or her willingness to stack envelopes beside the kettle. What I hope to have inherited is the space she left for another person's observation. A garden can be passed on without pretending that the next gardener will occupy the same ground."""

SEEDS = passage_questions(passage_id='lang-d-seeds', title='Room on the Packet', mode='reading',
 context='Original fictional reflective essay for a gardening journal; the family history and observations are invented.', passage=SEEDS_PASSAGE, items=[
 (2,'3.A',4,'The notes about a cold spring and a broken fence most strongly support the idea that the grandmother’s records',2,[
 ('establish universal rankings of the plants’ quality.','The notes specify circumstances rather than a universal hierarchy.'),
 ('exclude practical information in favor of family memories.','Season and growing support are practical details, even though a neighbor is also named.'),
 ('preserve circumstances that a variety name alone would not communicate.','Both notes connect growth to particular conditions and relationships.'),
 ('prove that damaged materials improve plant growth.','One successful use of a broken fence does not establish that damage causes better growth.'),
 ]),
 (4,'3.B',3,'Which statement best expresses the central claim of the essay?',0,[
 ('Inherited knowledge is most useful when it guides new observation without promising identical results.','The envelopes provide experience to build on while requiring attention to changed conditions.'),
 ('Modern labels inevitably erase the value of older practices.','Both grandmother and narrator accept clearer labels with room for context.'),
 ('Personal gardening records can replace all commercial descriptions.','Paragraph 5 explicitly recognizes functions that catalogs serve.'),
 ('Gardening succeeds only when descendants reproduce their ancestors’ methods exactly.','The narrator changes materials and methods while preserving an approach to observation.'),
 ]),
 (6,'3.A',2,'The grandmother’s willingness to discard damp seeds provides evidence that she',3,[
 ('has stopped valuing the plants associated with her neighbors.','The disposal concerns viability, not rejection of neighbors.'),
 ('prefers commercial seeds to every seed saved at home.','No such general preference is established.'),
 ('considers any handwritten record more important than a living plant.','She discards unusable seeds because she wants something that will grow.'),
 ('values practical cultivation more than preserving every object from the past.','Discarding spoiled seeds limits a purely nostalgic interpretation of her habits.'),
 ]),
 (5,'5.A',4,'The writer’s reasoning in paragraph 4 depends on recognizing that',1,[
 ('the same seeds should produce identical results wherever they are planted.','That assumption is the narrator’s error, not the paragraph’s conclusion.'),
 ('a record can remain informative even when changed conditions prevent it from predicting an outcome.','The note prompts another observation and trial without identifying every cause in advance.'),
 ('a disappointing result proves that every prior observation was inaccurate.','The narrator learns not to treat one disappointing result as invalidating the record.'),
 ('a gardener must identify a single cause before making any adjustment.','The narrator tries another position without claiming to have isolated one cause.'),
 ]),
 (5,'5.B',3,'Paragraph 5 contributes to the essay’s organization by',2,[
 ('introducing a commercial solution that makes the earlier story irrelevant.','The catalog comparison clarifies the earlier lesson rather than replacing it.'),
 ('returning to the first day of the narrator’s childhood in chronological order.','It pauses the narrative to compare forms of knowledge.'),
 ('qualifying a possible rejection of catalogs while clarifying what personal records add.','Acknowledging catalogs’ uses allows a more precise account of the envelopes’ value.'),
 ('resolving the exact cause of the beans’ poor growth.','The cause remains undetermined; the paragraph discusses expectations of information.'),
 ]),
 (8,'7.A',2,'The phrase “a record of encounters” chiefly emphasizes that the envelopes',0,[
 ('connect plants with particular people, conditions, and experiences.','The phrase gathers the notes about neighbors, seasons, and places into a shared description.'),
 ('list accidental meetings in the order they occurred.','The records concern cultivation rather than a chronological social diary.'),
 ('contain instructions that require no interpretation.','Their particularity and incompleteness require interpretation.'),
 ('describe competitions between different plant varieties.','The passage does not frame the plants as competitors.'),
 ]),
 (7,'7.C',3,'The colon before “plant this, obtain that” in paragraph 5 introduces',3,[
 ('a quotation explicitly attributed to a named seed company.','No company or literal catalog quotation is identified.'),
 ('a list of the catalog’s separate legal obligations.','The phrase expresses an expectation rather than enumerating obligations.'),
 ('a qualification that reverses the preceding claim about impatience.','The phrase exemplifies that impatience rather than reversing the claim.'),
 ('a compressed formulation of the expectation the writer finds potentially misleading.','The paired commands make a direct, guaranteed outcome seem automatic.'),
 ]),
 (8,'1.B',4,'The acknowledgment that a seller should be accountable for a packet’s contents most directly addresses readers who might',1,[
 ('want the narrator to reproduce the grandmother’s handwriting.','The acknowledgment concerns reliable commercial information, not handwriting.'),
 ('worry that praising uncertainty excuses inaccurate or inadequate labeling.','The writer distinguishes openness to variable outcomes from a seller’s responsibility to describe contents clearly.'),
 ('assume that a family garden cannot supply seeds to neighbors.','Seed sharing is demonstrated elsewhere and is not the issue addressed here.'),
 ('believe that all plants require exactly the same amount of water.','The acknowledgment makes no claim about identical cultivation requirements.'),
 ]),
])

BRIDGE_PASSAGE = """[1] Members of the council, the old footbridge has been closed for seven months. In that time we have become very accomplished at explaining why a decision is difficult. Engineers have described the damaged supports. The finance committee has described the limited budget. Residents have described the longer walk. All these descriptions are necessary. None carries a person across the river.

[2] I speak as the keeper of the shop beside the eastern path, and I will not pretend to have no interest in its reopening. Fewer walkers pass my window now. But the petition I bring is signed also by people who have never bought anything from me: pupils whose school is on the western bank, a carer who makes the journey twice daily, and residents who use the path to reach the clinic. Our interests meet at the bridge without being identical.

[3] We have been told that a permanent replacement will last for generations. I hope it will. A town should not purchase a cheap danger merely because it is impatient. Yet a plan for the next fifty years does not answer every question about the next six months. The temporary crossing recommended in the engineer's second report would have a limited load and require inspection after heavy rain. Those conditions are reasons to specify how it will be managed, not reasons to speak as though no proposal exists.

[4] The cost estimate deserves public examination. It should include staffing inspections and removing the temporary structure when it is no longer needed. It should also be compared with the costs now distributed among residents: longer journeys, missed visits, and transport fares. I cannot place a precise sum on every inconvenience, and I would distrust a petition that pretended it could. But a cost does not become zero because it is difficult to enter in the council's ledger.

[5] Some signers want the temporary bridge approved tonight. I ask for a narrower decision. Publish the two estimates, identify the person responsible for inspections, and set a date on which the council will accept or reject the temporary plan with reasons. If the proposal is unsafe, say which condition cannot be met. If it is unaffordable, show the comparison. We can argue with an answer. We cannot plan our journeys around another promise to consider the matter.

[6] The river has not grown wider during these seven months. The distance between a difficulty described and a duty accepted has. I ask you to shorten that distance, even before anyone lays the first board."""

BRIDGE = passage_questions(passage_id='lang-d-bridge', title='A Date for an Answer', mode='reading',
 context='Original fictional council testimony by a shopkeeper about a closed footbridge. Technical reports, costs, and events are invented for rhetorical analysis.', passage=BRIDGE_PASSAGE, items=[
 (3,'3.A',3,'The list of pupils, a carer, and clinic users supports the speaker’s position by',1,[
 ('proving that none of the petitioners has a financial interest in reopening.','The speaker acknowledges a financial interest and does not exclude others’ financial interests.'),
 ('showing that a common request can arise from several different practical needs.','The examples explain how interests meet without being identical.'),
 ('establishing that the bridge is used by every resident of the town.','Several kinds of users do not establish universal use.'),
 ('showing that the engineer’s report is based on a survey of these groups.','The source of the engineer’s findings is not described.'),
 ]),
 (6,'3.B',2,'Which statement most accurately captures the speaker’s principal request?',3,[
 ('Approve a permanent replacement immediately, regardless of its cost.','The speaker requests an accountable decision process for the temporary proposal.'),
 ('Treat the petition’s signatures as a substitute for engineering review.','The speaker accepts safety conditions and asks that any unmet condition be identified.'),
 ('Postpone all decisions until every inconvenience has been assigned a precise price.','The speaker rejects treating hard-to-price burdens as zero and calls for a decision date.'),
 ('Make a timely, reasoned decision about the temporary crossing using explicit responsibilities and comparative costs.','Paragraph 5 specifies publication, inspection responsibility, and a dated acceptance or rejection.'),
 ]),
 (4,'1.A',4,'The speaker’s disclosure of a personal business interest chiefly serves the purpose of',0,[
 ('acknowledging a possible concern about credibility before showing that the petition has a broader basis.','The admission makes the interest visible rather than relying on a false claim of disinterest.'),
 ('making the council legally responsible for restoring the shop’s previous revenue.','No legal compensation claim is made.'),
 ('withdrawing from the debate because an interested person cannot offer relevant evidence.','The speaker continues and presents other residents’ needs.'),
 ('arguing that commercial interests should outweigh all other uses of the path.','The examples place the shop alongside, not above, other needs.'),
 ]),
 (2,'1.B',3,'The statement “A town should not purchase a cheap danger merely because it is impatient” appeals most directly to council members’ concern for',2,[
 ('preserving the appearance of unanimity among petitioners.','The speaker later admits disagreement among signers.'),
 ('avoiding any public discussion of engineering limits.','The speaker wants limits specified publicly.'),
 ('protecting safety and long-term value while responding to demands for action.','The concession accepts a legitimate reason for caution before distinguishing temporary and permanent planning.'),
 ('ensuring that shopkeepers receive priority access to public infrastructure.','No priority for shopkeepers is proposed.'),
 ]),
 (3,'5.C',2,'The contrast between “the next fifty years” and “the next six months” develops the argument by',1,[
 ('showing that the permanent bridge’s predicted lifetime is mathematically impossible.','The passage does not dispute the prediction’s calculation.'),
 ('distinguishing planning horizons that require related but different decisions.','A long-term replacement does not by itself address access during the wait.'),
 ('proving that a temporary structure is always less expensive than a permanent one.','No universal cost comparison follows from the time frames.'),
 ('identifying the exact date on which the current closure will end.','The speaker asks for a decision date; no reopening date has been established.'),
 ]),
 (5,'5.A',4,'The reasoning in paragraph 4 challenges the assumption that',3,[
 ('inspection and removal costs belong in the temporary proposal’s estimate.','The speaker explicitly says those costs should be included.'),
 ('different residents may bear different burdens from a closure.','The varied examples rely on that possibility rather than challenge it.'),
 ('public decisions should take financial constraints into account.','The speaker asks for examination of costs, not their exclusion.'),
 ('only costs readily recorded in the council’s accounts are relevant to the comparison.','The speaker includes distributed burdens while acknowledging uncertainty in pricing them.'),
 ]),
 (7,'7.B',3,'The repeated conditional pattern “If ... say” and “If ... show” in paragraph 5 chiefly',0,[
 ('turns possible grounds for rejection into specific obligations to explain the decision.','Each condition pairs a legitimate objection with a request for accountable evidence.'),
 ('asserts that both safety and cost objections have already been disproved.','The speaker allows that either objection might justify rejection.'),
 ('suggests that the council should alternate between two unrelated topics.','Both conditions concern evaluation of the same proposal.'),
 ('replaces the request for a decision with an invitation to postpone it indefinitely.','The conditions accompany a firm request for a decision date.'),
 ]),
 (6,'7.A',4,'The final paragraph’s shift from the river’s width to another kind of “distance” has the effect of',2,[
 ('minimizing the physical inconvenience caused by the closed bridge.','The testimony has emphasized that inconvenience throughout.'),
 ('suggesting that natural changes caused the council’s delay.','The river’s unchanged width explicitly rules out that implication.'),
 ('recasting the delay as a gap between recognizing a problem and taking responsibility for a decision.','The metaphor makes accountable action a first form of crossing before construction begins.'),
 ('promising that a speech can physically replace the damaged structure.','The distinction between responsibility and laying boards remains figurative and explicit.'),
 ]),
])

QUESTIONS = STAGE + SEEDS + BRIDGE
