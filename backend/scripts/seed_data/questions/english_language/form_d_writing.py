"""Original Form D revision tasks; studies, organizations, and events are invented."""
from .builders import passage_questions

REHEARSAL_PASSAGE = """(1) At our ensemble's first rehearsal, the conductor asked everyone to play the difficult passage again. (2) We played it louder, but the same entries were late. (3) Repetition had increased our confidence without correcting our coordination. (4) The ensemble should devote part of each rehearsal to short recordings that players review together.

(5) In a two-week trial, one group of twelve musicians recorded a passage, listened once, and identified a particular change to try. (6) Another group of twelve repeated its passage without listening to a recording. (7) The first group made fewer timing errors at its next rehearsal. (8) The groups played different pieces and were taught by different conductors. (9) Recordings therefore guarantee faster improvement for every musician. (10) Still, the trial suggests a method worth testing more carefully.

(11) A recording is useful only if someone decides what to listen for. (12) Players might begin by comparing the moment of an entrance with the phrase immediately before it, rather than ranking which performer sounds best. (13) The aim is to connect an audible problem with an action the group can try. (14) Several members own headphones in the ensemble's colors. (15) Without an agreed question, listening can become a second performance in which everyone defends the first.

(16) Some players are uncomfortable hearing their mistakes in front of others. (17) That concern should shape the procedure. (18) The conductor could start with a group passage, describe one change neutrally, and delete the file after rehearsal unless every recorded player agrees to keep it. (19) A rehearsal recording should not be posted publicly or used to rank members without their knowledge. (20) Clear rules would help distinguish a tool for learning from a permanent record of embarrassment.

(21) Recording and discussion take time that could otherwise be spent playing. (22) The ensemble should begin with one brief passage per rehearsal and review the method after a month. (23) Players could note whether the discussion led to a specific adjustment, while the conductor tracks whether the same problems recur. (24) The best reason to press Record is not to collect evidence that we have practiced, but to discover what our next attempt should change."""

REHEARSAL = passage_questions(passage_id='lang-d-rehearsal', title='Listening between Attempts', mode='writing',
 context='An original fictional draft for a community music newsletter. The ensemble and trial data are invented. The writer proposes a rehearsal method, not a proven universal learning effect.', passage=REHEARSAL_PASSAGE, items=[
 (4,'2.A',3,'Which addition before sentence 1 would best introduce the problem illustrated by the opening anecdote?',2,[
 ('A rehearsal schedule should list every piece in alphabetical order.','Scheduling order does not introduce repetition without useful feedback.'),
 ('An ensemble is successful whenever its members feel confident.','The anecdote distinguishes confidence from improved coordination.'),
 ('Doing a passage again helps only when we have some idea what to do differently.','The sentence introduces the distinction between repetition and informed adjustment.'),
 ('Recording equipment has become a substitute for live performance.','The proposal uses recordings within rehearsal, not instead of performance.'),
 ]),
 (2,'2.B',4,'Which addition after sentence 21 would best address players concerned that discussion will consume rehearsal time?',0,[
 ('The conductor could set a five-minute limit and ask the group to choose one adjustment before playing again.','This gives a concrete boundary and ties discussion to an immediate musical action.'),
 ('Players should accept as much discussion as the conductor prefers because feedback is always beneficial.','This dismisses the time concern and makes an unsupported universal claim.'),
 ('The group could listen repeatedly until every member agrees that the original attempt was unsuccessful.','Agreement about failure is not a useful time limit or actionable improvement.'),
 ('Recording should occur only during public concerts so that rehearsals remain unchanged.','This abandons the proposed rehearsal feedback and introduces different privacy and performance concerns.'),
 ]),
 (1,'4.A',2,'Which additional observation would best support the claim that listening led to an actionable adjustment?',3,[
 ('The recorder’s battery lasted for the entire rehearsal.','Battery duration does not show that listening changed the players’ approach.'),
 ('Most players said they preferred the room’s new chairs.','Seating preference does not support the claim about feedback.'),
 ('The conductor owned several recordings of professional ensembles.','Ownership does not show how these players used their own recording.'),
 ('After hearing an early entrance, the group agreed to watch a particular cue and used it on the next attempt.','This connects a detected problem, a chosen response, and an actual subsequent action.'),
 ]),
 (2,'4.A',4,'Which additional evidence would most strengthen a comparison of recording review with repetition alone?',1,[
 ('A survey of which method musicians expected to prefer before trying either one.','Preferences may matter for adoption but do not directly compare learning outcomes.'),
 ('Results from comparable groups assigned to the methods while playing the same passage under the same instructor.','This comparison reduces the piece and instructor differences that complicate the current trial.'),
 ('A count of how many professional musicians own recording devices.','Device ownership does not isolate the effect of reviewing recordings during practice.'),
 ('A second account of the first group’s improvement without information about the comparison group.','More detail about one group would not resolve the principal comparison problem.'),
 ]),
 (4,'4.B',3,'Which revision of sentence 4 best states a defensible thesis for the entire draft?',2,[
 ('Recordings reveal every important feature of musical performance.','The draft does not establish this sweeping claim or address every feature of performance.'),
 ('The ensemble should record all rehearsals because a larger archive always produces better playing.','The proposal emphasizes focused review and limited retention, not archive size.'),
 ('The ensemble should test brief, focused recording reviews with clear time limits and privacy rules.','This states the proposal and anticipates the practical qualifications developed later.'),
 ('Musicians disagree about whether they enjoy hearing recordings of themselves.','This observation identifies an issue without making the draft’s proposed argument.'),
 ]),
 (5,'6.A',2,'Which sentence after sentence 8 best explains why the trial does not justify sentence 9?',0,[
 ('The difference might reflect the pieces or instruction as well as the opportunity to hear a recording.','This explains how the identified differences limit the causal conclusion.'),
 ('The first group contained twelve musicians, which makes its result automatically representative.','Group size alone does not establish representativeness or resolve differing conditions.'),
 ('The second group’s conductor must have intended the players to make errors.','No evidence supports this claim about intention.'),
 ('Because the trial was short, none of its observations can be reported accurately.','A short trial may yield accurate but limited observations; its duration does not make reporting impossible.'),
 ]),
 (3,'6.C',3,'Which revision would most improve the development of the third paragraph?',3,[
 ('Move sentence 14 before sentence 11 to make equipment ownership the paragraph’s central claim.','Headphone colors do not explain effective listening.'),
 ('Delete sentences 12 and 13 so the paragraph relies entirely on the final metaphor.','This removes the concrete method and purpose needed to support the paragraph.'),
 ('Add a list of famous conductors without explaining their connection to the proposed method.','Names alone do not develop the reasoning about actionable feedback.'),
 ('Replace sentence 14 with an example of choosing a clearer cue after locating a late entrance.','This extends the claim with a concrete link between observation and the next action.'),
 ]),
 (5,'8.A',2,'Which revision of sentence 9 best maintains a measured tone appropriate to the limited evidence?',1,[
 ('The result settles the question for all musicians, regardless of experience.','This keeps the unjustified universal conclusion.'),
 ('The result is encouraging, although the differences between the groups prevent a firm conclusion about the method.','The revision acknowledges both the observation and the specific comparison limits.'),
 ('The trial was a disaster because it failed to prove a universal guarantee.','This treats a limited result as worthless and uses an unnecessarily alarmist tone.'),
 ('Anyone who doubts recording review is refusing to listen.','This attacks skeptics instead of evaluating the evidence.'),
 ]),
 (6,'8.A',3,'The writer wants sentence 20 to describe the benefit of privacy rules without promising that discomfort will disappear. Which revision best does so?',0,[
 ('Clear rules can reduce uncertainty about how a recording will be used, even when listening remains uncomfortable.','This identifies a plausible benefit and preserves a meaningful limitation.'),
 ('Clear rules ensure that no player will ever feel embarrassed.','Rules cannot guarantee every participant’s emotional response.'),
 ('Since discomfort is unavoidable, rules about recordings serve no purpose.','The existence of discomfort does not eliminate the value of informed expectations.'),
 ('Clear rules are a majestic shield against every possible misunderstanding.','The exaggerated metaphor overstates the protection and obscures the specific benefit.'),
 ]),
 (7,'8.B',4,'Which revision of sentence 18 most clearly preserves the conditions for retaining a recording?',2,[
 ('After starting with a group passage, the file could be kept if they agreed, describing one change neutrally.','The opening modifier attaches to the file and “they” leaves the required agreement unclear.'),
 ('The conductor could keep any file unless a player publicly explains why it should be deleted.','This replaces affirmative agreement by every player with a burdensome objection process.'),
 ('The conductor could use a group passage to discuss one change neutrally, then delete the file unless every recorded player agrees to retain it.','The actor, purpose, default deletion, and exception are all explicit.'),
 ('The conductor could delete the file before rehearsal unless the group passage describes a neutral change.','This changes both the sequence and the condition and assigns an action to the passage.'),
 ]),
])

TRAIL_PASSAGE = """(1) At the entrance to the riverside trail, a sign reads Easy Walk. (2) Farther along, visitors encounter loose gravel, a narrow gate, and a slope that becomes muddy after rain. (3) The label may accurately describe one visitor's experience while leaving another visitor without the information needed to plan a trip. (4) The parks office should replace broad difficulty labels with descriptions of specific trail conditions.

(5) In a visitor workshop, twelve participants reviewed two sample signs. (6) Most said that a sign listing distance, surface, and gate width helped them decide what else they needed to know. (7) The participants had volunteered after seeing a notice at the visitor center. (8) The workshop proves that the proposed signs meet every visitor's needs. (9) The office should consult people who do not currently visit, as well as those already using the trail.

(10) Measurements should be gathered consistently. (11) Staff could record the narrowest point, the steepest marked section, and the location of benches, then describe when those observations were made. (12) A sign that gives a width without naming the gate it refers to may be precise but still unhelpful. (13) Conditions also change, so the office needs a way to update information after damage or heavy rain. (14) The old sign has stood beside the entrance for eleven years.

(15) Detailed signs can become crowded. (16) One proposal would put a short summary at the entrance and link to a fuller guide through a printed web address and a scannable code. (17) However, a phone should not be the only way to find information essential to deciding whether to enter. (18) A paper guide at the visitor center and a readable entrance summary would give visitors more than one route to the same information. (19) Translations and clear symbols should be tested with the people expected to use them.

(20) Better descriptions do not repair a damaged surface or widen a gate. (21) Staff should record reports of barriers separately from requests to clarify the signs. (22) Otherwise, the park could congratulate itself for describing a problem while leaving that problem untouched. (23) Updating the signs is worthwhile if it supports informed choices and helps identify which physical improvements should come next."""

TRAIL = passage_questions(passage_id='lang-d-trail', title='Beyond an Easy Label', mode='writing',
 context='Original fictional draft for a parks advisory bulletin. Trail details, workshop participants, and proposals are invented; the draft is a composition exercise, not an accessibility standard.', passage=TRAIL_PASSAGE, items=[
 (7,'2.A',4,'Which alternative opening would best establish the draft’s central problem while retaining its measured approach?',1,[
 ('Visitors disagree about trails because some of them do not read carefully enough.','This blames visitors rather than identifying the limits of a broad label.'),
 ('A label can sound reassuring without telling a visitor whether a route fits that visitor’s needs.','This frames the information problem that the specific trail details develop.'),
 ('Every trail should be described with the same word so that visitors recognize it.','Uniform labeling would not address differences in conditions or needs.'),
 ('The parks office should remove all signs until every route has been rebuilt.','This creates an absolute demand that the draft does not support.'),
 ]),
 (8,'2.B',3,'Which addition after sentence 17 best addresses visitors who cannot rely on a phone during a trip?',3,[
 ('The scannable code could be printed in a brighter color.','Visibility does not resolve the absence of a usable phone or connection.'),
 ('Visitors should purchase newer phones before using the trail.','This imposes an unnecessary barrier instead of providing the information.'),
 ('The online guide could contain more photographs than the printed sign.','Additional online material does not provide an offline route to essential information.'),
 ('The entrance sign should include essential conditions directly, including any known point where a visitor may need to turn back.','This makes a planning decision possible without depending on a device.'),
 ]),
 (2,'2.B',2,'Which addition after sentence 13 would best address staff responsible for maintaining the signs?',0,[
 ('The plan should identify who checks reported changes and who replaces an outdated notice.','This clarifies operational responsibility for the update process.'),
 ('The plan should assume that visitors will correct every notice themselves.','This leaves staff responsibilities undefined and assumes unverified public maintenance.'),
 ('The office should count the number of signs without checking their contents.','An inventory alone does not keep changing information accurate.'),
 ('Staff should use the longest possible descriptions at every location.','Length does not determine accuracy or maintainability.'),
 ]),
 (3,'4.A',3,'Which evidence would best support the claim that a description is useful for planning, rather than merely preferred?',2,[
 ('A count of how many participants liked the sign’s border color.','Aesthetic preference does not show successful interpretation of trail conditions.'),
 ('The office’s total expenditure on printing in the previous year.','Printing expenditure does not measure whether visitors can plan a route.'),
 ('A trial in which varied users use the description to identify relevant conditions and explain any remaining uncertainty.','This tests how the information supports decisions instead of asking only whether the sign is liked.'),
 ('The number of words in the longest existing trail notice.','Word count does not establish decision usefulness.'),
 ]),
 (6,'4.A',2,'Which observation would most directly support sentence 13?',1,[
 ('The office ordered all signs from the same printer.','A shared printer does not show that trail conditions change.'),
 ('After a storm, a fallen branch narrowed a section previously described as clear.','This provides a specific instance in which an earlier description needs updating.'),
 ('Several visitors preferred a green heading to a blue heading.','Color preference does not establish a change in physical conditions.'),
 ('The visitor center sells maps of several parks.','Map sales do not show that this trail’s conditions have changed.'),
 ]),
 (9,'4.C',4,'Which revision of sentence 8 best qualifies the conclusion in light of sentences 5–7?',3,[
 ('The workshop proves that anyone who did not attend would reject the new signs.','Nonattendance supplies no evidence of rejection.'),
 ('The participants’ responses establish that the proposed signs require no further testing.','A small self-selected group cannot settle every user’s information needs.'),
 ('The responses have no relevance because the participants volunteered.','Self-selection limits generalization but does not erase the participants’ actual experiences.'),
 ('The responses suggest that specific descriptions may help, but a self-selected group cannot represent every potential visitor.','This retains the useful finding while identifying the population limit.'),
 ]),
 (4,'6.C',3,'Which change would best develop the distinction introduced in sentence 20?',0,[
 ('Add an example in which reporting a narrow gate leads both to a clearer notice and to review of whether the gate can be altered.','This illustrates separate informational and physical responses to the same barrier.'),
 ('Replace the final paragraph with another description of the sign’s color.','This removes rather than develops the distinction between information and physical access.'),
 ('State that publishing a gate’s width makes its width irrelevant.','Information does not eliminate the physical constraint.'),
 ('Delete sentence 21 so reports of barriers and unclear language are treated as identical.','Combining the reports would conceal the distinction the paragraph needs to explain.'),
 ]),
 (3,'6.A',4,'Which addition after sentence 7 would best explain why the consultation proposed in sentence 9 matters?',2,[
 ('Volunteer workshops are always less accurate than mailed surveys.','The draft does not establish a universal ranking of research methods.'),
 ('Every person who avoids a trail does so because its signs are confusing.','This makes an unsupported single-cause claim about nonvisitors.'),
 ('People excluded by current conditions may be missing from a workshop advertised only where existing visitors gather.','This connects recruitment location to a specific gap in the perspectives collected.'),
 ('The visitor center is the only place where an opinion about the trail can be formed.','This contradicts the reason to seek people outside its current users.'),
 ]),
 (5,'6.B',3,'Which phrase at the start of sentence 20 best connects the final paragraph to the preceding recommendations?',1,[
 ('Because clear information is unnecessary,','This contradicts the draft’s central proposal.'),
 ('Even when information is clear and available,','This acknowledges the recommendations’ value before introducing a limit they cannot overcome.'),
 ('For the same reason that the sign is old,','Age does not logically connect readable information with physical barriers.'),
 ('To demonstrate that all improvements are complete,','The final paragraph argues that physical improvements may remain necessary.'),
 ]),
 (8,'8.A',4,'Which revision of sentence 22 best preserves its criticism in a professional tone?',3,[
 ('The office would be foolish to think signs matter at all.','This attacks the office and rejects the informational value the draft defends.'),
 ('The park’s glorious signs will finally conquer every obstacle.','This exaggeration obscures the distinction between description and repair.'),
 ('Visitors must stop expecting the office to do anything beyond providing words.','This shifts blame to visitors and abandons the draft’s recommendation.'),
 ('Otherwise, improved descriptions could be mistaken for progress on the physical barriers they identify.','This states the risk precisely without disparaging people or denying the value of descriptions.'),
 ]),
 (7,'8.C',2,'Which revision correctly joins the two independent clauses in sentence 13?',0,[
 ('Conditions also change; therefore, the office needs a way to update information after damage or heavy rain.','A semicolon separates the independent clauses, with punctuation around the conjunctive adverb.'),
 ('Conditions also change, therefore the office needs a way to update information after damage or heavy rain.','A comma alone does not correctly join these independent clauses.'),
 ('Conditions also change therefore the office needs a way to update information after damage or heavy rain.','The clauses are fused without appropriate punctuation.'),
 ('Conditions also change; and because the office needs a way to update information after damage or heavy rain.','The material after the semicolon is a dependent fragment rather than an independent clause.'),
 ]),
])

QUESTIONS = REHEARSAL + TRAIL
