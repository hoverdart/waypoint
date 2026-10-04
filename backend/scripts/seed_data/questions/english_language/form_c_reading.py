"""Third reading form: original public address, nature essay, and civic letter.

All speakers, events, observations, and historical settings below are fictional.
These are original practice texts, not quotations from published authors.
"""
from .builders import passage_questions

SKY_PASSAGE = """[1] When this observatory was proposed, its supporters promised that it would bring the stars closer to our town. Tonight, at its opening, I must begin with a correction: the stars have not moved. Nor has the light from them become younger on its long journey here. What has moved is a door. A room that once existed only in a drawing is now open, and a child who could not reach an eyepiece yesterday may reach one tonight.

[2] I want to thank the people whose names appear on the plaque beside that door. Their gifts bought the telescope and the land beneath it. I also want to name work that would sit awkwardly on a plaque: the bus driver's test journeys up this narrow road, the cleaner's discovery that the red lamps left a step almost invisible, the carpenter's patient rebuilding of a platform after our first trial with a wheelchair. We like to say that a telescope lets us see farther. Before it can do that for everyone, someone must notice what is near.

[3] Some of you will remember my first public lecture, given in the school gymnasium during a rainstorm. I had brought a chart of the planets. A leak opened above it halfway through my account of Mars, and the planet acquired a river I had not intended to discuss. A student asked whether our pictures of other worlds ever needed correcting too. It was a better question than any I had planned. I had been guarding the chart from the rain; she had begun to test what a chart could tell her.

[4] There will be cloudy evenings here. There will be visitors who travel a long way and see no rings around Saturn. We owe them honest notices, comfortable chairs, and more than an apology. The telescope is an instrument, not a promise that nature will perform on schedule. A room full of disappointed visitors can still become a room full of questions, provided we do not treat the questions as a consolation prize. The history of astronomy is not a procession of people who saw exactly what they expected.

[5] So tonight I ask our volunteers to welcome not only the visitor who knows the constellations, but the visitor who asks why the Moon follows the car. Do not hurry that question toward the answer you have rehearsed. Ask what the visitor has noticed. Ask when it happens. A question can be mistaken in its premise and exact in its observation. Teaching begins when we can hear the difference.

[6] Years from now we may count the school groups, the lectures, the nights of clear weather. Let us count them; a public institution should be able to describe its work. But I hope we will also remember a moment too small for an annual table: a visitor stepping back from the eyepiece, looking up without it, and finding the familiar sky newly difficult to take for granted. That will not bring the stars closer. It will make this place worth opening."""

SKY = passage_questions(passage_id='lang-c-sky', title='A Door under the Stars', mode='reading',
    context='Original fictional address by an astronomy educator at the opening of a community observatory, delivered to donors, volunteers, and residents.', passage=SKY_PASSAGE, items=[
    (7, '1.A', 2, 'The speaker’s primary purpose is to', 2, [
        ('explain the optical principles that distinguish an observatory telescope from ordinary binoculars.', 'The telescope’s mechanism is not explained; its public educational role is the focus.'),
        ('persuade donors to replace the telescope with a larger instrument before public visits begin.', 'The speaker celebrates the opening and requests a way of welcoming visitors, not replacement equipment.'),
        ('celebrate the observatory’s opening while defining a welcoming, inquiry-centered mission for it.', 'Thanks to supporters lead into practical and intellectual commitments that give the new institution its purpose.'),
        ('defend professional astronomers against criticism from residents who prefer other public services.', 'No such dispute is introduced; residents are addressed as participants in the opening.'),
    ]),
    (2, '1.B', 3, 'By thanking both named donors and people whose work would “sit awkwardly on a plaque,” the speaker most likely seeks to', 0, [
        ('broaden the audience’s understanding of the contributions that make a public institution accessible.', 'The bus route, lighting, and platform show that access depends on practical work as well as financial gifts.'),
        ('suggest that public recognition of financial gifts is inherently embarrassing.', 'The speaker explicitly thanks the donors and does not propose removing their plaque.'),
        ('assure residents that accessibility improvements were completed without any expense.', 'The examples identify useful labor but provide no information about its cost.'),
        ('separate the observatory’s scientific work from concerns that its staff should leave to contractors.', 'The speaker makes attention to nearby barriers part of the institution’s scientific and public mission.'),
    ]),
    (8, '1.B', 4, 'The concession “Let us count them; a public institution should be able to describe its work” chiefly acknowledges an audience expectation that', 1, [
        ('all meaningful learning outcomes can be reduced to a single annual total.', 'The speaker immediately describes a valuable experience that may not appear in an annual table.'),
        ('an institution supported by the public should provide an account of its activity.', 'Endorsing the counting of visits and lectures recognizes accountability before extending the definition of success.'),
        ('visitors should already understand astronomy before attending a lecture.', 'Paragraph 5 welcomes elementary and even mistaken questions.'),
        ('scientific observations should be published only after residents vote to approve them.', 'The concession concerns institutional reporting, not public approval of scientific findings.'),
    ]),
    (2, '3.B', 3, 'Which statement best captures the central claim developed across the address?', 3, [
        ('The value of an observatory can be measured most accurately by the distance reached by its telescope.', 'The address shifts attention from optical reach to access, curiosity, and teaching.'),
        ('Public astronomy programs succeed when volunteers replace visitors’ mistaken questions with expert vocabulary.', 'The speaker asks volunteers to listen carefully rather than hurry visitors toward rehearsed answers.'),
        ('Unplanned events provide more reliable astronomical evidence than carefully prepared observations.', 'The wet chart illustrates inquiry, not the scientific superiority of accidents.'),
        ('An observatory fulfills its public purpose by making attentive inquiry accessible, not merely by providing equipment.', 'The examples connect physical access, responsive teaching, and renewed curiosity into one institutional mission.'),
    ]),
    (3, '3.A', 4, 'The student’s question about correcting pictures of other worlds supports the speaker’s argument because it', 1, [
        ('confirms that the chart’s depiction of Mars contained a previously unnoticed scientific error.', 'The river is rain damage; the passage does not establish an error in the original chart.'),
        ('shows a learner turning an interruption into a question about the limits of representations.', 'The student moves from a damaged chart to the broader possibility that scientific pictures need revision.'),
        ('demonstrates that visual materials prevent students from developing independent questions.', 'The chart and its unexpected alteration provoke the student’s independent question.'),
        ('proves that the speaker’s planned lecture had taught the student nothing useful.', 'One unplanned question does not establish that the rest of the lecture had no educational value.'),
    ]),
    (3, '5.A', 3, 'The reasoning in paragraph 4 depends on which distinction?', 0, [
        ('The inability to deliver a particular view does not necessarily prevent a worthwhile educational encounter.', 'Clouds may block Saturn, but thoughtful questions can still make the visit valuable.'),
        ('Scientific instruments are useful outdoors but cannot support discussion inside a building.', 'The speaker does not divide educational value by indoor and outdoor locations.'),
        ('Visitors who travel farther are more likely to understand the limitations of astronomy.', 'Travel distance establishes the seriousness of disappointment, not greater understanding.'),
        ('A failed prediction disproves the entire scientific method on which the prediction relies.', 'The history of unexpected observations supports inquiry rather than rejection of scientific methods.'),
    ]),
    (3, '5.C', 2, 'The anecdote about the rain-damaged chart primarily develops the address by', 2, [
        ('presenting statistical evidence that school lectures are less effective than observatory visits.', 'A single remembered incident provides no comparative statistical evidence.'),
        ('defining the technical differences between a map, a photograph, and a scientific diagram.', 'The anecdote raises questions about representations without defining these categories.'),
        ('illustrating through a personal incident the kind of responsive curiosity the speaker later asks volunteers to encourage.', 'The student’s unexpected question prepares for the instruction to listen to what visitors notice.'),
        ('establishing a chronological history of the observatory’s construction.', 'The earlier lecture illustrates an educational principle, not a sequence of construction events.'),
    ]),
    (7, '7.B', 4, 'In paragraph 5, the short sentences beginning “Ask what” and “Ask when” have which rhetorical effect?', 3, [
        ('They interrupt the address with questions the speaker expects the audience to answer aloud.', 'These are commands describing how volunteers should respond to future visitors, not requests for answers now.'),
        ('They create an abrupt shift from encouragement to ridicule of inexperienced visitors.', 'The commands model respectful attention and contain no ridicule.'),
        ('They imply that every visitor’s question can be resolved by only two factual answers.', 'The sentences begin an inquiry; they do not claim to exhaust every question.'),
        ('They turn the general invitation to listen into a concise, repeatable practice for volunteers.', 'The parallel imperatives provide concrete actions that enact the speaker’s teaching principle.'),
    ]),
])

MARSH_PASSAGE = """[1] At low tide the marsh behind my rented room looked like a place the sea had abandoned in a hurry. Channels lay exposed in the mud. A shopping cart stood tilted near the bank, its wheels pointing at a sky that offered no assistance. I had come to write about the coast and had imagined a clean horizon. Instead, my window framed a wet confusion of grass, rubbish, and water that could not decide where to stop.

[2] For the first week I walked past it to the beach. There the boundary was legible: land, a line of foam, sea. My notebook filled with sentences about distance. Then a storm closed the beach path, and I took my morning walk along the marsh. A woman in rubber boots was lifting plastic bags from the reeds. She showed me a strip of grass bent flat in one direction and standing upright just beyond it. The water had been here in the night, she said. I had mistaken its absence for evidence that nothing had happened.

[3] I began returning at different hours. Small fish entered a channel that, two hours later, appeared too shallow to contain them. Birds stood motionless and then struck at something I had not seen. On one afternoon the cart was almost submerged; on another it cast a jagged shadow over dry mud. The cart did not become beautiful. It became a marker by which I could notice change, and also a persistent embarrassment: a useful measure of water, an object that should not have been there.

[4] My first new account of the marsh was full of verbs. The water crept, the grass caught, the mud held. I liked these sentences until I noticed that they made the place sound like a diligent employee, quietly performing services on our behalf. The marsh does slow water and shelter living things, but I had begun to praise it only in the language of what it did for us. This was an improvement on calling it waste ground. It was not the end of the matter.

[5] When the woman returned with two neighbors to remove the cart, I helped pull. Without it the channel looked less familiar. For a moment I resented the loss of my convenient gauge; then I heard how absurd that sounded. Attention had given the object a role in my private education, not a right to remain. The work of looking did not excuse me from the work of carrying something heavy up a slippery bank.

[6] I still walk to the beach when the path is open. I have not traded one correct landscape for another. But my sentences about the coast no longer end so comfortably at the horizon. They return to an edge that advances and retreats, to mud holding yesterday's water, to a place that is neither empty when the tide is out nor complete when it comes in. I had wanted a view I could finish describing. The marsh has given me a reason to keep revising."""

MARSH = passage_questions(passage_id='lang-c-marsh', title='An Unfinished Edge', mode='reading',
    context='Original fictional personal essay for a general-interest nature magazine. Its observations describe an invented coastal setting.', passage=MARSH_PASSAGE, items=[
    (1, '1.A', 4, 'Which account of the essay’s rhetorical situation best explains the writer’s use of first-person errors and revisions?', 1, [
        ('A coastal engineer is reporting measurements to colleagues who need a reproducible flood model.', 'The essay provides reflective experiences rather than technical measurements or a reproducible model.'),
        ('A visitor is inviting general readers to reconsider habits of seeing by tracing changes in the visitor’s own attention.', 'The writer repeatedly admits mistaken expectations and uses those revisions to invite similar reflection.'),
        ('A property owner is documenting damage in order to establish a financial claim against neighbors.', 'The rented room and cleanup supply no property claim or accusation against neighbors.'),
        ('A tour organizer is assuring customers that the marsh offers an unobstructed view of the horizon.', 'The marsh frustrates the clean view initially sought and becomes valuable for different reasons.'),
    ]),
    (2, '3.A', 2, 'The bent strip of grass in paragraph 2 serves as evidence that', 3, [
        ('the woman has intentionally changed the direction in which the marsh plants grow.', 'The woman interprets the grass; the passage attributes its position to recent water.'),
        ('the beach path will remain closed throughout the writer’s stay.', 'The grass indicates prior water movement, not the duration of the path closure.'),
        ('the marsh has permanently dried out since the previous evening.', 'The observation concerns a recurring tide and does not imply permanent drying.'),
        ('the landscape retains signs of activity that is not visible at the moment of observation.', 'The grass records water that has already receded, correcting the writer’s assumption of inactivity.'),
    ]),
    (6, '3.B', 4, 'Which sentence best states the essay’s developing argument rather than only a detail of its narrative?', 0, [
        ('Careful attention can revise an observer’s categories, but appreciation also carries obligations beyond observation.', 'The writer revises ideas of beauty and usefulness, then recognizes that noticing the cart does not excuse leaving it.'),
        ('Removing discarded objects invariably makes a natural landscape easier to understand.', 'The cart’s removal initially makes the channel less familiar; ease of understanding is not the main criterion.'),
        ('A landscape deserves protection only when its practical services can be described precisely.', 'Paragraph 4 explicitly questions valuing the marsh only through services it provides people.'),
        ('Writers should avoid describing places that other people have altered.', 'The essay develops its insight through precisely such an altered place.'),
    ]),
    (5, '5.A', 4, 'Paragraph 5 complicates the role of the cart established in paragraph 3 by distinguishing between', 2, [
        ('objects that are aesthetically pleasing and objects that are made of durable materials.', 'Neither durability nor a newly positive aesthetic judgment explains the removal.'),
        ('the tide’s ability to move an object and a person’s inability to move it.', 'The neighbors and writer do move the cart; physical impossibility is not the distinction.'),
        ('an object’s usefulness to an observer and the justification for leaving that object in a place.', 'The cart helps the writer notice tides, but that private benefit does not justify retaining rubbish in the marsh.'),
        ('a visitor’s legal ownership of an object and a resident’s claim to that same property.', 'No ownership dispute appears; the issue is the writer’s responsibility to help remove the cart.'),
    ]),
    (5, '5.B', 3, 'The transition from paragraph 3 to paragraph 4 moves the essay from', 1, [
        ('an abstract definition of environmental responsibility to a history of coastal settlement.', 'Paragraph 3 reports observations, and paragraph 4 examines the writer’s language rather than settlement history.'),
        ('changes in what the writer notices to scrutiny of the language used to describe those changes.', 'After recounting recurring observations, the writer evaluates the verbs and implied values in a new draft.'),
        ('a criticism of residents’ behavior to a complete defense of their cleanup methods.', 'The residents are not criticized, and paragraph 4 addresses prose rather than cleanup methods.'),
        ('a sequence of scientific measurements to an argument that evidence is unnecessary.', 'The observations are informal, and the writer never rejects evidence.'),
    ]),
    (8, '7.A', 3, 'The comparison of the marsh to “a diligent employee” chiefly conveys the writer’s concern that', 0, [
        ('apparently appreciative language can still value a place only for the services it supplies people.', 'The employee comparison exposes the human-centered standard implicit in the writer’s praise.'),
        ('marsh processes operate on a predictable working schedule determined by residents.', 'The comparison concerns valuation, not a literal schedule or human control of tides.'),
        ('the woman should receive wages for every hour spent collecting discarded objects.', 'The comparison describes the marsh in the writer’s prose, not a compensation proposal.'),
        ('active verbs cannot accurately describe changes in a natural environment.', 'The writer questions the implied frame of the verbs, not their ability to describe real action.'),
    ]),
    (8, '7.B', 2, 'The paired sentences “The cart did not become beautiful. It became a marker” emphasize that', 3, [
        ('the writer has forgotten the object’s original function as a shopping cart.', 'The writer continues to identify the object and later helps remove it.'),
        ('the cart changes physically between the writer’s first two observations.', 'The emphasis is on its changed significance to the observer, not a physical transformation.'),
        ('a useful object must also be visually attractive to deserve attention.', 'The two sentences explicitly separate usefulness as a marker from beauty.'),
        ('the writer’s attention changes without requiring a new judgment that the cart is attractive.', 'The repeated subject makes the contrast between aesthetic approval and observational function explicit.'),
    ]),
    (7, '7.C', 3, 'The colon in “a persistent embarrassment: a useful measure of water, an object that should not have been there” introduces language that', 2, [
        ('lists the chronological steps by which the cart entered the marsh.', 'The phrases describe competing meanings of the cart, not its arrival.'),
        ('replaces the earlier description with an unrelated scenic detail.', 'Both phrases explain why the same cart is an embarrassment.'),
        ('explains the embarrassment through two simultaneously true but ethically conflicting descriptions.', 'The cart assists observation while remaining misplaced rubbish; the colon unfolds that tension.'),
        ('identifies the person legally responsible for removing the abandoned object.', 'No person or legal duty is identified after the colon.'),
    ]),
])

LIBRARY_PASSAGE = """[1] To the members of the reading-room committee: You have asked why the proposed evening hours are necessary when the room is already open six days each week. I can answer first with a fact about the timetable. On each of those days the door closes at five. At five the machinists are still at the works, the seamstresses are finishing orders, and the shop assistants are waiting for their employers to turn the key. Six days of an inaccessible hour do not make one accessible evening.

[2] I have heard it said that the room is quiet in the afternoons, and that this proves the town has little appetite for books. Yesterday I counted eleven readers. This is a useful count of the people who could come yesterday afternoon. It is not a count of the people who wished to come and could not. If we infer desire only from attendance, and arrange attendance so that many are excluded, we have made a neat circle in which our own rule supplies its own defense.

[3] The objection about expense deserves a less easy answer. Lamps must be filled, the stove tended, and someone paid to remain until closing. I do not propose that the attendant give us these hours as a gift. Nor do I claim that adding evenings will immediately fill every chair. The committee could open on two evenings for a period of eight weeks, recording use and expenditure separately. Such a trial would cost money. It would also purchase information our present timetable cannot give us.

[4] Another objection is more curious: that workers coming from the shops will use the room chiefly for newspapers rather than serious books. Suppose they do. A person following a dispute about water rates may have a more urgent reason to read than a person dutifully beginning a celebrated history. We should be cautious about measuring the seriousness of a reader by the thickness of the volume on the table. The room's rules require quiet conduct and care of its property; they do not require every reader to arrive with the committee's preferred question.

[5] I would welcome a report after the trial that found our chosen evenings inconvenient or our arrangements too costly. We could alter the hours or decline to continue. What I cannot accept is a report that calls an untried arrangement unnecessary because the people it would serve are absent from the arrangement we already have. Let us ask a question whose answer we have not fixed in advance. Open the door after the work bell, and then count who comes through it."""

LIBRARY = passage_questions(passage_id='lang-c-library', title='After the Work Bell', mode='reading',
    context='Original fictional civic letter set in a nineteenth-century town. A resident petitions the committee of a subscription-supported public reading room. This is not a historical primary source.', passage=LIBRARY_PASSAGE, items=[
    (2, '1.B', 4, 'In paragraph 3, the writer most directly accommodates committee members who value', 2, [
        ('the preservation of daytime attendance as the only acceptable measure of interest.', 'The writer challenges that measure and proposes collecting new evidence.'),
        ('the replacement of paid attendants with unpaid volunteers.', 'The writer explicitly refuses to ask the attendant to donate the additional hours.'),
        ('financial responsibility and the possibility of revising a policy after evaluating its results.', 'The limited trial, separate records, and willingness to discontinue recognize cost and accountability concerns.'),
        ('a guarantee that every new opening hour will immediately fill the room.', 'The writer explicitly declines to promise immediate full attendance.'),
    ]),
    (4, '1.A', 3, 'The writer’s immediate purpose is to persuade the committee to', 0, [
        ('test evening access before drawing conclusions about the demand for it.', 'The letter asks for an eight-week trial so the committee can evaluate demand it currently cannot observe.'),
        ('close the room during afternoons and permanently replace all daytime hours.', 'The proposal adds two evenings temporarily; it does not abolish daytime access.'),
        ('eliminate every rule governing how readers use the room.', 'Quiet conduct and care of property are affirmed as legitimate rules.'),
        ('purchase only newspapers until workers become interested in longer books.', 'The newspaper example challenges a hierarchy of reading purposes, not the acquisition policy.'),
    ]),
    (2, '3.B', 2, 'Which statement most directly expresses the main claim of paragraph 2?', 3, [
        ('Eleven readers constitute sufficient attendance to justify any possible expansion of hours.', 'The writer does not treat eleven as a threshold for expansion.'),
        ('A person who does not attend a reading room cannot be interested in public affairs.', 'The paragraph argues against inferring lack of interest from nonattendance.'),
        ('Counting attendance is always less reliable than asking committee members for their opinions.', 'The problem is the restricted circumstances of the count, not counting as a method.'),
        ('Attendance during restricted hours cannot establish the level of interest among people unable to attend then.', 'The paragraph distinguishes observed users from excluded potential users.'),
    ]),
    (7, '3.C', 4, 'The final paragraph qualifies the writer’s position by conceding that', 1, [
        ('the current timetable has already provided decisive evidence against evening access.', 'The writer repeatedly denies that the present arrangement can answer the question.'),
        ('evidence from a genuine trial could justify changing or abandoning the proposed arrangement.', 'The writer accepts an unfavorable trial report while rejecting a conclusion based on an untested assumption.'),
        ('workers’ reading interests are less serious than those of existing subscribers.', 'Paragraph 4 directly challenges that hierarchy.'),
        ('a successful trial would remove the need to pay for staffing and lighting.', 'The costs remain real; the trial would provide information with which to judge them.'),
    ]),
    (3, '5.C', 3, 'The comparison between a reader following water rates and one beginning a celebrated history primarily', 0, [
        ('offers a contrasting pair of examples that challenges the committee’s proposed measure of serious reading.', 'Urgent civic interest in a newspaper complicates the assumption that a longer prestigious book signals greater seriousness.'),
        ('establishes a universal rule that newspapers contain more accurate information than histories.', 'The examples concern readers’ purposes, not the factual accuracy of the two formats.'),
        ('explains the chronological development of the town’s newspaper industry.', 'No history of that industry is supplied.'),
        ('demonstrates that the committee lacks enough money to buy books.', 'The comparison does not concern purchasing costs or the collection budget.'),
    ]),
    (3, '5.A', 4, 'The phrase “our own rule supplies its own defense” identifies which problem in the committee’s reasoning?', 2, [
        ('It assumes that the cost of lamps will decrease whenever attendance increases.', 'No relationship between lamp cost and attendance is asserted.'),
        ('It treats all objections as equally persuasive regardless of their evidence.', 'The writer addresses different objections separately and does not make this criticism.'),
        ('It uses attendance shaped by a restrictive schedule to justify retaining that same restriction.', 'The rule helps cause the absence that is then interpreted as evidence that changing the rule is unnecessary.'),
        ('It confuses the number of books owned with the number of books borrowed.', 'The argument concerns access and attendance, not collection or borrowing totals.'),
    ]),
    (5, '7.A', 2, 'In context, the description of a “neat circle” conveys the writer’s', 3, [
        ('admiration for the architectural symmetry of the reading room.', 'The circle is a metaphor for reasoning, not a feature of the building.'),
        ('confidence that the committee has considered every possible point of view.', 'The writer argues that potential evening users are missing from its evidence.'),
        ('uncertainty about whether the town has a formal governing committee.', 'The letter is explicitly addressed to that committee.'),
        ('critical view of reasoning that appears orderly because it excludes the very evidence needed to test it.', '“Neat” is ironic: the self-contained reasoning protects itself from information about excluded readers.'),
    ]),
    (7, '7.C', 4, 'The colon following “Another objection is more curious” prepares readers for', 1, [
        ('a direct quotation whose exact wording the writer attributes to a named committee member.', 'The clause summarizes an objection without quotation marks or a named source.'),
        ('an explanation of the objection that the writer will then challenge through contrasting examples.', 'The colon introduces the concern about newspapers; the following sentences question its underlying value judgment.'),
        ('a list of expenses that confirms the preceding paragraph’s financial objection.', 'The objection introduced here concerns reading choices, not operating expenses.'),
        ('an unrelated aside that interrupts the argument without contributing to it.', 'The objection is one of the barriers to evening access that the letter systematically answers.'),
    ]),
])

QUESTIONS = SKY + MARSH + LIBRARY
