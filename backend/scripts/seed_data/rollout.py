"""Course rollout order, based on exam counts (not course enrollment).

Source: College Board 2025 Program Summary Report. New courses with no reported
2025 participation follow the ranked courses; absence is not a zero count.
"""

PARTICIPATION_YEAR = 2025
PARTICIPATION_SOURCE = "https://apcentral.collegeboard.org/media/pdf/program-summary-report-2025.pdf"
CATALOG_SOURCE = "https://apcentral.collegeboard.org/courses"
VERIFIED_ON = "2026-10-03"

# code, official course name, number of exams in the 2025 administration
COURSE_ROLLOUT = [
    ("english-language", "AP English Language and Composition", 616294),
    ("us-history", "AP United States History", 516738),
    ("english-literature", "AP English Literature and Composition", 416531),
    ("world-history", "AP World History: Modern", 411547),
    ("us-government", "AP United States Government and Politics", 387973),
    ("psychology", "AP Psychology", 334038),
    ("biology", "AP Biology", 287232),
    ("calculus-ab", "AP Calculus AB", 285891),
    ("human-geography", "AP Human Geography", 282781),
    ("statistics", "AP Statistics", 266791),
    ("precalculus", "AP Precalculus", 253596),
    ("environmental-science", "AP Environmental Science", 245371),
    ("spanish-language", "AP Spanish Language and Culture", 182670),
    ("macroeconomics", "AP Macroeconomics", 176356),
    ("computer-science-principles", "AP Computer Science Principles", 175174),
    ("physics-1", "AP Physics 1: Algebra-Based", 174401),
    ("chemistry", "AP Chemistry", 168833),
    ("calculus-bc", "AP Calculus BC", 160436),
    ("seminar", "AP Seminar", 126001),
    ("microeconomics", "AP Microeconomics", 117548),
    ("computer-science-a", "AP Computer Science A", 93217),
    ("european-history", "AP European History", 86729),
    ("physics-c-mechanics", "AP Physics C: Mechanics", 65980),
    ("art-design-2d", "AP 2-D Art and Design", 48279),
    ("research", "AP Research", 43214),
    ("physics-c-electricity-magnetism", "AP Physics C: Electricity and Magnetism", 29708),
    ("spanish-literature", "AP Spanish Literature and Culture", 27266),
    ("comparative-government", "AP Comparative Government and Politics", 27150),
    ("art-history", "AP Art History", 25584),
    ("physics-2", "AP Physics 2: Algebra-Based", 24211),
    ("drawing", "AP Drawing", 23107),
    ("african-american-studies", "AP African American Studies", 21435),
    ("french-language", "AP French Language and Culture", 19639),
    ("chinese-language", "AP Chinese Language and Culture", 18312),
    ("music-theory", "AP Music Theory", 17799),
    ("art-design-3d", "AP 3-D Art and Design", 10304),
    ("latin", "AP Latin", 4336),
    ("german-language", "AP German Language and Culture", 4213),
    ("japanese-language", "AP Japanese Language and Culture", 3245),
    ("italian-language", "AP Italian Language and Culture", 2241),
    ("business-personal-finance", "AP Business with Personal Finance", None),
    ("cybersecurity", "AP Cybersecurity", None),
    ("networking", "AP Networking", None),
]

PRIORITY = {code: index for index, (code, _, _) in enumerate(COURSE_ROLLOUT, start=1)}
