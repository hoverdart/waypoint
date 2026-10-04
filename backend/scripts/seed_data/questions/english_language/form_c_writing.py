"""Independent revision passages for Form C; invented drafts and pilot data."""
from .builders import passage_questions

TOOLS_PASSAGE = """(1) Last month I borrowed a tile cutter for a job that took forty minutes. (2) Buying it would have cost more than the tiles, and afterward it would have occupied most of my cupboard. (3) A neighbor lent me hers, but not everyone knows a neighbor with the right tool. (4) Our town should create a tool-lending pilot in an unused room at the community center.

(5) A lending program could begin with equipment that people need occasionally: a drill, a sewing machine, a carpet cleaner. (6) Residents would reserve an item, receive instructions, and return it after a short loan. (7) At a planning workshop, eighteen attendees named tools they would like to borrow. (8) This proves that everyone in town would use the service. (9) The workshop also produced three offers to help repair equipment, although no volunteer has yet agreed to a regular schedule.

(10) Sharing does not eliminate the costs of ownership; it moves some of them to the program. (11) Blades wear out, parts go missing, and borrowers may need help using unfamiliar equipment safely. (12) Each item would therefore need a maintenance record and a check before its next loan. (13) We should announce the opening date immediately and settle these details once borrowing begins. (14) The center already has tables painted a cheerful yellow.

(15) Some residents worry that a required deposit would exclude people who could most benefit from borrowing. (16) Others worry that lending without a deposit would leave the center unable to replace damaged equipment. (17) The committee should compare a small deposit with a sponsored-deposit option and publish the expected replacement costs before choosing a policy. (18) Any policy must explain who makes damage decisions and how a borrower can challenge a charge.

(19) The pilot could run for six months with a limited inventory. (20) Its report should track completed loans, repair costs, unmet requests, and whether residents say that deposits kept them from borrowing. (21) A successful program would put seldom-used equipment to work without pretending that the work of lending takes care of itself."""

TOOLS = passage_questions(passage_id='lang-c-tools', title='A Cupboard We Can Share', mode='writing',
    context='An original fictional draft for a town newsletter argues for a tool-lending pilot. The writer is revising for residents and the committee that manages the community center; all workshop details are invented.', passage=TOOLS_PASSAGE, items=[
    (2, '2.B', 3, 'The writer wants to address committee members who are responsible for the center’s operating budget. Which addition after sentence 4 would best serve that purpose?', 1, [
        ('Almost everyone enjoys discovering that a neighbor owns something useful.', 'This generalization does not address the committee’s financial responsibility.'),
        ('Before committing funds, the committee should estimate staffing, insurance, storage, and maintenance costs for a small trial.', 'This identifies concrete budget considerations and frames the proposal as a limited, costed pilot.'),
        ('A lending program deserves support because only an unneighborly person would oppose it.', 'The accusation dismisses legitimate budget concerns and alienates the intended decision makers.'),
        ('The history of cupboard design reveals many changing preferences in household furniture.', 'This subject does not help committee members evaluate the proposed program.'),
    ]),
    (7, '2.A', 2, 'Which opening sentence could be added before sentence 1 to introduce the problem developed in the first paragraph?', 3, [
        ('The community center was repainted several years ago.', 'The date of repainting does not introduce the mismatch between occasional need and ownership costs.'),
        ('No one should ever buy equipment for personal use.', 'This absolute claim exceeds the proposal, which concerns tools needed only occasionally.'),
        ('The town’s newest shop has a large display window.', 'The shop detail does not establish a relevant problem for the borrowing anecdote.'),
        ('Some household jobs require a tool for less time than it takes to decide where to store it.', 'This introduces occasional need and storage burdens that the tile-cutter example makes concrete.'),
    ]),
    (1, '4.A', 4, 'The writer wants additional evidence relevant to whether residents could actually use the proposed service. Which finding would be most useful to investigate and accurately report?', 0, [
        ('Responses from residents with varied work schedules about which pickup hours they could use and which tools they would borrow.', 'This evidence addresses practical access and demand beyond the self-selected workshop attendees.'),
        ('The average number of pages in instruction manuals sold with new drills.', 'Manual length does not establish local demand or access to pickup hours.'),
        ('The national retail price of the most expensive carpet cleaner ever advertised.', 'An extreme price gives little information about the proposed local inventory or its potential borrowers.'),
        ('The committee chair’s preference for the color of the storage cabinets.', 'Aesthetic preference does not support a claim about residents’ ability to use the program.'),
    ]),
    (2, '4.B', 3, 'Which revision of sentence 4 would best state a defensible thesis that anticipates the full draft?', 2, [
        ('Borrowing and buying are two different ways of obtaining equipment.', 'This factual distinction supplies no arguable position or direction for the proposal.'),
        ('A free tool service will solve every resident’s household repair problems.', 'The universal guarantee exceeds the evidence and ignores operating and access constraints.'),
        ('Our town should test a small tool-lending program with explicit maintenance, access, and evaluation policies.', 'This advances a specific proposal and previews the responsibilities developed in the later paragraphs.'),
        ('The community center is the only building in town with spare storage space.', 'The draft does not establish this claim, and storage alone does not express its broader argument.'),
    ]),
    (9, '4.C', 2, 'Which revision of sentence 8 best brings its claim into line with the evidence in sentence 7?', 1, [
        ('The workshop proves that all residents prefer borrowing to buying.', 'Eighteen attendees cannot establish a universal preference among residents.'),
        ('These suggestions show interest among the attendees, although they do not establish town-wide demand.', 'The revision preserves the observed interest while acknowledging the limited, self-selected group.'),
        ('The workshop provides no information of any kind about possible borrowers.', 'This dismisses the genuine but limited evidence of the attendees’ interest.'),
        ('Exactly eighteen loans will be made during the pilot’s first month.', 'Suggestions at a workshop do not establish a future number of completed loans.'),
    ]),
    (3, '6.A', 4, 'Which sentence added after sentence 9 would best explain the significance of the distinction between offers and scheduled commitments?', 3, [
        ('The workshop lasted ninety minutes and ended before sunset.', 'The workshop’s duration does not connect volunteer offers to the program’s ability to operate.'),
        ('Some tools are heavier than other tools and may require stronger shelves.', 'Storage loads do not explain why informal offers cannot yet support a staffing plan.'),
        ('The three volunteers should be praised as the town’s most experienced repair workers.', 'Their relative expertise has not been established and does not resolve scheduling.'),
        ('The budget cannot yet assume that volunteers will cover repairs, because an offer does not establish when help will be available.', 'This connects the evidence to a planning consequence and avoids treating enthusiasm as guaranteed capacity.'),
    ]),
    (5, '6.B', 3, 'Which transition at the beginning of sentence 15 best connects the fourth paragraph to the preceding discussion of program costs?', 0, [
        ('Deciding how to cover those costs raises a question of access.', 'This connects operating costs with the deposit policy’s potential effect on who can borrow.'),
        ('In contrast, maintenance is never a financial concern.', 'This contradicts the preceding paragraph’s account of wear, missing parts, and checks.'),
        ('For example, every resident already owns the same equipment.', 'This unsupported assertion does not connect maintenance costs to deposits.'),
        ('Meanwhile, the history of yellow paint deserves attention.', 'This follows an irrelevant detail instead of the argument’s financial and access concerns.'),
    ]),
    (6, '8.A', 4, 'The writer wants to replace sentence 13 with a sentence that sustains the practical, measured tone of the proposal. Which choice best does so?', 2, [
        ('If the committee hesitates, it will show that it does not care about residents.', 'This attacks motives rather than addressing the operational requirements just identified.'),
        ('We can probably sort everything out somehow after the doors open.', 'The vague reassurance minimizes the concrete maintenance and safety concerns.'),
        ('The opening date should follow an approved maintenance plan and clear borrower instructions.', 'The revision treats the preceding risks as planning requirements and maintains a specific, practical tone.'),
        ('The glorious dawn of universal access to equipment is finally upon us.', 'The inflated language overstates the pilot’s scope and departs from the draft’s practical register.'),
    ]),
    (7, '8.B', 2, 'Which revision of sentence 17 most clearly preserves its meaning?', 1, [
        ('Comparing a small deposit with a sponsored-deposit option, expected replacement costs should be published by the committee.', 'The opening modifier grammatically describes the costs rather than the committee doing the comparison.'),
        ('Before choosing a policy, the committee should compare a small deposit with a sponsored-deposit option and publish expected replacement costs.', 'The revision clearly identifies the actor and retains both preparatory actions and their timing.'),
        ('The committee should choose a policy before it compares deposits or publishes replacement costs.', 'This reverses the original sequence and defeats the purpose of informed comparison.'),
        ('They should compare it with the other one and publish those before choosing it.', 'The repeated pronouns obscure the policies, costs, and responsible actor.'),
    ]),
    (7, '8.C', 3, 'Which revision of sentence 10 correctly joins its two independent clauses while preserving their relationship?', 3, [
        ('Sharing does not eliminate the costs of ownership, it moves some of them to the program.', 'A comma alone cannot join these independent clauses in standard written English.'),
        ('Sharing does not eliminate the costs of ownership it moves some of them to the program.', 'Without punctuation or a conjunction, the independent clauses form a fused sentence.'),
        ('Sharing does not eliminate the costs of ownership, because it moves some of them to the program?', 'The question mark incorrectly turns a declarative explanation into a question, and the revision changes the construction unnecessarily.'),
        ('Sharing does not eliminate the costs of ownership; instead, it moves some of them to the program.', 'The semicolon correctly separates the independent clauses, and “instead” clarifies the contrast.'),
    ]),
])

HEAT_PASSAGE = """(1) On a hot afternoon, two streets a block apart can feel like different cities. (2) One offers shade from mature trees; the other reflects sunlight from a broad paved lot. (3) A student group in our neighborhood proposes a project to map these differences and recommend places for new shade.

(4) During a trial on one afternoon, volunteers took readings at six sites with handheld thermometers. (5) The shaded sites had lower readings than the unshaded sites. (6) One volunteer visited the shaded sites first, while another measured the paved lot an hour later. (7) These results prove that planting trees will lower every neighborhood temperature by the same amount. (8) The group plans to collect more observations before submitting its final report.

(9) To make comparisons more useful, teams should follow the same measurement procedure. (10) They should record the time, cloud cover, sensor position, and surrounding surface at each site. (11) Readings near a sunlit wall may not be comparable with readings taken in open shade. (12) The group should also record which routes volunteers could not safely reach, rather than leaving those routes as unexplained blank spaces on the map. (13) Several volunteers designed an attractive logo for their notebooks.

(14) Measurements alone will not tell the group which places most need attention. (15) A lightly used parking area may be hotter than a bus stop where people wait each afternoon. (16) Residents can identify where they spend time outside, whether they can reach existing shade, and which paths become difficult in hot weather. (17) Such reports should be compared with the temperature observations rather than treated as a substitute for them.

(18) The final map should distinguish measured conditions from proposals for change. (19) A shaded symbol could show where shade was observed, while a separate symbol could identify a location proposed for a tree or shelter. (20) A recommendation should also consider maintenance, space, and whether underground utilities limit planting. (21) The project will be useful if it produces a spectacularly perfect map. (22) The group should publish its procedure and invite residents to identify both missing locations and errors."""

HEAT = passage_questions(passage_id='lang-c-heat', title='Mapping the Heat We Meet', mode='writing',
    context='An original fictional draft for a neighborhood association explains a student mapping proposal. The trial and observations are invented; no real research results are being reported.', passage=HEAT_PASSAGE, items=[
    (8, '2.B', 2, 'The writer wants to invite residents without technical training to contribute. Which addition after sentence 16 best serves that purpose?', 2, [
        ('Only reports written with specialized meteorological terminology will be considered.', 'This creates an unnecessary barrier for the intended contributors.'),
        ('The group assumes that anyone who has not used a thermometer has no useful observations.', 'This dismisses the lived experience that paragraph 4 seeks to include.'),
        ('Residents could mark a familiar route on a simple paper map and describe when and where shade is hard to find.', 'This offers a concrete, accessible way to contribute relevant information without technical equipment.'),
        ('The association should begin by requiring everyone to calculate a regional climate average.', 'This technical demand does not help residents report local access to shade.'),
    ]),
    (2, '2.B', 4, 'Which addition after sentence 20 would best address an audience concerned that recommendations might create new responsibilities for residents?', 0, [
        ('Each proposal should identify who would maintain the added shade and how residents could comment before a location is chosen.', 'This addresses continuing responsibilities and gives affected residents a role in reviewing the proposal.'),
        ('Every proposed location should receive the same symbol size on the printed map.', 'Symbol size does not address maintenance burdens or participation in decisions.'),
        ('Residents who ask about upkeep should wait until construction is complete.', 'This postpones a legitimate concern until after decisions can readily be changed.'),
        ('The project’s logo could be printed on shirts in three colors.', 'Merchandise design does not answer concerns about responsibilities created by recommendations.'),
    ]),
    (4, '2.A', 3, 'Which revision of sentence 21 would best begin a conclusion that reflects the draft’s purpose?', 3, [
        ('Mapping has a long history that began before handheld thermometers were invented.', 'This introduces a new historical topic rather than concluding the local proposal.'),
        ('Because every map contains limitations, the group should abandon its project.', 'This contradicts the draft’s emphasis on improving and clearly reporting limited evidence.'),
        ('The project will be successful only if every resident agrees with every recommendation.', 'Universal agreement is not a standard established or defended in the draft.'),
        ('The project will be useful if its evidence and limitations help residents discuss specific, feasible improvements.', 'This draws together careful measurement, local experience, transparent limits, and practical recommendations.'),
    ]),
    (2, '4.A', 3, 'Which additional evidence would most strengthen the comparison suggested in sentence 15?', 1, [
        ('The number of letters in the official names of the parking area and bus stop.', 'Name length has no bearing on heat exposure or use.'),
        ('Observations of how many people wait at each location, for how long, and during which hours.', 'These observations connect temperature conditions to the duration and frequency of people’s exposure.'),
        ('A volunteer’s ranking of the colors used on nearby buildings.', 'Aesthetic rankings do not establish how people use the two locations.'),
        ('The price of the most expensive thermometer available online.', 'Equipment price does not demonstrate differences in local use or exposure.'),
    ]),
    (6, '4.A', 4, 'The writer is considering adding a quotation from a landscaping company claiming that “trees solve urban heat.” What would be the most responsible revision decision?', 0, [
        ('Seek relevant evidence with a described method and report the conditions and limits of any findings used.', 'This would support a qualified claim with assessable evidence rather than relying on an interested source’s broad slogan.'),
        ('Use the slogan as proof because any company that sells trees must be an impartial authority.', 'Commercial experience does not make a broad claim automatically impartial or sufficient evidence.'),
        ('Present the slogan as a finding from the student trial without mentioning the company.', 'This would misattribute the statement and falsely represent the trial’s evidence.'),
        ('Reject all evidence about trees because this particular company has a commercial interest.', 'A concern about one source does not justify dismissing all relevant research or observations.'),
    ]),
    (6, '4.B', 2, 'Which revision of sentence 3 best provides a thesis that encompasses the whole draft?', 2, [
        ('Temperatures are sometimes measured with handheld instruments.', 'This factual statement is too narrow and does not advance the draft’s proposal.'),
        ('The neighborhood’s paved lot is the only place that needs new shade.', 'The draft does not establish that conclusion and advocates considering multiple forms of evidence.'),
        ('A student mapping project can guide shade proposals by combining consistent observations, residents’ experience, and practical constraints.', 'This states a defensible direction and previews the three strands developed throughout the draft.'),
        ('Residents should choose shade locations before any observations are collected.', 'This reverses the evidence-informed sequence the draft recommends.'),
    ]),
    (5, '6.A', 3, 'Which sentence after sentence 6 would best explain why the trial cannot support the conclusion in sentence 7?', 3, [
        ('The volunteers used notebooks with several different cover designs.', 'Notebook appearance does not explain the limits of the temperature comparison.'),
        ('The group should assume that the warmer site was measured with a broken instrument.', 'The draft supplies no evidence of equipment failure.'),
        ('A temperature difference always identifies a single cause with certainty.', 'This false generalization ignores the timing difference and other possible influences.'),
        ('Because the sites were measured at different times, the observations do not isolate the effect of shade from changing conditions.', 'This explains the specific comparison problem rather than merely announcing that more data are needed.'),
    ]),
    (3, '6.C', 4, 'Which revision of the third paragraph would most improve its development of a reliable measurement plan?', 1, [
        ('Delete sentence 10 and retain sentence 13 as the main supporting example.', 'This removes concrete measurement guidance and gives prominence to an irrelevant design detail.'),
        ('Replace sentence 13 with a plan to repeat measurements at comparable times on several days and label inaccessible sites as missing data.', 'This adds repeated comparable observations and transparent handling of coverage gaps, extending the paragraph’s reasoning.'),
        ('Move sentence 7 into the paragraph and repeat it after every procedural suggestion.', 'Repeating an unsupported conclusion does not strengthen the measurement plan.'),
        ('Add a description of the volunteers’ favorite restaurants without connecting it to the project.', 'An unrelated description does not develop the argument for comparable observations.'),
    ]),
    (5, '6.B', 2, 'Which transition should begin sentence 14 to connect the measurement plan with the discussion that follows?', 0, [
        ('Even with a consistent procedure,', 'This acknowledges the value of careful measurement while introducing the additional need to consider people’s experiences.'),
        ('Because procedures are unnecessary,', 'This contradicts the preceding paragraph’s central recommendation.'),
        ('For exactly the same reason that logos are attractive,', 'Logo design supplies no logical link between measurement and exposure.'),
        ('To prove that the trial was conclusive,', 'The draft identifies limits in the trial rather than claiming a conclusive result.'),
    ]),
    (8, '8.A', 3, 'The writer wants a precise, appropriately cautious replacement for sentence 7. Which choice best fits?', 2, [
        ('Trees are miraculous machines that erase all unpleasant weather.', 'The inflated claim is neither precise nor supported by the trial.'),
        ('The trial is completely worthless and should never be mentioned again.', 'This dismisses limited observations that can help identify improvements in method.'),
        ('The trial suggests a difference worth investigating, but its timing and small number of sites limit what we can conclude.', 'This preserves the reason for further study while accurately identifying limits in the evidence.'),
        ('The results are definitely universal, although nobody can explain why.', 'This asserts universality without evidence and undermines the draft’s careful approach.'),
    ]),
    (8, '8.B', 4, 'Which revision of sentence 19 most clearly distinguishes observed conditions from proposed changes?', 3, [
        ('A symbol could show shade, which could show a proposal, and it could identify it there.', 'The repeated vague pronouns blur what was observed and what is proposed.'),
        ('Proposed and observed shade should share an identical symbol because they are the same.', 'This contradicts sentence 18 and makes a proposal appear to be an existing condition.'),
        ('Having observed the shade, a separate symbol could propose a location for a tree.', 'The introductory modifier incorrectly suggests that a symbol made the observation.'),
        ('One symbol could mark existing shade; another could mark a proposed tree or shelter.', 'The parallel clauses identify the two distinct categories directly and concisely.'),
    ]),
])

QUESTIONS = TOOLS + HEAT
