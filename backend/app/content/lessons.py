"""Original guided lessons. Examples are fictional instructional scenarios.

Skill categories checked against the AP English Language course overview.
Lesson completion records a learning check, not AP mastery or an exam score.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    slug: str
    title: str
    skill: str
    objective: str
    explanation: tuple[str, ...]
    example: str
    walkthrough: str
    prompt: str
    options: tuple[str, ...]
    feedback: tuple[str, ...]
    correct: int
    revision: int = 1


FOUNDATIONS = (
    Lesson(
        slug="read-the-situation", title="Read the situation before the sentence", skill="1.A",
        objective="Connect a writer's choice to the audience, occasion, and intended response.",
        explanation=(
            "Start with who is speaking, to whom, and why now. The topic is what a text discusses; the purpose is what the writer wants readers to think, feel, or do about it. A text about library hours might seek a policy change, explain a budget decision, or reassure worried families.",
            "Look for evidence of audience needs rather than inventing them. A reference to a shared deadline, responsibility, or concern can explain why an appeal matters to these readers. Then connect the choice to the intended response: the writer emphasizes X because this audience values Y, supporting the request for Z.",
            "Avoid stopping at a device label such as statistics or emotional appeal. Explain what the selected detail does in this situation. An effect is a supported interpretation, not proof that every reader was persuaded.",
        ),
        example="At a budget hearing, a librarian tells council members: 'Students whose shifts end at six reach locked doors at our branch. Keeping it open until eight on two evenings would let them use the computers they need for applications.'",
        walkthrough="The speaker requests an actionable schedule change from officials who can fund it. The working students' schedules establish a mismatch between current hours and access. The limited two-evening proposal makes the request concrete; it does not establish the proposal's cost or prove approval is inevitable.",
        prompt="A principal writes to families: 'Before next month's bus-route vote, please tell us which stops your children can reach safely.' What is the most supported account of the purpose?",
        options=("To announce that the routes have already been approved", "To gather families' practical knowledge before a decision", "To prove that every existing stop is dangerous"),
        feedback=("The vote is still ahead. Asking for information signals consultation, not a completed decision.", "Yes. The upcoming vote supplies the occasion, and families' knowledge of access is the requested contribution.", "Concern about safety does not establish that every stop is unsafe. Keep the inference within the text's evidence."),
        correct=1,
    ),
    Lesson(
        slug="separate-claim-and-evidence", title="Separate the claim from its support", skill="3.A",
        objective="Identify what a writer argues and evaluate what the evidence actually supports.",
        explanation=(
            "A claim asks readers to accept a position. Evidence provides grounds for accepting it: observations, records, examples, testimony, or data. A reason links support to the position. These roles depend on the argument; a statement can support a larger claim while needing evidence of its own.",
            "Test relevance and scope separately. Relevant evidence addresses the actual claim. Sufficient evidence supports the breadth of that claim. A successful trial at one school can justify further testing, but it cannot alone establish that the policy will work at every school.",
            "For a causal claim, ask what other explanations remain. A change that follows a policy may be consistent with an effect, but a comparison, baseline, and information about other changes make the causal inference stronger.",
        ),
        example="A student editorial argues: 'The district should pilot a later start. At one nearby school, reported tardiness fell during a later-start trial, although its bus routes also changed that semester.'",
        walkthrough="The policy claim is the recommendation to pilot a later start. The nearby school's record is supporting evidence. The simultaneous route change limits a claim that start time alone caused the decline. The modest pilot recommendation fits the uncertainty better than a promise that all schools will get identical results.",
        prompt="A writer claims that a new tutoring program caused higher scores. Which added evidence would best help evaluate that causal claim?",
        options=("A description of the tutoring room's decoration", "A testimonial that repeats the claim in stronger language", "Before-and-after scores for comparable participants and nonparticipants, with information about other instructional changes"),
        feedback=("The room's appearance does not directly test whether the program explains the score change.", "Repeating a conclusion does not independently support it or address alternative explanations.", "Yes. A comparison and information about other changes help evaluate the explanation, although they do not automatically remove every source of bias."),
        correct=2,
    ),
    Lesson(
        slug="develop-relevant-evidence", title="Make evidence earn its place", skill="4.A",
        objective="Choose specific evidence and explain how it develops an appropriately limited claim.",
        explanation=(
            "Before adding evidence, state the exact claim the paragraph must support. Choose details for their relevance, credibility, and precision rather than for how impressive they sound. A vivid anecdote may illustrate an experience without showing how common it is.",
            "Introduce enough context to make evidence interpretable. Who or what was studied? When? Compared with what? Preserve limitations rather than stretching a source into a stronger claim than it supports. If evidence complicates your position, refine the claim.",
            "Follow the detail with commentary explaining the link. A useful draft pattern is claim, specific evidence, and an explanation of why that evidence matters. This is a reasoning check, not a requirement that every paragraph follow an identical formula.",
        ),
        example="Draft claim: 'A shaded waiting area could make the afternoon bus stop more usable in hot weather.' Evidence: 'During three clear afternoons, a student group recorded lower surface temperatures under the stop's existing canopy than on adjacent exposed pavement.'",
        walkthrough="The observation is relevant to local heat conditions. It supports investigating additional shade, but surface temperature is not a direct measure of passenger comfort or air temperature. Strong commentary explains the connection and proposes checking comfort and accessibility before asserting the design solves every problem.",
        prompt="A paragraph recommends a small trial of weekend library hours. Which evidence best develops that recommendation?",
        options=("A local survey describing unmet weekend access needs, paired with estimated staffing costs for a trial", "A national statistic about the total number of books printed", "An assertion that libraries have always been valuable"),
        feedback=("Yes. Local demand and trial costs directly address why the proposal may be useful and feasible. Survey representativeness still matters.", "Book production does not directly establish local demand for weekend access or the feasibility of a trial.", "General value does not explain why this specific change is warranted. Add evidence tied to the proposal."),
        correct=0,
    ),
)

AUDIENCE_AND_THESIS = (
    Lesson(
        slug="infer-audience-values", title="Infer audience values from the text", skill="1.B",
        objective="Use textual clues to explain what a writer assumes the audience knows or values.",
        explanation=(
            "An audience is more specific than everyone who might read a text. Start with the occasion and distribution: a letter to donors, a testimony before a board, and a neighborhood notice invite different responses. Then examine what the writer explains, leaves unstated, or treats as a shared priority.",
            "A writer may appeal to values the audience already holds or try to reshape those values. Repeated references to cost might reflect anticipated budget concerns; they do not prove that readers care only about money. Separate the writer's apparent assumptions from facts about every member of the audience.",
            "Support your inference with a particular choice. Explain why that choice fits these readers and this purpose. If several audiences are present, identify the one most directly addressed rather than forcing a single description onto everyone.",
        ),
        example="In a letter to museum members, a director writes: 'You have kept our doors open through difficult years. A monthly contribution now will let us keep admission free for school groups.'",
        walkthrough="The reference to past support positions members as continuing partners. Connecting a monthly contribution with free school visits appeals to an interest in public access, while making a specific request. It does not show that every member has children or agrees with every museum policy.",
        prompt="A housing proposal addressed to a neighborhood association emphasizes that the design preserves the existing courtyard and walking paths. Which inference is best supported?",
        options=("The writer assumes every resident opposes additional housing", "The writer anticipates concern about shared spaces and familiar routes", "The writer believes residents have already approved the design"),
        feedback=("Preservation may address a concern without implying opposition from every resident.", "Yes. The details respond to possible concern about continuity and access in the neighborhood.", "A proposal's reassurance does not establish prior approval. That would require additional evidence."),
        correct=1,
    ),
    Lesson(
        slug="adapt-without-distorting", title="Adapt to readers without distorting the argument", skill="2.B",
        objective="Revise emphasis and explanation for an audience while preserving the claim's accuracy.",
        explanation=(
            "Audience awareness affects which information comes first, how much background readers need, and what objections deserve attention. Before revising, name the action or understanding you want from these particular readers. A change in tone alone cannot repair missing information.",
            "Readers with different responsibilities may need different evidence. Volunteers considering a project need schedules and tasks; officials approving it may need costs, safeguards, and accountability. Neither audience should receive a promise the evidence cannot support.",
            "Respectful acknowledgment can make disagreement productive. State a real concern accurately, then show how your proposal addresses it or where a tradeoff remains. Avoid flattery, stereotypes, and jargon that obscures the decision readers must make.",
        ),
        example="A student asks a facilities manager to approve a courtyard garden. Instead of 'Everyone loves gardens,' the revised request explains who will water it during breaks, where tools will be stored, and how paths will remain accessible.",
        walkthrough="The revision answers practical concerns connected to the manager's responsibilities. It does not abandon the garden proposal; it supplies information the decision requires. Benefits for students can still matter, but enthusiasm alone does not resolve maintenance and access questions.",
        prompt="A writer seeks approval from a school board for a student-run repair workshop. Which revision best addresses that audience's decision?",
        options=("Add a supervision plan, a proposed budget, and a clear description of permitted repairs", "Replace the budget section with a longer celebration of student creativity", "Describe the workshop as risk-free so the board feels reassured"),
        feedback=("Yes. These additions address feasibility and oversight while retaining the proposal's purpose.", "Creativity may be a benefit, but removing the budget withholds information needed for approval.", "An unsupported guarantee conceals uncertainty. Explain safeguards and limitations rather than claiming there is no risk."),
        correct=0,
    ),
    Lesson(
        slug="trace-supporting-claims", title="Trace the claims inside an argument", skill="3.A",
        objective="Distinguish a central claim, supporting reasons, and evidence in a short argument.",
        explanation=(
            "Arguments often contain several claims at different levels. The central claim gives the position the whole text develops. Supporting claims supply reasons for accepting it. Evidence grounds those reasons in something more specific than repetition or assertion.",
            "Ask what each sentence is doing relative to the others. A fact is not automatically evidence for every nearby claim. Test the connection by completing the thought: this detail supports this reason because of this relationship. If you cannot explain the link, the writer may need commentary or better evidence.",
            "An opposing claim can appear inside an argument without becoming the writer's position. Watch for attribution and responses: some critics contend, however, and although can signal different voices. Map the reasoning before deciding which position the writer endorses.",
        ),
        example="An editorial argues that the town should publish meeting recordings. It says recordings help residents whose shifts prevent attendance, then cites interviews with evening workers. It acknowledges that summaries are faster to read but argues that recordings preserve exchanges summaries omit.",
        walkthrough="Publishing recordings is the central recommendation. Access for workers is one supporting reason; the interviews support that reason. The point about convenient summaries is a concession, followed by a separate reason about preserving discussion. Merely counting these sentences would miss their different roles.",
        prompt="An essay states, 'Some opponents call the schedule inflexible. Yet the proposal lets teams select any two afternoons, so it preserves meaningful choice.' What role does the second sentence play?",
        options=("It accepts the opponents' characterization as the essay's conclusion", "It introduces an unrelated benefit of afternoon activities", "It responds to the objection by identifying a flexible feature"),
        feedback=("The word yet and the explanation of choice challenge that characterization.", "Choice among afternoons directly addresses the objection about inflexibility.", "Yes. The writer uses a specific provision to answer the preceding criticism."),
        correct=2,
    ),
    Lesson(
        slug="qualify-evidence-use", title="Use evidence at the scale it supports", skill="4.A",
        objective="Select and frame evidence without turning a limited observation into a universal conclusion.",
        explanation=(
            "Evidence has a scope: a population, time period, setting, and method. Identify those boundaries before using it. A survey of volunteers describes those respondents; it may not represent students who never heard about the survey or chose not to answer.",
            "Relevant evidence can still be limited. Do not discard every imperfect source, but match the claim to what it can establish and combine it with other suitable evidence. An interview can illuminate a mechanism or experience; a broader sample may help estimate prevalence.",
            "When revising, preserve information readers need to evaluate the inference. Words such as all, always, proves, and causes often make a claim broader than the source permits. Replace them when warranted with an accurate description of what was observed, then explain what further evidence would be useful.",
        ),
        example="Twenty students who already attend a writing center say appointments helped them plan essays. A draft concludes, 'Appointments improve every student's writing.' A revision says the responses suggest planning benefits for participating students and recommends a trial that also invites students who have not used the center.",
        walkthrough="The revision retains useful testimony while acknowledging selection and scope. The responses do not directly measure essay quality or represent every student. A broader trial and evaluation of writing would address different questions from the satisfaction survey.",
        prompt="A neighborhood poll of 40 self-selected respondents favors a proposed market. Which use of the poll is most responsible?",
        options=("Describe it as evidence of interest among respondents, then seek broader input before claiming neighborhood-wide support", "Present the result as proof that most residents favor the market because 40 is a precise count", "Omit how participants were selected so readers focus on the market's benefits"),
        feedback=("Yes. This uses the evidence while keeping its representativeness limits visible.", "A precise sample size does not make a self-selected sample representative of all residents.", "Selection is relevant to the inference. Omitting it can make the evidence seem stronger than it is."),
        correct=0,
    ),
    Lesson(
        slug="recognize-a-thesis", title="Recognize the thesis that organizes a text", skill="3.B",
        objective="Identify a defensible central position and connect it to the argument's supporting claims.",
        explanation=(
            "A thesis expresses a position that evidence and reasoning can develop. A subject announcement tells readers what will be discussed but may not establish a position. 'This essay considers public art' names a topic; 'Public art funding should reserve space for temporary neighborhood projects' makes a claim readers can examine.",
            "A thesis may appear after context or emerge across more than one sentence. Do not assume the first or last sentence is automatically the thesis. Look for the position that explains why the writer includes and connects the supporting claims.",
            "The thesis need not list exactly three reasons. What matters is a coherent relationship between the central claim and the reasoning that follows. If a paragraph supports an unrelated position, the writer may need to revise the thesis, the paragraph, or the explanation linking them.",
        ),
        example="After describing empty storefronts, a writer argues that the town should offer short-term leases to local groups. Later paragraphs explain how a trial could test demand and limit long-term commitments, then acknowledge the need for safety inspections.",
        walkthrough="The recommendation about short-term leases organizes the text. Testing demand and limiting commitments explain its appeal; inspections qualify how it should operate. The initial description establishes context, but a description of empty buildings alone does not make the policy argument.",
        prompt="Which sentence offers a central claim that could organize an argument about school announcements?",
        options=("School announcements appear in several formats", "Schools should provide written summaries of spoken announcements so absent students can access essential information", "This essay will discuss whether announcements are useful"),
        feedback=("This observation supplies context but does not establish a position about what should happen or why.", "Yes. The recommendation and access rationale can guide supporting evidence and discussion of implementation.", "This announces a discussion without taking a position that the discussion will defend."),
        correct=1,
    ),
    Lesson(
        slug="write-a-defensible-thesis", title="Write a thesis you can actually defend", skill="4.B",
        objective="Revise a broad assertion into a clear position with a manageable scope and line of reasoning.",
        explanation=(
            "Begin by answering the question the prompt actually asks. A thesis about whether a policy should be adopted differs from a thesis analyzing how a writer persuades an audience. Both need a defensible position, but the evidence and reasoning they require are different.",
            "Make the claim specific enough to guide your paragraphs, without adding a list of reasons you cannot support. A useful qualification identifies a meaningful condition, limit, or tradeoff. Adding sometimes to an otherwise vague statement does not by itself create a thoughtful argument.",
            "Test the draft thesis against your evidence. Could a reasonable reader disagree? Can you explain the connection between your support and your position? Revise overstatements rather than inventing proof. In rhetorical analysis, connect the writer's choices to purpose instead of merely listing devices.",
        ),
        example="Prompt: Should a town replace all printed public notices with online notices? Draft: 'Technology is the future.' Revision: 'The town should expand searchable online notices while retaining printed postings at key public sites, because digital convenience does not eliminate residents' unequal access to reliable internet.'",
        walkthrough="The revision answers the replacement question with a specific position and a rationale that can be supported. It allows a discussion of costs and access. The draft is a slogan about technology that does not resolve whether all printed notices should disappear.",
        prompt="A prompt asks whether schools should require every student to join a competitive team. Which thesis responds with the clearest defensible position?",
        options=("Competition has existed for a long time and affects many people", "There are arguments on both sides, so the issue is complicated", "Schools should offer competitive teams without requiring universal participation, since collaborative noncompetitive activities can also develop commitment"),
        feedback=("Historical context does not answer the question about a universal requirement.", "Acknowledging disagreement is a starting point, but this does not take a position.", "Yes. The thesis addresses the requirement and supplies a rationale that evidence and counterargument can develop."),
        correct=2,
    ),
)

REASONING_AND_DEVELOPMENT = (
    Lesson(
        slug="identify-the-assumption", title="Find the assumption between evidence and claim", skill="3.A",
        objective="Explain the unstated connection a writer needs for evidence to support a claim.",
        explanation=(
            "Evidence does not interpret itself. A writer moves from an observation to a conclusion by relying on a connection, sometimes called a warrant. Naming that connection helps you explain the argument instead of merely repeating its details.",
            "Try writing the argument as evidence, assumed relationship, and claim. Then ask whether the relationship is plausible and what could limit it. An assumption is not automatically a flaw: ordinary reasoning depends on assumptions. The useful question is whether this assumption is justified in this situation.",
            "Keep the scale of the conclusion in view. Evidence that one feature matters to some users may support testing a change without proving it should be adopted everywhere. A narrower claim can remain persuasive even when a sweeping version would fail.",
        ),
        example="A campus editorial says, 'Several students leave evening study sessions early to catch the last bus. Extending the bus schedule would allow those students to stay longer.'",
        walkthrough="The observation connects early departure with the last bus. The conclusion assumes transportation is a constraint on these students' attendance and that a later bus would be usable. The editorial would need more evidence to claim that all students would study longer or that the change would necessarily improve grades.",
        prompt="A proposal argues that posting recordings of public meetings will improve access for residents who work during meeting hours. Which assumption most directly connects the proposal to its reason?",
        options=("Most residents disagree with decisions made at public meetings", "At least some affected residents can access recordings at a more convenient time", "Recorded meetings will be shorter than live meetings"),
        feedback=("Disagreement is not necessary for the access argument. The relevant issue is when and how residents can follow proceedings.", "Yes. The argument depends on recordings being usable outside the conflicting work hours.", "The proposal can improve scheduling access even if a recording lasts as long as the original meeting."),
        correct=1,
    ),
    Lesson(
        slug="choose-complementary-evidence", title="Choose evidence that adds a new kind of support", skill="4.A",
        objective="Combine complementary evidence instead of accumulating details that repeat the same point.",
        explanation=(
            "More evidence is not always stronger evidence. Several anecdotes can repeat an experience without establishing how widespread it is. Choose the next source by identifying the question your existing support leaves unanswered.",
            "Different forms of evidence do different work. A personal account can reveal a mechanism or consequence. A representative survey can estimate how common a view is. A budget can address feasibility. Match the evidence to the claim rather than treating every statistic as inherently stronger than every example.",
            "Preserve disagreements and limits between sources. If interviewees report a benefit while cost records show an obstacle, develop a qualified proposal that addresses both. Synthesis means explaining relationships among evidence, not lining up quotations as if they all make the same point.",
        ),
        example="An argument for translated emergency notices includes a resident's account of misunderstanding an evacuation message. The writer adds a local language-access survey and estimates from qualified translation services.",
        walkthrough="The account illustrates consequences, the survey helps establish the scope of local need, and estimates address implementation. Each source supports a different part of the proposal. Neither one resident's experience nor the survey alone establishes the cost or reliability of a translation plan.",
        prompt="A writer has three interviews describing difficulty reaching a clinic by bus. The next paragraph claims a proposed shuttle is financially feasible. Which addition best supports that new claim?",
        options=("A fourth interview describing the same travel difficulty", "A photograph showing a long line at the clinic entrance", "A documented operating-cost estimate compared with identified funding"),
        feedback=("Another account may reinforce the access concern but does not establish the shuttle's affordability.", "The photograph may raise questions about demand, but it does not supply cost or funding information.", "Yes. Cost and funding evidence directly addresses financial feasibility; the writer should still identify assumptions in the estimate."),
        correct=2,
    ),
    Lesson(
        slug="test-the-line-of-reasoning", title="Test each step in the line of reasoning", skill="5.A",
        objective="Evaluate whether an argument's sequence of claims supports its conclusion.",
        explanation=(
            "A line of reasoning is the path from supporting claims to a conclusion. Outline what each paragraph contributes using verbs such as establishes, explains, compares, qualifies, and responds. This reveals relationships that a list of topics can miss.",
            "Check each transition in the logic. Does a local observation become a universal claim? Does sequence in time become proof of cause? Does the writer change the meaning of a key term? Identify the exact step and the missing support instead of simply calling the whole argument weak.",
            "A counterexample may require qualification rather than total rejection. Distinguish evidence against a reason from evidence against the conclusion itself. A sound conclusion can have a poorly supported justification, and a plausible reason may still be insufficient for a broad conclusion.",
        ),
        example="A writer notes that registrations rose after a recreation center extended its hours, then concludes that longer hours caused the entire increase. The center also reduced fees and launched an advertising campaign during the same period.",
        walkthrough="The chronology is relevant, but the causal conclusion exceeds it. Fees and advertising offer alternative explanations. The writer could revise to say the increase coincided with the changes and seek comparisons that help isolate the role of hours.",
        prompt="A proposal argues that one successful outdoor class proves every course should meet outdoors all year. Where does its reasoning most clearly need support?",
        options=("The move from one class in one setting to all courses and seasons", "The use of a specific example instead of an abstract opening", "The decision to discuss a school policy rather than a personal preference"),
        feedback=("Yes. The conclusion extends beyond the conditions the example establishes; different subjects and weather may matter.", "Specific examples can be useful. The issue is the breadth of the inference drawn from this one.", "Policy arguments are legitimate. The gap lies between the evidence's scope and the proposed universal rule."),
        correct=0,
    ),
    Lesson(
        slug="write-commentary-that-connects", title="Write commentary that makes the connection", skill="6.A",
        objective="Explain why evidence supports a claim rather than paraphrasing it or announcing its importance.",
        explanation=(
            "Commentary supplies the reasoning between a detail and your claim. Ask what the evidence shows, why that matters for this argument, and how far the inference extends. A sentence saying 'This proves my point' performs none of those jobs unless it explains the connection.",
            "In rhetorical analysis, connect a writer's choice to the audience and purpose. Do not treat naming a device as an explanation of its effect. In an argument, explain how an example or observation supports a reason and how that reason advances your position.",
            "Avoid claiming certainty about every reader's reaction. Use the text and situation to support a plausible effect. Strong commentary can also identify a limit: a detail may establish urgency without showing that the proposed solution is affordable.",
        ),
        example="A speaker urging repair of a footbridge tells officials that residents must now take a two-mile detour to reach a grocery store. Weak commentary says, 'This shows the bridge is important.' Stronger commentary explains that the detour turns structural damage into a daily access problem, giving officials a concrete public-service reason to prioritize repairs.",
        walkthrough="The stronger version explains the relationship between the detail and the request. It does not merely rename the topic. The detour helps establish the repair's significance, although it does not determine engineering costs or prove repairs should outrank every other project.",
        prompt="A writer advocating extended clinic hours cites workers who cannot attend during their shifts. Which commentary best connects that evidence to the proposal?",
        options=("The workers say they cannot attend during their shifts, which is what the evidence states", "Offering appointments outside those shifts would address a scheduling barrier identified in the workers' accounts", "The evidence is very powerful and proves the writer is completely correct"),
        feedback=("This repeats the evidence without explaining why the proposed change responds to it.", "Yes. The commentary identifies the barrier and explains how the proposal could address it without promising to solve every access problem.", "Praise and certainty do not supply reasoning. Explain the specific relationship between the accounts and the proposal."),
        correct=1,
    ),
    Lesson(
        slug="recognize-development-methods", title="Explain why a writer develops an idea this way", skill="5.C",
        objective="Identify a method of development and explain its function in the argument.",
        explanation=(
            "Writers develop ideas through methods such as narration, description, comparison, definition, and cause-and-effect explanation. A passage may combine several. Identify the method by what the sentences do, then connect it to the claim the writer is developing.",
            "A comparison can clarify a distinction, expose an inconsistency, or support an evaluation. A narrative can establish a problem through an experience. Neither method guarantees sound reasoning: check whether the compared cases are relevant or whether the story is being asked to represent more than it can.",
            "Avoid confusing organization with purpose. Chronological order tells you how a passage proceeds, but you still need to explain why that sequence helps the writer. A procedural account may show where a delay occurs; a before-and-after account may emphasize a change.",
        ),
        example="An article places two application processes side by side: one requires several office visits, while the other allows documents to be submitted in a single appointment. It compares the same steps in each process before recommending a trial of the second.",
        walkthrough="The comparison isolates procedural differences relevant to the recommendation. It helps readers see where repeated visits might be reduced. The writer would need separate evidence to establish effects on accuracy, staffing costs, or every applicant's experience.",
        prompt="A paragraph recounts each step a resident takes to report a broken streetlight, emphasizing that the same information must be submitted to three offices. What is the most supported account of the method's function?",
        options=("It defines the technical meaning of electrical failure", "It compares streetlights with other kinds of public infrastructure", "It traces a process to reveal duplication that motivates procedural reform"),
        feedback=("The sequence concerns reporting, not an explanation of an electrical concept.", "No second type of infrastructure is developed as a basis for comparison.", "Yes. Following the resident's steps makes the repeated submissions visible and supports considering a simpler process."),
        correct=2,
    ),
    Lesson(
        slug="develop-an-argument-purposefully", title="Choose a development method that serves your claim", skill="6.C",
        objective="Plan an argument's development around the reasoning readers need to follow.",
        explanation=(
            "Choose a method after identifying the job a paragraph must do. To clarify a misunderstood term, define it with relevant boundaries. To evaluate alternatives, compare them using consistent criteria. To explain a proposed remedy, show how it addresses the problem's causes or mechanisms.",
            "A method is a tool rather than a mandatory template. You can begin with an illustrative narrative and then compare alternatives, provided you explain the relationship. Do not let a vivid opening consume space needed for evidence or leave the central recommendation unstated.",
            "Check the completed plan for fairness and relevance. Compare options on the same criteria, acknowledge differences that limit the comparison, and explain tradeoffs. Develop the position the prompt asks for instead of substituting an easier description of the general topic.",
        ),
        example="A writer choosing between two school lunch systems organizes the argument around waiting time, dietary access, and cost. Under each criterion, the writer considers both systems, then recommends a limited trial with measures for judging the results.",
        walkthrough="Using shared criteria makes the comparison usable for a decision. Describing only the benefits of one system and only the costs of the other would create an uneven comparison. The trial recommendation can address uncertainty if the writer explains what it will test.",
        prompt="You are arguing that a confusing permit process should be simplified. Which plan most directly develops that argument?",
        options=("Trace where applicants repeat steps, explain the proposed changes, and evaluate how those changes preserve necessary review", "List every type of permit issued by the town without connecting the list to the process", "Describe a successful applicant's celebration and assume readers will infer the needed changes"),
        feedback=("Yes. This plan links the identified problem to a remedy while addressing a likely concern about maintaining oversight.", "A catalog may supply background but does not explain what is confusing or how simplification would work.", "A story can engage readers, but it cannot replace the explanation of the proposed reform and its consequences."),
        correct=0,
    ),
)


def lessons_for(code: str, unit_order: int) -> tuple[Lesson, ...]:
    if code != "english-language":
        return ()
    return {1: FOUNDATIONS, 2: AUDIENCE_AND_THESIS, 3: REASONING_AND_DEVELOPMENT}.get(unit_order, ())
