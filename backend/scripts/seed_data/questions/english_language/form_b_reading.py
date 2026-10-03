"""Second independent reading form; original fictional essays and correspondence."""
from .builders import passage_questions

MUSEUM_PASSAGE = """[1] At the entrance to our museum's portrait gallery, a visitor recently asked where the famous painting was. I pointed toward the far wall. She thanked me, hurried past seventeen other portraits, photographed the eighteenth, and left. It would be easy to tell this story as evidence that visitors no longer know how to look. As a curator, however, I must admit that we had helped plan her journey. Our poster showed only the eighteenth portrait. Our ticket described it as unmissable. She had followed our instructions with remarkable efficiency.

[2] Museums need recognizable works. A celebrated painting can persuade someone who has never entered a gallery to cross its threshold, and there is no virtue in an institution so pure that no one visits it. But when recognition becomes the promised reward, an encounter with art can shrink to the confirmation that a familiar image really exists. The visitor arrives already knowing what she is expected to find. Looking becomes a task that can be completed.

[3] Last spring, we moved a small, unsigned portrait beside the celebrated one. Its subject holds a glove awkwardly; the paint around one hand has been revised several times. The new label asked why a painter might keep changing a hand. It did not identify the final revision as the correct one. Visitors began pointing to the glove, arguing about whether the subject looked impatient or uncertain, and returning to the famous portrait to inspect its hands. The unsigned work had not become a celebrity. It had become a question that made its neighbor less settled.

[4] I cannot prove that every visitor looked longer. We did not conduct a controlled study, and a crowded room can make lingering unpleasant. Nor should a museum require a prolonged encounter from someone who has come for a brief moment of pleasure. The change matters to me for another reason: it altered what our arrangement invited. A gallery can offer a route through known achievements, or it can give viewers a reason to notice what their first glance leaves unresolved. Both may be useful; the second is too easily sacrificed to the first.

[5] Our next exhibition will still need a poster. It will still have a work that draws people through the door. But beside its reproduction I would like to print a detail that resists instant recognition: an unfinished sleeve, perhaps, or the edge of an uncertain smile. An invitation need not reveal the entire experience in advance. Sometimes its most honest promise is that there will be something left to see."""

MUSEUM = passage_questions(passage_id='lang-b-museum', title='Something Left to See', mode='reading',
    context='Original practice essay: a fictional curator reflects on gallery design for readers of an arts magazine.', passage=MUSEUM_PASSAGE, items=[
    (8, '1.B', 4, 'The writer’s admission that “we had helped plan her journey” most directly responds to readers who might', 1, [
        ('assume that publicity has no influence on the number of museum visitors.', 'The admission concerns the kind of visit encouraged, not chiefly the number of visitors attracted.'),
        ('blame the visitor’s hurried behavior entirely on her own priorities.', 'By listing the poster and ticket instructions, the curator shares responsibility for the visitor’s narrow focus.'),
        ('believe that curators should hide the location of celebrated works.', 'The writer continues to value recognizable works and does not recommend concealing them.'),
        ('expect the essay to compare the monetary values of the portraits.', 'Neither the admission nor its supporting details address market values.'),
    ]),
    (2, '3.B', 3, 'Which statement best expresses the essay’s main position?', 3, [
        ('Museums should display unsigned paintings primarily to correct the prices assigned by collectors.', 'The unsigned portrait matters because it prompts inquiry, not because its market price needs correction.'),
        ('Visitors should be taught to spend the same amount of time on every work in a gallery.', 'Paragraph 4 explicitly respects brief visits and does not prescribe equal viewing time.'),
        ('Familiar images offer deeper pleasure than unfamiliar details because recognition creates confidence.', 'The essay acknowledges recognition’s value but argues that uncertainty can deepen looking.'),
        ('Museums can use familiar works to attract visitors while arranging encounters that reopen curiosity.', 'The writer retains publicity and famous works while advocating invitations to notice unresolved details.'),
    ]),
    (6, '3.A', 4, 'The return to the famous portrait at the end of paragraph 3 supports which inference?', 0, [
        ('Attention to an unfamiliar work can change how viewers approach a familiar one.', 'Discussion of the glove sends visitors back to examine the famous portrait’s hands, altering the comparison.'),
        ('Visitors ultimately preferred the famous portrait because the unsigned one was unfinished.', 'Returning to inspect hands does not establish a preference or rejection of the unsigned portrait.'),
        ('The unsigned portrait’s uncertain authorship was the main cause of visitors’ disagreement.', 'Their disagreement concerns the subject’s expression and the revised hand, not the painter’s identity.'),
        ('The new arrangement showed that the famous painter had copied the unsigned portrait.', 'The passage provides no evidence of copying or a historical relationship between the works.'),
    ]),
    (5, '5.A', 3, 'The argument in paragraph 2 depends most directly on distinguishing', 2, [
        ('the value of a museum visit from the cost of advertising it.', 'Advertising costs are not discussed; the paragraph distinguishes forms of experience.'),
        ('a painter’s intention from a curator’s interpretation of the work.', 'The paragraph does not investigate the painter’s intention.'),
        ('attracting a viewer through recognition from sustaining an open encounter with a work.', 'The writer accepts recognition as an entrance while questioning recognition as the entire reward.'),
        ('the enjoyment of reproductions from the superior monetary value of originals.', 'The concern is how looking is framed, not the price difference between original and reproduction.'),
    ]),
    (5, '5.B', 2, 'The placement of the gallery experiment in paragraph 3 chiefly allows the writer to', 1, [
        ('establish the museum’s history before describing a recent advertising campaign.', 'The example is not an institutional history; it follows a general problem with a possible response.'),
        ('give a concrete example of an alternative to the recognition-focused visit just described.', 'The arrangement turns a familiar image into a subject of renewed inquiry, exemplifying the alternative.'),
        ('supply a counterargument that the final two paragraphs completely reject.', 'The writer qualifies the evidence but continues to endorse the arrangement’s invitation.'),
        ('prove a statistical claim introduced in the first paragraph.', 'No statistical claim is introduced, and paragraph 4 explicitly limits the experiment’s evidentiary force.'),
    ]),
    (7, '7.B', 3, 'In “The unsigned work had not become a celebrity. It had become a question,” the paired sentences emphasize', 0, [
        ('a change in the work’s function for viewers rather than an increase in its fame.', 'The repeated construction distinguishes prompting inquiry from becoming another object of recognition.'),
        ('the curator’s uncertainty about whether the work should remain in the exhibition.', 'The question is metaphorical; the curator does not express indecision about keeping the painting.'),
        ('a contrast between the painter’s intended subject and the viewers’ mistaken interpretation.', 'No authoritative account of the painter’s intention is provided.'),
        ('the inability of museum labels to convey factual information about unfamiliar works.', 'The passage shows a label doing useful work by inviting inquiry, not failing to communicate facts.'),
    ]),
    (6, '7.A', 4, 'The description of the famous portrait as “less settled” suggests that the new arrangement', 3, [
        ('makes the painting’s place in the permanent collection less secure.', 'The phrase concerns interpretation, not whether the museum will retain the work.'),
        ('casts doubt on the accuracy of the museum’s restoration techniques.', 'The revised hand belongs to the unsigned portrait and no restoration dispute is raised.'),
        ('replaces the famous portrait’s established meaning with one final new interpretation.', 'The arrangement generates questions and competing observations rather than a single new verdict.'),
        ('loosens viewers’ sense that familiarity has already exhausted what the painting offers.', 'Looking again at its hands makes the familiar work newly open to investigation.'),
    ]),
    (7, '3.C', 2, 'The qualifications in paragraph 4 mainly prevent readers from concluding that the writer', 2, [
        ('values the invitation to look differently even without a measured change in viewing time.', 'This is what the paragraph explicitly says, not the interpretation it prevents.'),
        ('thinks crowded galleries can affect visitors’ willingness to linger.', 'The writer acknowledges that effect directly.'),
        ('has proved that every visitor benefits from spending longer in the gallery.', 'The writer denies a controlled result and respects brief visits, limiting both the factual and prescriptive claim.'),
        ('wants future exhibitions to continue using familiar works in publicity.', 'The final paragraph explicitly retains that practice.'),
    ]),
])

CLOCK_PASSAGE = """[1] You ask whether the new electric clocks at the works have made our mornings easier. They have made them more exact. Those are not always the same achievement. Before the clocks were fitted, the foreman rang the bell when the first light reached the upper windows. On a cloudy day he consulted his watch; on a bitter morning he sometimes waited for the men coming over the hill. No one called this arrangement scientific, but everyone knew where judgment entered it.

[2] Now a clock at the gate records each arrival on a card. The clerk can tell you, to the minute, who came after the appointed hour. I do not deny the improvement. The foreman can no longer favor a friend by pretending not to notice his lateness. A worker who has arrived on time has a record that does not depend on a superior's memory. Several of us welcomed the change for precisely that reason.

[3] Yet the card has no column for the tram that stopped halfway up the hill, or for the mother who found the school door unexpectedly locked. These circumstances are not all alike, and some explanations will be false. That is an argument for hearing them carefully, not for deciding that nothing outside the card can matter. The machine has made the arrival visible. It has not made the circumstances disappear.

[4] Yesterday the manager showed us a table of late arrivals. The figures were neatly ruled, the totals correct. He said the table at last gave him the facts without anyone's opinion. I wondered about the decision to call one minute late a lost quarter-hour of pay. No wire in the clock had made that decision. A person had made it, and now the printed figures seemed to lend it the machine's authority. The argument had not ended; it had moved into the rule by which the figures were used.

[5] I would keep the clocks. I would also keep a place where a worker can ask what the record means and explain what it leaves out. Perhaps you will say this makes a simple arrangement complicated. But the complications were here before the electrician arrived. We have acquired a better instrument for marking time. We must still decide how to spend our judgment."""

CLOCK = passage_questions(passage_id='lang-b-clock', title='Letter from the Works', mode='reading',
    context='Original fictional letter set in an early twentieth-century industrial town. A factory employee replies to a relative; it is not a historical primary source.', passage=CLOCK_PASSAGE, items=[
    (7, '1.A', 3, 'The writer’s primary purpose in replying to the relative is to', 0, [
        ('explain why more precise records do not remove the need for fair human judgment.', 'The letter accepts accurate clocks while examining the choices and omissions involved in their use.'),
        ('persuade the relative to apply for a position operating the new equipment.', 'The relative’s employment is not discussed; the opening question concerns the clocks’ effect.'),
        ('describe the electrical mechanism that makes factory clocks more accurate.', 'The mechanism is not explained; the letter addresses social and managerial consequences.'),
        ('celebrate the replacement of discretionary rules with universally accepted standards.', 'The worker disputes the fairness of the pay rule even while accepting precise records.'),
    ]),
    (4, '3.B', 4, 'Which sentence most directly states the distinction developed throughout the letter?', 2, [
        ('“On a cloudy day he consulted his watch.”', 'This illustrates the old procedure but does not state the broader distinction.'),
        ('“Several of us welcomed the change for precisely that reason.”', 'This acknowledges one benefit without stating the relationship between data and judgment.'),
        ('“The machine has made the arrival visible. It has not made the circumstances disappear.”', 'The paired claims distinguish a precise observation from the contextual judgment needed to use it fairly.'),
        ('“The figures were neatly ruled, the totals correct.”', 'This concedes the table’s formal accuracy but leaves its implications unstated.'),
    ]),
    (1, '3.A', 4, 'The example of the punctual worker’s card in paragraph 2 is important because it', 3, [
        ('establishes that every dispute about arrival times can now be resolved automatically.', 'A record can help establish time of arrival without resolving disputes about circumstances or penalties.'),
        ('shows that workers’ memories are generally less reliable than their supervisors’ memories.', 'The example contrasts an independent record with dependence on a superior, not the relative quality of two memories.'),
        ('implies that the employee who wrote the letter had previously been punished for lateness.', 'The passage does not establish that personal history.'),
        ('acknowledges that the same technology being questioned can protect workers from arbitrary treatment.', 'The card reduces dependence on a superior’s selective memory, making the critique qualified rather than anti-technology.'),
    ]),
    (3, '5.C', 4, 'The tram and school-door examples in paragraph 3 primarily', 1, [
        ('demonstrate two circumstances that should automatically receive identical treatment.', 'The next sentence expressly says the circumstances are not all alike.'),
        ('make concrete the kind of relevant information an arrival record cannot contain.', 'The examples show why a timestamp alone may be insufficient for judging responsibility.'),
        ('establish that all late arrivals result from unavoidable public-service failures.', 'The writer admits that some explanations will be false and makes no universal causal claim.'),
        ('prove that the old foreman’s judgments were consistently fair to parents and commuters.', 'They illustrate missing context in the new system, not the accuracy of all past decisions.'),
    ]),
    (8, '7.B', 3, 'The short sentence “No wire in the clock had made that decision” chiefly emphasizes', 2, [
        ('the writer’s uncertainty about how the electric clock transmits information.', 'The statement is rhetorical rather than a question about electrical engineering.'),
        ('the difference between the new clock’s accuracy and the old watch’s accuracy.', 'The comparison concerns who chooses a penalty, not relative timekeeping accuracy.'),
        ('human responsibility for a penalty that is being presented with mechanical authority.', 'The sentence separates the chosen pay rule from the instrument that records time.'),
        ('the possibility that a technical fault caused the quarter-hour deduction.', 'The writer identifies a deliberate rule, not a malfunction.'),
    ]),
    (5, '7.A', 2, 'The final phrase “spend our judgment” connects judgment to time in order to suggest that', 1, [
        ('workers should be paid according to their ability to explain their decisions.', 'The phrase does not propose a new wage system.'),
        ('careful decision making remains a responsibility requiring attention after measurement improves.', 'The economic verb extends the discussion of time and pay to the continuing use of human judgment.'),
        ('judgment can be recorded as precisely as arrival times.', 'The letter repeatedly distinguishes contextual judgment from measurable timestamps.'),
        ('the new clocks have increased the length of the working day.', 'No change in working hours is established.'),
    ]),
    (9, '3.C', 3, 'The acknowledgment that some explanations will be false strengthens the argument by', 0, [
        ('showing that the proposed hearing process must discriminate among cases rather than accept every excuse.', 'The writer anticipates abuse but treats it as a reason for careful evaluation, not for eliminating hearings.'),
        ('conceding that the manager’s table includes every fact needed to assign responsibility.', 'The writer continues to argue that circumstances outside the table can matter.'),
        ('identifying dishonesty as the sole source of disagreement over factory rules.', 'The examples also involve genuine delays and the chosen penalty formula.'),
        ('retreating from the proposal to let workers challenge interpretations of their records.', 'The final paragraph explicitly renews that proposal.'),
    ]),
    (7, '7.C', 4, 'In “The argument had not ended; it had moved into the rule by which the figures were used,” the semicolon helps connect', 3, [
        ('a reported fact with an unrelated personal memory.', 'Both clauses interpret the same dispute over the meaning of the records.'),
        ('an accusation about inaccurate totals with proof of a calculation error.', 'The totals are described as correct; the objection concerns the rule applied to them.'),
        ('two explanations offered as equally likely alternatives.', 'The second clause explains the first rather than offering an alternative explanation.'),
        ('a rejection of apparent closure with an explanation of where the unresolved issue now resides.', 'The second clause specifies how the disagreement persists despite the accurate table.'),
    ]),
])

BIRDS_PASSAGE = """[1] The first map from our neighborhood bird survey looked reassuringly green along the river and almost blank beside the railway. A volunteer suggested we had already learned where the birds preferred to live. Before printing the map, however, we plotted something less beautiful: the routes our volunteers had walked. Most followed the river path. Almost none crossed the busy road to the railway lots. Our map might have described the birds. It certainly described us.

[2] This is not a reason to dismiss observations made by volunteers. A person who passes the same hedge every morning may notice a change that a visiting researcher misses. Local attention can make a survey more detailed, more frequent, and more responsive than a small research team could manage alone. But attention is unevenly distributed. Some places are pleasant to visit, some feel unsafe, and some are difficult to reach without a car. A large collection of observations can preserve these inequalities rather than cancel them.

[3] We therefore added a second layer to the map: observation effort. A blank area now carried a note when no one had surveyed it. We arranged paired visits to less accessible sites and offered an early bus fare to volunteers who needed it. The new records did not instantly reverse the first pattern. There were still more reported species by the river. What changed was our ability to ask a better question: how much of that difference remained when places received comparable attention?

[4] Some volunteers worried that the extra records—minutes spent, route followed, weather encountered—would turn a joyful walk into paperwork. They were not wrong about the burden. A survey that demands too much from its contributors can become accurate in principle and empty in practice. We reduced the form to information that would change our interpretation and explained why each item mattered. We also retained a place for unexpected observations that did not fit the checkboxes. Standardization should make accounts comparable, not make surprise impossible.

[5] When we presented the revised map, the railway lots were no longer silent white spaces. Some had bird records; others were plainly marked as places where we still knew little. The map was less tidy and more useful. It no longer offered an effortless answer to where life flourished. It showed where people had looked, what they had noticed, and where the next walk could begin."""

BIRDS = passage_questions(passage_id='lang-b-birds', title='A Map of Where We Looked', mode='reading',
    context='Original practice essay: a fictional citizen-science organizer writes for volunteers about interpreting a neighborhood bird survey.', passage=BIRDS_PASSAGE, items=[
    (1, '1.A', 4, 'The opening scene establishes the need to distinguish', 1, [
        ('the preferences of professional researchers from those of amateur birdwatchers.', 'The problem identified is uneven survey coverage, not a comparison between professional and amateur preferences.'),
        ('a pattern in reported sightings from the underlying distribution of birds.', 'The route map reveals that apparent bird differences may partly reflect where observations occurred.'),
        ('the visual attractiveness of river birds from that of birds near railway lines.', 'The passage describes the map’s appearance, not differences in birds’ attractiveness.'),
        ('the reliability of electronic maps from that of handwritten field notes.', 'No comparison of recording technologies is made.'),
    ]),
    (2, '1.B', 2, 'The statement “They were not wrong about the burden” primarily helps the writer', 3, [
        ('announce that the survey will abandon all common reporting requirements.', 'The response is to simplify and explain useful fields, not eliminate standardization.'),
        ('suggest that volunteers care less about accuracy than researchers do.', 'The writer treats the burden as a legitimate design concern, not a failure of commitment.'),
        ('explain why only paid contributors can supply dependable observations.', 'The essay continues to value and improve volunteer participation.'),
        ('acknowledge contributors’ experience before describing a workable adjustment.', 'The concession validates the concern and introduces a shorter, purposefully designed form.'),
    ]),
    (3, '5.A', 3, 'Which inference does paragraph 3 most clearly support?', 0, [
        ('Accounting for observation effort improves interpretation even if the reported pattern remains similar.', 'The river still has more reported species, but comparable attention permits a better question about that difference.'),
        ('Equal numbers of visits would necessarily produce equal numbers of species at every site.', 'The paragraph improves comparability without assuming that the underlying habitats are identical.'),
        ('The original river sightings were inaccurate because they were collected more frequently.', 'Uneven sampling does not make each individual sighting false.'),
        ('Providing bus fares establishes that habitat differences no longer influence bird distribution.', 'Bus access changes observation opportunities, not all ecological differences.'),
    ]),
    (6, '3.A', 3, 'The example of a person passing the same hedge every morning illustrates', 2, [
        ('why familiar places should be the only locations included in a survey.', 'The writer later advocates sampling less familiar and less accessible sites as well.'),
        ('why observations cannot be compared when different people collect them.', 'Repeated local observation is presented as a benefit; comparability can be improved through survey design.'),
        ('how sustained local attention can contribute information that brief visits miss.', 'Frequent familiarity may reveal changes unavailable to an occasional visiting researcher.'),
        ('how a researcher can eliminate the need to record observation effort.', 'The example does not remove the importance of measuring how often places are observed.'),
    ]),
    (2, '3.B', 4, 'Which statement best describes the relationship between the essay’s main claim and its view of volunteer data?', 3, [
        ('The data are celebrated as valuable because collecting enough observations automatically removes bias.', 'The essay expressly warns that a large collection can preserve unequal attention.'),
        ('The data are rejected as unreliable because volunteers choose where to walk.', 'The essay improves survey design while retaining the value of volunteer contributions.'),
        ('The data are treated as useful only when contributors stop making unplanned observations.', 'The form retains room for surprises that do not fit its checkboxes.'),
        ('The data are valued, but their interpretation must account for the circumstances in which they are gathered.', 'The essay pairs the strength of local observation with attention to sampling effort, access, and reporting burden.'),
    ]),
    (4, '5.C', 2, 'The contrast between the first and revised maps chiefly develops the argument by', 1, [
        ('comparing two neighborhoods with identical ecological conditions.', 'Both maps concern the same survey area, and ecological equality is not established.'),
        ('showing how a change in method alters what readers can reasonably conclude.', 'Effort labels distinguish no sightings from little observation and guide more cautious interpretation.'),
        ('tracing the historical development of railway land use.', 'The railway is part of the sampling example, not the subject of a historical account.'),
        ('ranking bird species by their importance to residents.', 'No species ranking is presented.'),
    ]),
    (6, '7.A', 2, 'Calling the original railway areas “silent white spaces” highlights how the map could', 0, [
        ('make a lack of observation look like an absence of life or information worth seeking.', 'The revised labels reveal that some blanks indicate what observers do not yet know.'),
        ('show that railway noise prevents residents from hearing any birds.', 'The silence is a description of the map’s missing information, not a measured acoustic finding.'),
        ('confirm that the railway lots lack the vegetation birds need.', 'The map cannot establish that ecological explanation without adequate observations.'),
        ('demonstrate that color printing gives less accurate results than black-and-white printing.', 'Color is used figuratively to discuss representation, not printing technology.'),
    ]),
    (9, '3.C', 2, '“Standardization should make accounts comparable, not make surprise impossible” qualifies the proposal by insisting that', 2, [
        ('every unexpected observation should be accepted without verification.', 'Keeping a place for unexpected observations does not eliminate the need for verification.'),
        ('survey forms should record every detail regardless of how it will be used.', 'The preceding sentence says the form was reduced to information that changes interpretation.'),
        ('shared reporting rules should leave room for relevant observations outside preset categories.', 'The statement balances comparability with the flexibility needed to notice unanticipated findings.'),
        ('comparability matters only when a survey produces surprising results.', 'The writer values comparability generally and adds, rather than substitutes, room for surprise.'),
    ]),
])

QUESTIONS = MUSEUM + CLOCK + BIRDS
