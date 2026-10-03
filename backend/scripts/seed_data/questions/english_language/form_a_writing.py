"""Original revision sets: choices require attention to purpose and passage context."""
from .builders import passage_questions

GARDEN_PASSAGE = """(1) Last September, the courtyard behind our apartment building contained two benches, a broken planter, and a sign telling residents not to leave anything there. (2) By May, it contained twenty vegetable beds and a waiting list. (3) The change began when several tenants asked to use the unused space, but permission alone did not make a garden. (4) Residents organized watering shifts, translated planting instructions, and obtained a small grant for raised beds. (5) These tasks made the project possible for people whose work schedules or physical abilities would otherwise have kept them out.

(6) Some neighbors objected that a shared garden would become a private benefit for the few people who could claim a bed. (7) That concern was reasonable, especially in a building where balconies are rare. (8) The organizers therefore reserved several beds for shared harvests and scheduled open workdays that did not require membership. (9) A resident who cannot kneel can label seedlings at a table; a resident who works evenings can water in the morning. (10) They also painted the storage shed green, which is my favorite color.

(11) During the pilot season, organizers recorded participation rather than simply counting the vegetables harvested. (12) Of the forty households that joined at least one workday, sixteen did not hold individual beds. (13) This small local count cannot predict participation in other buildings, but it does show that access extended beyond the people who received plots. (14) The garden may also reduce residents' grocery bills, though organizers have not yet measured expenses or harvest values.

(15) Our housing association is now considering gardens at three other properties. (16) It should fund accessible beds and coordination time, as well as seeds and soil. (17) Giving residents a patch of ground is only a beginning; giving them a workable way to share it is the real investment."""

GARDEN = passage_questions(
    passage_id='lang-a-garden', title='Draft: A Garden People Can Share', mode='writing',
    context='Original practice draft for a tenant newsletter. All details and participation figures are fictional. Answer each question independently; assume other sentences stay unchanged.',
    passage=GARDEN_PASSAGE, items=[
    (4, '2.A', 2, 'The writer wants the opening to draw readers into the change described in the draft. Should sentences 1 and 2 be kept?', 0, [
        ('Yes, because their before-and-after details make the transformation concrete.', 'The contrast between an unused courtyard and occupied beds introduces the project through observable change.'),
        ('Yes, because they establish that vegetable gardening always increases property values.', 'The sentences provide no property-value evidence and make no universal claim.'),
        ('No, because an argument about shared space cannot begin with a description.', 'A concrete description can introduce the problem and engage this audience.'),
        ('No, because the waiting list proves the project was unsuccessful.', 'Demand alone does not prove failure; the draft investigates how access can be broadened.'),
    ]),
    (6, '4.B', 3, 'Which replacement for sentence 3 would best preview the draft’s main argument?', 2, [
        ('Many buildings have outdoor areas, and some residents enjoy growing vegetables.', 'This general observation does not establish the argument about coordination and access.'),
        ('The garden should receive funding because gardens are nicer than empty spaces.', 'This claim omits the draft’s central reasoning about equitable participation.'),
        ('Permission opened the courtyard, but deliberate planning made it a resource that more residents could share.', 'This previews both the initial opportunity and the design choices developed in subsequent paragraphs.'),
        ('Anyone can create a successful garden without assistance if they are sufficiently determined.', 'The draft emphasizes grants, accessible beds, schedules, and coordination rather than determination alone.'),
    ]),
    (1, '4.A', 3, 'Which additional detail after sentence 5 would most directly support its claim?', 1, [
        ('The first meeting was held on a Tuesday evening in the lobby.', 'Meeting time and location alone do not explain how barriers to participation were reduced.'),
        ('Several residents using wheelchairs planted in beds designed with open space beneath them.', 'This specific example shows how physical design enabled participation that might otherwise be blocked.'),
        ('Many residents preferred tomatoes to squash.', 'Crop preferences do not directly support the claim about schedules and physical access.'),
        ('The building has been managed by the association for fourteen years.', 'The management history does not establish the effect of the organizers’ access measures.'),
    ]),
    (2, '2.B', 3, 'To address tenants who worry that they cannot commit to regular gardening, which sentence should follow sentence 9?', 3, [
        ('Dedicated gardeners should be willing to spend every free hour in the courtyard.', 'This increases the perceived commitment rather than responding to the audience’s concern.'),
        ('Gardening has been practiced by human societies for thousands of years.', 'The historical generalization does not answer a practical concern about limited time.'),
        ('People who do not take part have no reason to discuss the garden’s future.', 'Excluding concerned tenants undermines the argument for shared access.'),
        ('Even a single workday offers a way to contribute without taking responsibility for a plot.', 'This directly explains a low-commitment option already consistent with the open-workday policy.'),
    ]),
    (3, '6.A', 4, 'Which sentence would best explain how the evidence in sentence 12 supports the argument?', 0, [
        ('Because two-fifths of participating households had no individual plot, the shared activities reached beyond plot holders.', 'Sixteen of forty is two-fifths; the commentary connects participation data to inclusive access without overgeneralizing.'),
        ('Since forty households participated, every household in the building must have benefited equally.', 'The building’s total households and distribution of benefits are not given.'),
        ('The figures prove that shared gardens cost less than every other use of outdoor space.', 'The count contains no comparative cost information.'),
        ('The number sixteen is smaller than forty, so individual beds should be eliminated.', 'That arithmetic does not establish that eliminating beds would improve access.'),
    ]),
    (5, '6.B', 2, 'Which transition best replaces “therefore” in sentence 8 while preserving the logical relationship?', 2, [
        ('Nevertheless,', 'This would suggest that the organizers acted despite the access concern rather than responding to it.'),
        ('For an unrelated reason,', 'The reserved beds directly address the preceding concern.'),
        ('In response,', 'The design changes answer the worry that only plot holders would benefit.'),
        ('Similarly,', 'The sentence describes a response, not a parallel example of the same concern.'),
    ]),
    (8, '8.A', 3, 'The writer wants sentence 10 to strengthen the focus on access and maintain the draft’s measured tone. Which revision best achieves that goal?', 1, [
        ('The beautiful green shed makes the entire courtyard absolutely perfect.', 'Subjective praise and an absolute claim do not advance the argument about access.'),
        ('They posted the tool schedule in the shed so residents could plan visits around other obligations.', 'The revision supplies a practical access measure in the draft’s matter-of-fact style.'),
        ('Their glorious shed proves that all objections to community gardens are foolish.', 'The dismissive tone contradicts the respectful treatment of reasonable objections.'),
        ('The shed was painted a color that could be described as green.', 'This wordier version preserves an irrelevant color detail rather than strengthening the focus.'),
    ]),
    (9, '4.C', 4, 'Which revision of sentence 14 most appropriately handles the limits of the available evidence?', 3, [
        ('The garden eliminates grocery costs for all residents.', 'Neither expenses nor harvest values have been measured, and the absolute claim is unsupported.'),
        ('The garden cannot affect grocery costs because no study has been conducted.', 'Lack of measurement does not establish that no effect exists.'),
        ('The garden saves enough money to pay for expansion, according to the workday count.', 'Participation counts cannot establish monetary savings or funding sufficiency.'),
        ('Savings are a possible benefit, but the association should measure costs and harvest values before relying on that claim.', 'This preserves a plausible possibility while making the evidentiary limit and next step explicit.'),
    ]),
    (7, '8.B', 3, 'Which revision of sentence 16 most clearly emphasizes that coordination deserves funding alongside physical materials?', 2, [
        ('Seeds, soil, and the beds, coordination was funded by the association.', 'The sentence is grammatically unclear and shifts the recommendation into an unsupported past-tense claim.'),
        ('The association, which funds things, should provide various forms of assistance.', 'This removes the specific comparison between coordination and material costs.'),
        ('Along with seeds, soil, and accessible beds, the association should fund the time needed to coordinate shared use.', 'The sentence places physical supplies alongside coordination and explains the latter’s purpose.'),
        ('The association should fund seeds and soil, which make coordination unnecessary.', 'This contradicts the draft’s evidence that organizing is essential.'),
    ]),
    (7, '2.A', 4, 'Which conclusion would best preserve and extend the purpose of sentence 17?', 1, [
        ('Gardens are pleasant places, and many people enjoy pleasant places.', 'The repetition contributes no insight into the argument about shared access.'),
        ('As the program expands, its success should be judged by who can participate as well as by what grows.', 'This draws the evidence about participation into a clear criterion for future decisions.'),
        ('The association should immediately replace all common areas with private plots.', 'This contradicts both shared access and the draft’s qualified recommendation.'),
        ('Next month, this newsletter will feature a recipe for tomato soup.', 'The announcement changes the subject rather than concluding the argument.'),
    ]),
])

ARCHIVE_PASSAGE = """(1) Our town library has begun scanning its old newspapers. (2) The project promises that anyone with an internet connection will soon be able to search decades of local reporting from home. (3) For a student working after the library closes or a former resident living far away, that promise matters. (4) Yet a searchable file is not the same thing as a complete public record.

(5) The first problem is what survives. (6) The library owns nearly every issue of the former daily newspaper but only scattered issues of the neighborhood newsletters printed in several languages. (7) Digitizing the larger collection first is efficient, but efficiency alone can make the most powerful historical voices even easier to hear. (8) A second problem is how material becomes searchable. (9) Scanning software sometimes mistakes damaged letters for other characters. (10) In a trial of fifty pages from one fragile newsletter, volunteers found errors in thirty of the automatically transcribed headlines. (11) The sample was small and deliberately selected for poor print quality, so it cannot tell us the error rate for the entire archive.

(12) These difficulties do not justify abandoning the project. (13) They do suggest that the library should describe missing material, preserve images beside transcriptions, and invite corrections from readers. (14) Residents could help identify names and places that software gets wrong. (15) Allowing public suggestions also requires a review process; a confident correction may itself be mistaken. (16) The library could display proposed changes separately until staff or trained volunteers check them against the page images.

(17) A digital archive should make its own limits visible. (18) Otherwise, a search returning no results may look like evidence that a person, event, or community left no record at all. (19) The town’s past will never fit perfectly into a search box, but we can design the box so that it does not pretend otherwise."""

ARCHIVE = passage_questions(
    passage_id='lang-a-archive', title='Draft: What a Search Cannot Find', mode='writing',
    context='Original practice draft for a local newspaper’s opinion page. The archive, trial, and data are fictional. Consider each proposed revision independently.',
    passage=ARCHIVE_PASSAGE, items=[
    (4, '2.A', 3, 'Which sentence could best precede sentence 1 to introduce the issue without overstating the draft’s argument?', 2, [
        ('All historical records are equally reliable once they are digitized.', 'The draft distinguishes incomplete collections and transcription errors, contradicting this absolute claim.'),
        ('Technology has made libraries unnecessary for the study of history.', 'The draft gives the library continuing roles in preservation, context, and verification.'),
        ('Making local history easier to reach also changes which parts of that history people are likely to find.', 'This connects improved access with selection and search limits, the draft’s central tension.'),
        ('No one should use a searchable archive until every error has been removed.', 'The draft recommends useful improvements without demanding perfection before access.'),
    ]),
    (8, '2.B', 2, 'Which detail would best expand sentence 3 for readers who doubt the value of remote access?', 0, [
        ('A researcher who cannot travel to the library could compare reports from home.', 'This gives another concrete case where remote access removes an obstacle.'),
        ('The library’s front steps were replaced five years ago.', 'A building-maintenance detail does not explain the value of remote research.'),
        ('The scanning equipment is available in several colors.', 'Equipment color is unrelated to the audience’s concern about usefulness.'),
        ('Residents should stop asking questions about the cost of technology.', 'Dismissing concerns does not offer evidence of a benefit.'),
    ]),
    (2, '4.B', 4, 'Which revision of sentence 4 would most clearly state the position developed throughout the draft?', 3, [
        ('Digital newspapers are interesting because they contain many different stories.', 'The observation is too general to organize the argument about limitations and safeguards.'),
        ('The project should stop because incomplete evidence can never be useful.', 'The draft expressly rejects abandoning the project.'),
        ('The library should scan only documents that software can read without errors.', 'This would exclude damaged minority records and contradict the proposed correction process.'),
        ('The library should expand digital access while showing gaps in its holdings and uncertainty in its transcriptions.', 'This states both the benefit retained and the two limitations addressed in the body.'),
    ]),
    (3, '6.C', 3, 'The writer wants to develop the reasoning in sentence 7. Which added example would be most effective?', 1, [
        ('The daily newspaper usually printed more pages on Sundays than on Mondays.', 'Page counts by weekday do not explain which historical voices become more visible.'),
        ('A search might return many accounts by city officials but miss residents’ responses published only in an uncollected newsletter.', 'The example illustrates how unequal preservation can create unequal visibility in search results.'),
        ('The library closes earlier on Saturdays than on weekdays.', 'Opening hours concern access but do not develop the claim about whose records survive.'),
        ('The town once had a newspaper delivery route that crossed a bridge.', 'This historical detail does not connect the collection imbalance to representational consequences.'),
    ]),
    (3, '4.A', 4, 'Which additional evidence would most directly support the claim in sentence 9?', 2, [
        ('A survey showing that many residents enjoy reading old advertisements', 'Reader interest does not establish transcription errors.'),
        ('A list of the software company’s other products', 'A product list does not show how the transcription software handles damaged type.'),
        ('A page image showing a family name beside the different name produced by its automated transcription', 'This concrete comparison demonstrates the specific character-recognition problem described.'),
        ('A statement that all printed newspapers eventually become difficult to store', 'Storage challenges are distinct from software’s misreading of characters.'),
    ]),
    (9, '4.C', 4, 'The writer is considering deleting sentence 11. Which assessment is most accurate?', 0, [
        ('Keep it, because the sample’s selection limits what the trial can establish about the full archive.', 'Purposively choosing poor-quality pages prevents treating the observed error proportion as a representative archive-wide estimate.'),
        ('Keep it, because it proves that the remaining pages contain no errors.', 'A limited sample cannot establish that unexamined pages are error-free.'),
        ('Delete it, because acknowledging a limitation always weakens an argument.', 'Responsible qualification makes the inference more accurate and credible.'),
        ('Delete it, because thirty out of fifty means every page contains an error.', 'Thirty of fifty is not all, and the observation concerns headlines on the selected pages.'),
    ]),
    (5, '6.B', 3, 'Which transition should begin sentence 12 to clarify its relationship to the preceding paragraph?', 3, [
        ('For example,', 'The sentence is not an additional example of a transcription error.'),
        ('Consequently, and without exception,', 'That phrasing implies an absolute consequence rather than a qualified pivot toward solutions.'),
        ('At the same location,', 'The relationship is argumentative, not a change or continuity of physical location.'),
        ('Even so,', 'The transition acknowledges the difficulties while rejecting abandonment as the response.'),
    ]),
    (5, '6.A', 3, 'Which sentence would best follow sentence 14 to explain why residents’ contributions could be valuable?', 1, [
        ('Anyone who makes a correction should be trusted without further checking.', 'This conflicts with the review requirement developed in sentences 15 and 16.'),
        ('Their knowledge of local families and landmarks can help resolve spellings that a recognition program cannot interpret in context.', 'This explains the distinctive information residents contribute while remaining compatible with verification.'),
        ('Computers process information using electronic components.', 'The technical generality does not explain the value of local knowledge.'),
        ('Most residents prefer short documents to long ones.', 'The preference is unsupported and unrelated to identifying names or places.'),
    ]),
    (7, '8.C', 2, 'Which version of sentence 15 most clearly expresses its relationship between a recommendation and its explanation?', 0, [
        ('Allowing public suggestions also requires a review process: a confident correction may itself be mistaken.', 'The colon appropriately introduces the reason a review process is needed after a complete clause.'),
        ('Allowing public suggestions also requires, a review process a confident correction may itself be mistaken.', 'The comma separates the verb from its object and fails to separate the two complete clauses.'),
        ('Allowing public suggestions also requires a review process because.', 'The subordinating word is left without a clause explaining the reason.'),
        ('Allowing public suggestions also requires a review process a confident correction, may itself be mistaken.', 'The clauses run together, and the comma improperly separates the second subject from its verb.'),
    ]),
    (8, '8.B', 3, 'Which revision best combines sentences 17 and 18 while preserving their reasoning?', 2, [
        ('A digital archive should hide its limits because readers dislike searches that return no results.', 'This reverses the recommendation and invents a rationale about readers’ preferences.'),
        ('A digital archive has limits, no results, and evidence that communities have no history.', 'The compressed list loses the distinction between a misleading appearance and a justified inference.'),
        ('A digital archive should make its limits visible so that an empty search is not mistaken for proof that no record exists.', 'The sentence clearly links transparency to preventing the specific interpretive error.'),
        ('Although an empty search proves no record exists, an archive should display its limits.', 'An empty search does not establish nonexistence; the revision contradicts the draft.'),
    ]),
    (6, '8.A', 4, 'Which alternative to sentence 19 best maintains the draft’s measured, constructive tone?', 3, [
        ('Search boxes are useless traps, and only foolish people rely on them.', 'The insult and blanket rejection conflict with the draft’s balanced support for digital access.'),
        ('The library’s awesome technology will totally fix history for everyone.', 'The casual exaggeration contradicts the acknowledged limits.'),
        ('A perfect record is impossible, so improvements are not worth attempting.', 'This abandons the constructive measures the draft recommends.'),
        ('The goal is not an archive without gaps, but one that helps readers recognize and investigate them.', 'This conclusion accepts unavoidable limits while identifying a realistic public benefit.'),
    ]),
])

QUESTIONS = GARDEN + ARCHIVE
