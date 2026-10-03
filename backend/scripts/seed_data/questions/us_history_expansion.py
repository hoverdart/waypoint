"""Original U.S. history reasoning questions; no reproduced exam passages."""
from scripts.seed_data.questions.authored_mcq import build_questions
from scripts.seed_data.units_topics.us_history import UNITS

ITEMS = [
    (
        "European Exploration in the Americas",
        "Which combination of developments most directly supported the expansion of European transatlantic exploration in the late fifteenth century?",
        "Improved navigation and ship technology combined with state interest in trade routes",
        ["The disappearance of competition among European states and the end of overseas trade", "Industrial steam engines combined with mass-produced railroads", "The end of religious competition and the abolition of monarchies"],
        "Navigation and sailing developments helped make ocean voyages feasible, while monarchs and merchants sought trade, wealth, and strategic advantage. Steam engines and railroads belong to a much later period. Exploration occurred amid continuing political and religious competition.",
    ),
    (
        "Europe and the Colonies: Political and Economic Rivalries",
        "British Navigation Acts required many colonial goods to travel on English ships and pass through English ports. These policies most clearly reflected which economic goal?",
        "Directing colonial commerce to benefit the mother country",
        ["Giving colonies unrestricted free trade with all foreign powers", "Eliminating imperial regulation of colonial trade", "Replacing all Atlantic commerce with local barter"],
        "The Navigation Acts were part of mercantilist efforts to channel colonial production and commerce toward imperial interests. They restricted rather than guaranteed free trade. Their enforcement and evasion contributed to tensions within the British Atlantic system.",
    ),
    (
        "The Seven Years' War (French and Indian War)",
        "How did Britain's victory in the Seven Years' War contribute to conflict with its North American colonists?",
        "War debt and new territorial responsibilities encouraged Britain to raise colonial revenue and tighten imperial control",
        ["Britain surrendered all its mainland colonies to France", "The war eliminated Britain's need for taxes or an army", "Colonial representatives gained voting seats in Parliament immediately after the war"],
        "Victory enlarged Britain's North American responsibilities while leaving a heavy debt. Revenue measures and efforts to regulate westward settlement challenged colonists accustomed to considerable autonomy. These postwar policies helped set the stage for resistance in the 1760s and 1770s.",
    ),
    (
        "Washington, Hamilton, and the New Government",
        "Debates over Alexander Hamilton's proposed national bank most directly exposed which constitutional disagreement?",
        "Whether the federal government could use implied powers to carry out enumerated responsibilities",
        ["Whether the Constitution explicitly required the abolition of all state governments", "Whether the president could appoint hereditary successors", "Whether every state was prohibited from collecting taxes"],
        "Hamilton defended the bank using a broad understanding of implied powers and the Necessary and Proper Clause. Opponents such as Jefferson favored a narrower reading of federal authority. The dispute concerned the scope of constitutional power, not hereditary rule or the elimination of states.",
    ),
    (
        "Markets and Westward Expansion",
        "Which effect of canals and improved roads in the early nineteenth century best illustrates the market revolution?",
        "Farmers could ship surplus crops to distant markets at lower cost",
        ["Rural households became entirely isolated from cities", "Commercial agriculture disappeared throughout the West", "Transportation improvements ended regional economic specialization"],
        "Lower transportation costs linked producers and consumers across longer distances, encouraged commercial agriculture, and supported regional specialization. These connections strengthened market exchange rather than eliminating it or isolating rural communities.",
    ),
    (
        "The Compromise of 1850 and Escalating Sectional Conflict",
        "Why did the Fugitive Slave Act of 1850 intensify conflict over slavery in many northern communities?",
        "It expanded federal enforcement of slaveholders' claims and compelled participation in returning alleged fugitives",
        ["It immediately abolished slavery in every border state", "It guaranteed jury trials to every person accused of escaping slavery", "It prohibited federal officers from assisting slaveholders"],
        "The act strengthened federal enforcement and denied important procedural protections to alleged fugitives, making slavery's enforcement a direct issue in free states. Resistance and personal liberty measures deepened sectional conflict. It neither abolished slavery nor guaranteed jury trials to the accused.",
    ),
    (
        "The Western Frontier and Native American Displacement",
        "The Dawes Act of 1887 divided many Native American reservation lands into individual allotments. Which outcome was most consistent with its implementation?",
        "The erosion of communal landholding and substantial transfer of Native land to non-Native owners",
        ["The restoration of all previously lost tribal territory", "A federal guarantee that Native communal ownership would remain unchanged", "The end of federal efforts to assimilate Native peoples"],
        "Allotment aimed to promote assimilation through individual land ownership and opened lands deemed surplus to non-Native settlement. The policy reduced tribal land bases and undermined communal institutions. It was not a program of territorial restoration or protection of unchanged communal ownership.",
    ),
    (
        "American Imperialism and World War I",
        "Senate opposition to U.S. membership in the League of Nations after World War I most often centered on which concern?",
        "Collective-security commitments could limit U.S. freedom to decide when to enter conflicts",
        ["The League required the United States to restore British colonial rule over its states", "The League had already abolished the U.S. Constitution", "The treaty prohibited every form of international trade"],
        "Many opponents and reservationists worried that League obligations, especially collective security, could draw the United States into conflicts or constrain congressional authority. Disagreement also involved domestic politics and Wilson's handling of the treaty. The League did not abolish the Constitution or all trade.",
    ),
    (
        "Postwar Prosperity and Suburbanization",
        "Which statement best describes the relationship between federal housing policy and suburban growth after World War II?",
        "Mortgage support encouraged homeownership, but discriminatory practices restricted equal access to its benefits",
        ["Federal policy played no role in expanding homeownership", "All racial groups received identical access to mortgages and suburban housing", "Suburban growth occurred only because all urban employment disappeared"],
        "Federal mortgage guarantees and related policies helped many families buy homes, while redlining and racial discrimination excluded many Black families and other groups. Postwar suburban growth therefore combined broader access for some with continuing structural inequality.",
    ),
    (
        "Demographic and Cultural Change Since 1980",
        "Which development most directly contributed to the growing demographic diversity of the United States in the late twentieth century?",
        "Continued immigration from Latin America and Asia following changes to immigration law in 1965",
        ["A permanent end to all immigration after 1980", "The restoration of the original national-origins quota system in every decade", "The disappearance of international economic and family networks"],
        "The 1965 immigration reforms removed the earlier national-origins quota framework. Subsequent migration shaped by family ties, employment, and other forces increased the population's diversity, including immigration from Latin America and Asia. Immigration did not cease after 1980.",
    ),
]
QUESTIONS = build_questions(UNITS, ITEMS)
