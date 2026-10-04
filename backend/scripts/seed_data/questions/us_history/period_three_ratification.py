"""Original questions about confederation and ratification using public-domain texts."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='Government Under the Articles of Confederation', code='3.7',
    source_url='https://www.archives.gov/milestone-documents/articles-of-confederation', source_kind='primary excerpt',
    stimulus='Articles of Confederation, Article VIII, adopted 1777, effective 1781: “The taxes for paying that proportion shall be laid and levied by the authority and direction of the legislatures of the several states”',
    items=[
        ('claims-evidence', 2, 'Under this provision, which institution levied the taxes used to meet a state’s share of common expenses?', 1, [
            ('A separately elected national executive.', 'The Articles did not establish a separately elected national executive with taxing authority.'),
            ('The legislature of that state.', 'Article VIII explicitly assigned the levying of these taxes to state legislatures.'),
            ('A permanent federal supreme court.', 'This clause assigns taxation to state legislatures, not a federal supreme court.'),
            ('The British Parliament.', 'The Articles organized government for the independent United States, not taxation by Parliament.'),
        ]),
        ('causation', 3, 'Which difficulty could most directly result from the arrangement described?', 3, [
            ('States would lose all control over revenue collection.', 'The provision preserves state legislative control over levying these taxes.'),
            ('Congress would be required to pay every expense with British currency.', 'The provision says nothing requiring British currency.'),
            ('All state debts would automatically become private debts.', 'The allocation of taxation authority does not convert state debts into private obligations.'),
            ('Congress could struggle to fund common expenses when states failed to supply requested revenue.', 'Reliance on state legislatures left national finances vulnerable to inadequate state contributions.'),
        ]),
        ('comparison', 3, 'Which later constitutional provision most directly addressed the institutional limitation illustrated here?', 0, [
            ('Granting Congress authority to lay and collect taxes.', 'A federal power to collect taxes reduced dependence on state legislatures for national revenue.'),
            ('Guaranteeing each state two senators.', 'Equal Senate representation concerns legislative representation rather than collecting revenue.'),
            ('Requiring a minimum age for the presidency.', 'Presidential eligibility does not change how national revenue is collected.'),
            ('Prohibiting religious tests for federal office.', 'The prohibition concerns eligibility for office, not national taxing authority.'),
        ]),
        ('contextualization', 4, 'Which interpretation best situates the provision within revolutionary political concerns?', 2, [
            ('It sought to reestablish Parliament’s authority over colonial taxation.', 'The states had declared independence and were creating their own confederation.'),
            ('It made taxation independent of representative legislatures.', 'Taxation remained under representative state legislatures.'),
            ('It reflected reluctance to concentrate fiscal authority in a distant central government.', 'Experiences of disputed imperial taxation helped make local and state control politically attractive.'),
            ('It implemented the later Federalist program for a powerful national treasury.', 'The arrangement preceded and differed from the later effort to strengthen national fiscal authority.'),
        ]),
    ],
)

QUESTIONS += source_set(
    period='Period 3: 1754-1800', topic='Constitutional Convention and Ratification', code='3.8',
    source_url='https://www.archives.gov/founding-docs/bill-of-rights-transcript', source_kind='primary excerpt',
    stimulus='Congressional resolution proposing constitutional amendments, September 25, 1789, preamble: “in order to prevent misconstruction or abuse of its powers, that further declaratory and restrictive clauses should be added”',
    items=[
        ('sourcing', 2, 'The stated purpose of adding these clauses was primarily to', 0, [
            ('reduce fears that governmental powers would be misinterpreted or abused.', 'The preamble explicitly identifies misconstruction and abuse of power as concerns.'),
            ('restore the Articles of Confederation unchanged.', 'The resolution proposed amendments to the Constitution rather than restoration of the Articles.'),
            ('abolish the new federal government.', 'Restricting powers through amendments assumes the continued existence of the government.'),
            ('grant Congress unlimited authority over individual liberties.', 'Restrictive clauses limit power rather than make it unlimited.'),
        ]),
        ('contextualization', 3, 'Which ratification-era concern most directly helps explain this proposal?', 2, [
            ('A demand that senators be directly elected under the Seventeenth Amendment.', 'The Seventeenth Amendment dates to 1913 and is not the immediate context for this proposal.'),
            ('A dispute over readmitting former Confederate states.', 'Reconstruction followed the Civil War, long after 1789.'),
            ('Opposition to the Constitution’s lack of explicit protections against federal infringements of liberties.', 'Calls for a bill of rights were central to concerns raised during ratification.'),
            ('A demand to end the Electoral College after the election of 1824.', 'The 1824 election occurred after this resolution and cannot explain its adoption.'),
        ]),
        ('argumentation', 4, 'Which argument about ratification is most strongly supported by the resolution’s proposal?', 1, [
            ('All opponents of the Constitution accepted every feature of the new government.', 'A proposal addressing objections does not prove unanimous acceptance of the Constitution.'),
            ('Criticism of the Constitution helped shape changes to the new governmental framework.', 'The proposed restrictions responded to concerns about federal power and show criticism influencing constitutional development.'),
            ('Ratification ended debate over the limits of federal authority permanently.', 'A response to earlier concerns does not establish that later debate ended.'),
            ('The Constitution could be altered only by violent revolution.', 'The resolution used the constitutional amendment process rather than revolutionary overthrow.'),
        ]),
        ('claims-evidence', 3, 'Which conclusion would require evidence beyond this preamble?', 3, [
            ('The authors identified possible abuse of governmental powers as a concern.', 'The preamble states this concern explicitly.'),
            ('The authors favored adding restrictions to the constitutional text.', 'The proposal explicitly calls for additional restrictive clauses.'),
            ('The authors viewed clarification of power as a reason for amendment.', 'Preventing misconstruction indicates a desire to clarify how powers should be understood.'),
            ('The proposed protections were consistently enforced for every person after ratification.', 'A statement of legislative purpose cannot establish universal enforcement or equal access to rights in practice.'),
        ]),
    ],
)
