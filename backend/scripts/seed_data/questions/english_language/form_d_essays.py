"""Fourth original essay set: repair policy, civic testimony, and public recognition."""
from .form_a_essays import make_essay
from .form_d_reading import BRIDGE_PASSAGE

SOURCES = """Source A — Municipal purchasing proposal (fictional)
The town replaces approximately 240 office chairs each year. Purchasing staff propose giving repairability a formal place in future bids. Vendors would describe how worn parts can be replaced, how long spare parts will remain available, and whether repairs require proprietary tools. The lowest purchase price would remain relevant but would no longer determine the decision by itself. The proposal does not yet specify how the town would verify a vendor's promises or handle a supplier that stops trading. Staff suggest beginning with one department rather than changing every contract at once.

Source B — Maintenance supervisor's memorandum (fictional)
A repairable chair is useful only when we have the part, instructions, tools, and time to repair it. We currently store several broken chairs while waiting for replacement mechanisms. Some repairs take minutes; others require more labor than a replacement would cost. Comparing a new chair's price with the price of a spare part alone hides that labor. I support clearer specifications, but the pilot budget must include staff training, storage, and a process for deciding when repair is no longer sensible. Otherwise, repairability will be an attractive word attached to a room full of unusable furniture.

Source C — Illustrative supplier comparison (fictional data)
These are invented quotations for a hypothetical bid, not actual product prices. Projected service life assumes routine maintenance and is not a guarantee.

Model | Purchase price | Replacement seat | Parts commitment | Projected service life
A     | 100 units      | unavailable      | none             | 4 years
B     | 145 units      | 30 units         | 6 years          | 7 years
C     | 170 units      | 25 units         | 10 years         | 9 years

The comparison excludes labor, storage, shipping, downtime, financing, and disposal. It does not show how often a seat will need replacement or whether other components are equally available. The longest parts commitment does not necessarily establish the lowest total cost.

Source D — Small supplier's testimony (fictional)
A requirement to hold every spare part for ten years might favor large firms able to finance extensive inventories. A small workshop may instead use standard fittings that another maker can supply. The town should ask whether an item can actually be repaired, not merely whether its original seller can promise a large warehouse. We could provide diagrams and dimensions for common parts, but we cannot guarantee that our business will exist forever. An effective rule should reward usable information and interchangeable components as well as long commitments.

Source E — Proposed repairability label (fictional visual)
+------------------------------------------+
| REPAIR READY                             |
|          ★ ★ ★ ★ ☆                       |
| Replaceable seat: YES                     |
| Instructions: available online            |
| Parts: contact supplier                  |
+------------------------------------------+
The concept label gives no explanation of the four-star rating. It does not state whether a customer can access instructions without an account, how long parts will be sold, or what tools a repair requires. The label is an invented design for this exercise.

Source F — Employee consultation summary (fictional)
Employees said that keeping furniture in use matters, but an empty workstation while a chair awaits repair also has a cost. Several requested a small pool of safe replacement chairs during maintenance. Others noted that comfort needs differ and asked that a purchasing rule not force everyone into the same design solely because it is easy to repair. The consultation included 31 volunteers from two departments. It identifies possible concerns but cannot establish how common those concerns are across the whole workforce. Participants proposed recording repair time and user feedback during the pilot."""

SYNTHESIS_PROMPT = """Synthesis essay — Purchasing for repair
Suggested writing time: 40 minutes after reading the sources. All six sources and numerical examples are original fictional practice materials.

A town is considering making repairability a formal criterion when purchasing office furniture. Write an essay developing your position on the factors that should guide the policy. Synthesize evidence from at least three sources, identify sources by letter, and explain how the evidence supports your reasoning. Consider relevant limitations and competing priorities.

""" + SOURCES

SYNTHESIS_MODEL = """One defensible model approach:

The town should give repairability a meaningful role in purchasing, but it should evaluate a working repair system rather than a product's reassuring label. A limited pilot should test access to parts and instructions, the full cost of maintenance, and employees' ability to use the furniture. These criteria would make the policy answerable to actual performance rather than the appearance of responsibility.

First, the town needs verifiable specifications. Source A proposes asking about parts and tools, which is more useful than relying on the unexplained stars in Source E. The label says that a seat can be replaced but leaves out who can obtain instructions, how long parts will exist, and what equipment the work requires. A purchaser cannot infer those conditions from the word “ready.” Bids should therefore provide accessible instructions and concrete terms that staff can check before awarding a contract.

Verification should not become an unnecessarily narrow rule about who stores the parts. Source D explains that standard fittings may remain available from other makers even if the original small supplier closes. That possibility complicates the assumption that a long promise from one company is always the best protection. The town should evaluate whether repairs can realistically continue, including through interchangeable components, while requiring enough documentation to assess those alternatives.

Cost also needs a wider definition. In Source C, Model A has the lowest purchase price, but no replacement seat. Models B and C offer more possibilities at higher initial prices. The table cannot identify a winner because it omits labor and does not say how often repairs will be needed. Source B supplies the practical reason for that limitation: possessing a repairable object is different from having the time and equipment to repair it. The pilot should record labor, parts, storage, and downtime rather than comparing a spare seat's price with an entire new chair.

Employees' experience belongs in that evaluation as well. Source F suggests that a small reserve of safe chairs could reduce disruption while repairs occur. It also warns that uniform repairability should not eliminate needed differences in comfort and fit. The consultation is small and self-selected, so its concerns are questions to investigate rather than a statistical verdict. Tracking repair time alongside user feedback would help the town see whether a policy that extends an object's life also supports the people using it.

Starting in one department, as Source A suggests, would make these commitments testable. The town could revise its criteria before expanding them and explain why it chooses one bid over another. Repairability deserves attention because replacement is not the only possible response to wear. To realize that possibility, the purchasing rule must account for the people, information, and resources that turn a repairable chair back into a usable one.

Other positions can be defended. This model illustrates source connections and limitations rather than a required recommendation."""

RHETORICAL_PROMPT = """Rhetorical analysis essay — Asking for an accountable decision
Suggested time: 40 minutes.

In the original fictional testimony below, a shopkeeper addresses a council about a footbridge that has been closed for seven months. Write an essay analyzing how the speaker's rhetorical choices develop the argument for a timely, accountable decision. Use specific evidence and explain how the choices respond to the speaker's interests, audience, and purpose.

""" + BRIDGE_PASSAGE

RHETORICAL_MODEL = """One defensible model approach:

The shopkeeper argues for an accountable decision without pretending that the council faces a simple construction problem. The testimony combines acknowledged interests, carefully bounded concessions, and repeated demands for explicit reasons. These choices give the speaker a way to challenge delay while respecting the council's obligations to consider safety and cost.

The opening lists the work already done by engineers, the finance committee, and residents. Calling those descriptions necessary initially grants legitimacy to the process. The short statement that none carries a person across the river then identifies its limit. The contrast does not deny that understanding a problem matters; it challenges the point at which explanation becomes a substitute for action. That distinction prepares the audience to hear the later request as a demand for responsibility rather than impatience with expertise.

The speaker next admits a business interest in reopening. This disclosure anticipates a reason council members might distrust the petition, but it does not claim that honesty alone proves the proposal right. Pupils, a carer, and clinic users establish that the same crossing serves different purposes. Saying that interests meet without being identical turns the speaker's acknowledged stake into one part of a broader argument. The audience is invited to evaluate overlapping needs rather than choose between a supposedly selfless public and a selfish shopkeeper.

Concessions about a permanent replacement further limit an easy objection. The speaker hopes it will last and rejects purchasing a cheap danger. The contrast between fifty years and six months then separates long-term planning from the immediate access problem. Similarly, the inspection requirements in the engineer's report become conditions that need a management plan, not details the speaker ignores. This treatment lets the testimony press for action while preserving a legitimate route to rejecting an unsafe proposal.

The cost paragraph makes an analogous move. It accepts inspection and removal expenses while pointing to burdens spread among residents. The admission that not every inconvenience can be priced prevents the argument from presenting invented precision as evidence. The ledger image instead asks the council to recognize that a difficult measurement does not erase an experienced cost.

Finally, the speaker narrows the demand from approval that night to publication, assigned responsibility, and a dated decision. The parallel conditional commands ask the council to identify an unmet safety condition or show a financial comparison. Rejection remains possible, but it must become an answer people can assess. The closing metaphor of an increasing distance between description and duty returns to the physical crossing while shifting the first required action into the council chamber. Before building a bridge, the council can bridge that gap by accepting responsibility for a reasoned decision.

Other supported interpretations are possible. Effective analysis explains how choices advance the argument, rather than simply labeling the concessions or metaphors."""

ARGUMENT_PROMPT = """Argument essay — Recognition and worthwhile work
Suggested time: 40 minutes.

Public recognition can encourage people to contribute, but it can also affect which contributions receive attention. Write an essay arguing your position on the role recognition should play in motivating worthwhile work. Use specific evidence from reading, knowledge, observation, or experience, and explain how it supports your reasoning. Consider relevant qualifications. Label hypothetical examples clearly and do not invent factual quotations."""

ARGUMENT_MODEL = """One defensible model approach using explicitly hypothetical examples:

Recognition can strengthen worthwhile work when it makes contributions visible and invites others to participate. It becomes less useful when people must reshape the work to fit what is easiest to celebrate. Organizations should therefore recognize both conspicuous achievements and the continuing labor that makes them possible, while avoiding the claim that an award measures the whole value of a contribution.

Imagine a school robotics team whose assembly celebrates only the student who presents the finished machine. A confident presenter can genuinely help the team explain its work. Yet other students may have spent weeks documenting failed trials, ordering parts, and checking connections. If only the final presentation receives credit, next year's members may compete for the visible role while neglecting the less visible tasks. Recognition has not simply rewarded effort; it has supplied a model of which effort counts. A more useful ceremony would describe several concrete contributions and explain their relationship to the result.

A hypothetical neighborhood cleanup illustrates another benefit of recognition. A short public account of volunteers' work might attract new participants who had not known the project existed. Naming the coordination required can also help residents understand why a clean path is not an accidental condition. In this case, visibility supports the activity rather than merely flattering the volunteers. But a photograph of a single event could mislead if it omits the person who returns each week to empty bins. The recognition should tell an accurate story about how the benefit is sustained.

These examples do not mean that every contribution must receive an identical prize. Different responsibilities can reasonably receive different forms of acknowledgment, and competitive awards may encourage demanding achievements. The important question is whether the criteria make sense in relation to the work. A prize for a presentation can honor communication honestly if it does not pretend to identify the only valuable member of the team. Problems arise when a narrow award becomes a complete account of merit.

There are also contributions whose value does not depend on publicity. A person may prefer to help privately, and some work involves information that should not be shared for the sake of a celebration. Respecting that preference prevents recognition from becoming another obligation imposed on the contributor. Encouragement can be personal, specific, and quiet.

Recognition should therefore remain a way of attending to work, not a replacement for understanding it. The most useful acknowledgment explains what someone did, why it mattered, and how it related to others' efforts. It can motivate participation while leaving room for worthwhile actions that do not fit a stage, a photograph, or a ranked list.

These scenarios are hypothetical illustrations. Accurate personal, literary, or historical evidence can support a different defensible position."""


def essay(kind, unit, skill, prompt, model):
    question = make_essay(kind, unit, skill, prompt, model)
    question['skill_tags'] = [f'ap-skill:{skill}', f'format:{kind}', f'item:lang-d-{kind}']
    return question


QUESTIONS = [
    essay('synthesis', 9, '4.C', SYNTHESIS_PROMPT, SYNTHESIS_MODEL),
    essay('rhetorical-analysis', 2, '3.B', RHETORICAL_PROMPT, RHETORICAL_MODEL),
    essay('argument', 3, '6.C', ARGUMENT_PROMPT, ARGUMENT_MODEL),
]
