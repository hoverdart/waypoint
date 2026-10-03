"""Original concept and experimental-design questions for uncovered Biology topics."""
from scripts.seed_data.questions.authored_mcq import build_questions
from scripts.seed_data.units_topics.biology import UNITS

ITEMS = [
    (
        "Elements of Life",
        "A plant receives adequate water, light, and carbon dioxide but grows slowly in soil lacking nitrogen. Which synthesis is most directly limited by the nitrogen shortage?",
        "Synthesis of amino acids and nucleotides",
        ["Synthesis of water molecules", "Conversion of oxygen gas to carbon dioxide", "Formation of glucose using only carbon, hydrogen, and oxygen"],
        "Amino acids contain an amino group, and nucleotide bases contain nitrogen. A nitrogen shortage therefore limits protein and nucleic acid synthesis. Glucose contains carbon, hydrogen, and oxygen, so nitrogen is not a structural component of glucose itself.",
    ),
    (
        "Cell Compartmentalization",
        "A lysosome maintains an acidic interior while the surrounding cytosol remains near neutral. Which feature most directly allows these different conditions to coexist?",
        "A membrane that separates the lysosomal contents and contains proton pumps",
        ["A cell wall surrounding each lysosome", "Free diffusion of protons throughout the cell", "Ribosomes that prevent water movement"],
        "Compartmentalization separates chemical environments. The lysosomal membrane limits unrestricted proton movement, and membrane proton pumps maintain the concentration difference. Unrestricted diffusion would dissipate that difference; lysosomes do not have cell walls.",
    ),
    (
        "Environmental Effects on Energy Capture and Use",
        "A researcher measures photosynthesis at increasing light intensities while holding carbon dioxide and temperature constant. At high intensity the rate levels off. Which follow-up would best test whether carbon dioxide availability is limiting?",
        "Increase carbon dioxide concentration while holding light intensity and temperature constant",
        ["Increase light intensity and temperature at the same time", "Remove all light while increasing carbon dioxide", "Measure only the plant's height without changing any condition"],
        "Changing carbon dioxide alone tests its effect while controlling alternative explanations. A rise in photosynthetic rate would support carbon dioxide limitation under the original conditions. Changing multiple variables prevents attributing the response specifically to carbon dioxide.",
    ),
    (
        "Cell Communication",
        "A peptide hormone circulates to many tissues, but only some cells respond. What best explains the specificity of the response?",
        "Responsive cells express a receptor that recognizes the hormone",
        ["The hormone enters every cell nucleus directly", "Only responsive cells contain DNA", "The hormone carries a different genetic code in each tissue"],
        "A signal affects a target cell when an appropriate receptor and response pathway are present. Many peptide hormones bind cell-surface receptors because they cannot freely cross the lipid bilayer. Exposure alone does not make every cell a target.",
    ),
    (
        "Feedback",
        "When blood glucose rises, insulin release promotes glucose uptake and storage, reducing blood glucose. This is an example of which regulatory pattern?",
        "Negative feedback because the response reduces the initial change",
        ["Positive feedback because glucose rises before insulin is released", "Positive feedback because insulin is a hormone", "No feedback because glucose can vary over time"],
        "Negative feedback counteracts a deviation from a regulated range. Here, a rise in glucose triggers a response that lowers glucose. Positive feedback would amplify the original change; the presence of a hormone does not determine the feedback type.",
    ),
    (
        "Environmental Effects on Phenotype",
        "Genetically identical plants are grown at two light intensities. Their average leaf sizes differ. Which conclusion is best supported?",
        "Environmental conditions can influence phenotype without a difference in inherited DNA sequence",
        ["Different leaf sizes prove that the plants inherited different alleles", "Light must have changed every gene in each plant", "Phenotype is determined only by genotype"],
        "The controlled genetic background makes environmental influence a plausible explanation for the observed difference. Development and gene expression can respond to light. A phenotypic difference alone does not prove a mutation or a difference in inherited alleles.",
    ),
    (
        "DNA and RNA Structure",
        "A nucleic acid sample contains ribose and uracil. Which statement is most consistent with these observations?",
        "The sample is RNA, which can participate in translating genetic information",
        ["The sample is DNA because uracil pairs with cytosine", "The sample is a protein because ribose forms peptide bonds", "The sample is DNA because DNA contains ribose rather than deoxyribose"],
        "RNA contains ribose and typically uses uracil instead of thymine. Messenger, transfer, and ribosomal RNAs participate in translation. DNA contains deoxyribose, and peptide bonds join amino acids rather than nucleotides.",
    ),
    (
        "DNA Replication",
        "Cells grown for many generations in heavy nitrogen are transferred to light nitrogen. After one complete round of DNA replication, what DNA molecules are expected under the semiconservative model?",
        "Each molecule has one parental heavy strand and one new light strand",
        ["Half the molecules contain two heavy strands and half contain two light strands", "Every molecule contains two entirely light strands", "Each strand has alternating intact heavy and light nucleotides by necessity"],
        "Semiconservative replication preserves one original strand in each daughter molecule. New strands incorporate light nitrogen after the transfer. The prediction of separate all-heavy and all-light molecules corresponds to conservative replication, not semiconservative replication.",
    ),
    (
        "Translation",
        "An mRNA codon is 5′-AUG-3′. Which anticodon orientation would pair with it during translation?",
        "3′-UAC-5′", ["3′-AUG-5′", "3′-TAC-5′", "5′-UAC-3′"],
        "Codon and anticodon align antiparallel and use complementary RNA bases: A pairs with U and G with C. Thus 5′-AUG-3′ pairs with 3′-UAC-5′. RNA uses uracil rather than thymine, and reversing the stated direction changes the sequence being represented.",
    ),
    (
        "Common Ancestry",
        "The forelimbs of whales, bats, and humans share an underlying arrangement of bones despite different functions. What is the strongest evolutionary interpretation of this pattern?",
        "The structures were inherited from a common ancestor and modified in different lineages",
        ["All three species independently developed identical DNA sequences because they needed limbs", "The species must occupy the same ecological niche", "Similar bone arrangement proves the species can interbreed"],
        "Homologous structures reflect shared ancestry even when their present functions differ. Natural selection can modify an inherited structure in separate lineages. Similarity in a body plan does not require identical DNA, identical niches, or reproductive compatibility.",
    ),
    (
        "Continuing Evolution",
        "Before antibiotic exposure, a bacterial population contains rare resistant variants. After exposure, resistant bacteria become common. Which explanation best fits natural selection?",
        "Resistant variants survive and reproduce more successfully during treatment",
        ["Each bacterium intentionally mutates in response to its need for resistance", "The antibiotic creates only helpful mutations", "Individual susceptible bacteria evolve resistance by trying repeatedly"],
        "Selection changes the frequency of inherited variants in a population. Preexisting resistant bacteria leave more descendants under antibiotic exposure. Mutations do not arise because an organism needs a particular outcome, and individuals do not evolve through effort.",
    ),
    (
        "Responses to the Environment",
        "Seedlings bend toward a light source. Which observation most directly supports the explanation that unequal growth causes bending?",
        "Cells on the shaded side elongate more than cells on the illuminated side",
        ["Both sides stop growing at the same moment", "The illuminated side loses all its cells", "The stem moves without any difference in cell length"],
        "Differential cell elongation bends a growing shoot. Greater elongation on the shaded side curves the shoot toward the light. Equal growth on both sides would lengthen a straight stem rather than produce the observed directional curvature.",
    ),
    (
        "Biodiversity",
        "Two grasslands have the same total number of plants. One contains a single species; the other contains several species with different drought tolerances. Which prediction is most reasonable during an unusually dry year?",
        "The diverse grassland may maintain more function because some species tolerate drought better",
        ["Both grasslands must respond identically because plant abundance is equal", "The diverse grassland cannot lose any species", "The single-species grassland is guaranteed to have higher productivity"],
        "Functional differences among species can buffer ecosystem responses to disturbance. Drought-tolerant species may maintain some production when other species decline. Diversity does not guarantee that no species will be lost or that every diverse system is always more productive.",
    ),
]
QUESTIONS = build_questions(UNITS, ITEMS)
