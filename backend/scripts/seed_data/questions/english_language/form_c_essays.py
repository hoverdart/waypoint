"""Third original essay set. All source documents and scenarios are fictional."""
from .form_a_essays import make_essay
from .form_c_reading import SKY_PASSAGE

SOURCES = """Source A — Library director's proposal (fictional)
The municipal library proposes digitizing a collection of neighborhood photographs donated over forty years. Online access would let former residents, teachers, and researchers consult images without traveling to the reading room. The director recommends scanning 2,000 photographs in the first year, beginning with material whose ownership and permission records are clear. The budget includes scanning equipment and temporary staff but no separate allowance for answering removal requests or correcting descriptions after publication. The proposal treats the number of scans uploaded as its main measure of success. Original photographs would remain in storage.

Source B — Donor's letter (fictional)
My father gave the library photographs from his grocery shop because he wanted the neighborhood to remember it. The envelopes include customers' names and notes about purchases made on credit. I am glad that someone might identify a grandparent in a picture. I am less sure that a private debt written on an envelope should become searchable alongside that person's face. Giving a photograph to a local collection and expecting it to appear in a worldwide search are different experiences. Please contact families where possible, and explain what the library will do when someone raises a concern. Do not assume that every family member will agree about the answer.

Source C — Six-month trial in another invented library
These figures describe use and staff work during a limited trial. The trial did not measure users' learning, the seriousness of privacy concerns, or the experience of people without internet access.

Collection segment | Images uploaded | Page views | Correction requests | Removal requests
Street scenes      | 300             | 9,000      | 12                  | 2
School groups      | 150             | 12,000     | 28                  | 14
Business interiors | 150             | 6,000      | 20                  | 9

A page view is not a unique visitor. Collection segments differ in size and subject matter. A request does not establish that the library made an error or that removal is required. Staff estimated that reviewing requests occupied 70 hours during the trial; the table does not divide those hours by segment.

Source D — Local historian's commentary (fictional)
A misnamed person can become harder to identify after digitization if the mistaken label is copied into other collections. Yet keeping every uncertain photograph offline also prevents people from contributing knowledge. A catalog can distinguish a verified name from a tentative identification and retain a record of changes. It should let a user see why a description changed, not quietly replace one certainty with another. The public may help repair the record, but volunteers' contributions still need review. An archive is not made reliable merely by being searchable.

Source E — Proposed website mockup (fictional visual source)
+----------------------------------------------------+
| OUR TOWN: EVERY FACE, EVERY STORY                    |
| [ Search a name __________________ ] [ FIND ]       |
|                                                    |
| PHOTO: customers standing outside a grocery shop    |
| Caption: "M. Vale and neighbors, approximately 1940" |
| [Download high-resolution image] [Share]             |
|                                                    |
| 2,000 IMAGES ONLINE — THE PAST, COMPLETE             |
+----------------------------------------------------+
The pictured layout is a concept, not a working website. It shows no uncertainty label, explanation of permission, or link for reporting a concern. The phrase "approximately 1940" appears in the caption, but the name is not marked as tentative. The mockup was produced by the fictional project team, not an actual library.

Source F — Community workshop summary (fictional)
Participants described different barriers to using the existing collection. Former residents wanted remote access; several older residents wanted help navigating the catalog; a teacher wanted images that could be projected with readable captions. Others asked the library to preserve in-person assistance and offer descriptions in the languages used locally. One participant warned that counting only online activity could make people who still use the reading room appear less important. The workshop drew 24 self-selected attendees and cannot establish the prevalence of these views across the town. It can identify issues the library should investigate before choosing a single model of access."""

SYNTHESIS_PROMPT = """Synthesis essay — A public archive online
Suggested writing time: 40 minutes after reading the sources. All sources and numbers are original fictional practice materials.

A municipal library is considering publishing its neighborhood photograph collection online. Write an essay that develops your position on the factors the library should prioritize when deciding how to carry out the project. Synthesize evidence from at least three sources, identify sources by letter, and explain how their evidence supports your reasoning. Consider relevant tensions or limitations rather than simply summarizing the documents.

""" + SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The library should expand access to its photographs, but it should define publication as an ongoing responsibility rather than a scanning target. The most important priorities are meaningful access, transparent descriptions, and a workable process for reviewing concerns. Without those commitments, a project that makes images easier to find may also make mistakes and private information harder to contain.

Remote access has real value. Source A identifies former residents and researchers who cannot easily reach the reading room, while Source F describes teachers who need usable captions and residents who need help with the catalog. These sources together show why access cannot be measured simply by whether a file exists online. A legible image with a clear description and navigation assistance serves people differently from an inaccessible upload. The library should retain in-person help while developing the website, so expanding one route does not quietly close another.

The library also needs to distinguish possession of a photograph from a settled decision about publishing everything associated with it. Source B welcomes recognition of family members but questions making private credit notes searchable. That distinction argues for reviewing the information accompanying an image, not for refusing digitization altogether. The writer also warns that relatives may disagree. Consultation therefore cannot be a promise that every request will produce immediate removal; it needs published criteria, a responsible reviewer, and an explanation of decisions.

The trial in Source C makes the staffing implications visible. School-group images received more views and more requests than the larger street-scene segment, but those raw totals do not prove that school photographs should be excluded. Page views are not unique users, and a request is not proof of an error. The seventy hours of review do show why the budget in Source A is incomplete: processing files is not the only work publication creates. The library should fund review and measure its response time alongside uploads.

Accuracy requires a similar continuing commitment. Source D argues for marking tentative identifications and preserving corrections. That approach exposes the weakness of Source E's claim that the past is complete. Its confident slogan and easy sharing controls encourage users to circulate material, while the mockup offers no clear way to question it. A visible uncertainty label and reporting link would make the interface more consistent with what an archive can actually know.

A phased project could begin with clearly documented material while building these procedures. Success would mean that more people can consult the collection, understand its limits, and help improve it. The number of scans remains useful, but it cannot stand in for the quality of the relationship the library creates with the people represented and the people searching.

This model is one supported position. Other priorities can be defended through accurate source use and a coherent line of reasoning."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — Opening a door to inquiry
Suggested time: 40 minutes.

At the opening of a community observatory, an astronomy educator addresses donors, volunteers, and residents. Read the original fictional speech below. Write an essay analyzing how the speaker's rhetorical choices develop a vision of the observatory's public purpose. Support your analysis with specific evidence and explain how the choices respond to the occasion and audience.

""" + SKY_PASSAGE

RHETORICAL_MODEL = """One defensible model approach:

The educator uses the observatory's opening to turn celebration into a shared responsibility for inquiry. By correcting a familiar promotional phrase, expanding the list of people who deserve thanks, and modeling a response to unexpected questions, the speaker defines success as more than ownership of a telescope. The speech honors the audience's achievement while asking donors and volunteers to judge it by what visitors can experience.

The opening correction that the stars have not moved initially sounds like a scientist's insistence on literal accuracy. The following claim, “What has moved is a door,” changes the scale of the celebration. Rather than crediting the institution with transforming distant objects, the speaker locates its achievement in a nearby barrier that has opened. The child reaching an eyepiece gives that distinction a concrete beneficiary. On an occasion that invites grand claims, the modest image offers an ambitious but credible public purpose.

The acknowledgments extend the same reasoning. Financial supporters receive explicit thanks, so the speaker does not require donors to see recognition as a mistake. The bus driver's trial route, the cleaner's observation, and the carpenter's rebuilt platform then broaden what counts as enabling science. Each example concerns a practical detail that determines whether people can participate. The contrast between seeing farther and noticing what is near connects access work to the telescope's celebrated function rather than treating it as a separate administrative matter.

The damaged-chart anecdote makes the speaker a learner as well as an authority. The unintended river on Mars provides humor, but the student’s question supplies the episode's argumentative force. While the educator protects an object, the student examines the reliability of representations. Admitting that the question was better than those planned models the openness the speech later requests from volunteers. The anecdote therefore gives the audience a practical reason to welcome interruptions instead of treating them as failures of a prepared lesson.

Cloudy evenings present a less cheerful limit. The speaker recognizes disappointed visitors and specifies ordinary obligations such as honest notices and chairs. Only then does the speech claim that questions have value in their own right. This order matters: curiosity is not offered as an excuse for poor treatment. The short commands “Ask what” and “Ask when” subsequently translate that principle into actions volunteers can remember. Listening becomes a method, not merely an admirable attitude.

Finally, the speaker accepts annual counts while describing a visitor whose changed attention may escape them. Returning to the unchanged distance of the stars closes the speech around the opening distinction. The observatory cannot shorten that distance, but it can change a person's encounter with a familiar sky. The audience is asked to preserve that possibility through both practical access and intellectual hospitality.

Other evidence-based analyses can emphasize different choices; naming devices without explaining their effects would not accomplish the same work."""

ARGUMENT_PROMPT = """Argument essay — The value of being a beginner
Suggested time: 40 minutes.

Learning something unfamiliar often requires a person who is capable in one area to accept being inexperienced in another. Write an essay arguing your position on the value of deliberately becoming a beginner. Support your argument with specific evidence from reading, knowledge, observation, or experience, and explain the reasoning connecting that evidence to your position. You may qualify your claim. Clearly identify hypothetical examples rather than presenting invented events as facts."""

ARGUMENT_MODEL = """One defensible model approach using explicitly hypothetical examples:

Deliberately becoming a beginner is valuable when it makes a person more willing to examine assumptions and more attentive to other people's learning. Its value does not come from inexperience itself. It comes from undertaking an unfamiliar task seriously enough to notice how progress actually happens. That distinction also explains why beginning again should not be confused with rejecting expertise.

Imagine an experienced school debater joining a beginner drawing class. In debate, a quick response may signal competence; in drawing, the same impulse may cause the student to sketch what an object is supposed to look like rather than its actual proportions. A teacher asks the student to compare two angles before adding another line. If the student persists, the new activity can expose a habit that success elsewhere has rewarded. The lesson is not that quick thinking is always harmful. It is that a useful habit in one setting may need adjustment in another. Becoming a beginner gives the student a concrete reason to test that distinction.

A second hypothetical example concerns an accomplished musician learning to swim as an adult. The musician is used to practicing difficult passages and may expect physical skill to respond immediately to disciplined repetition. In the pool, fear and breathing disrupt that expectation. An instructor's small steps and specific feedback become essential. Later, when the musician teaches a child, this experience may make a slow first attempt easier to interpret as part of learning rather than evidence of insufficient effort. The benefit depends on reflection: struggling alone does not automatically make anyone patient, but remembering what support made possible can improve how an expert supports others.

There are limits. A person cannot responsibly treat every setting as an opportunity for unsupervised experimentation. A novice handling dangerous equipment needs instruction, and an organization should not dismiss qualified workers merely to celebrate fresh perspectives. Nor does beginning many activities without sustained effort necessarily produce insight. The debater must actually learn to observe, and the musician must practice the unfamiliar skill; otherwise beginner status can become an excuse to avoid the demands of competence.

Choosing a manageable unfamiliar activity therefore offers a useful balance. It preserves respect for expertise while interrupting the assumption that expertise transfers automatically. A person can remain accomplished and still need elementary guidance. Accepting that combination makes learning less threatening and may make one's own knowledge easier to share. The strongest reason to become a beginner is not to forget what one knows, but to remember what knowing required.

These examples are invented illustrations, not biographical reports. Accurate personal, literary, or historical evidence can support other defensible arguments."""


def essay(kind, unit, skill, prompt, model):
    question = make_essay(kind, unit, skill, prompt, model)
    question['skill_tags'] = [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-c-{kind}']
    return question


QUESTIONS = [
    essay('synthesis', 3, '4.A', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    essay('rhetorical-analysis', 8, '1.B', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    essay('argument', 2, '4.B', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
