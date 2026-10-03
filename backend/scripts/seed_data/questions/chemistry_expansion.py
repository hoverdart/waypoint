"""Original questions with numerical and particle-level chemical reasoning."""
from scripts.seed_data.questions.authored_mcq import build_questions
from scripts.seed_data.units_topics.chemistry import UNITS

ITEMS = [
    (
        "Mass Spectroscopy of Elements",
        "A hypothetical element has two isotopes with masses 10.0 u and 11.0 u. Their abundances are 20.0% and 80.0%, respectively. What is its average atomic mass?",
        "10.8 u", ["10.2 u", "10.5 u", "21.0 u"],
        "Average atomic mass is the abundance-weighted mean: (0.200)(10.0) + (0.800)(11.0) = 10.8 u. The simple midpoint 10.5 u would be correct only for equal abundances; adding the two masses does not give an average.",
    ),
    (
        "Ionic and Metallic Bonding",
        "Why can a solid copper wire conduct electric current while solid sodium chloride does not?",
        "Copper contains mobile delocalized electrons, while the ions in solid sodium chloride are fixed in a lattice",
        ["Copper atoms carry a net negative charge, while sodium chloride contains no charged particles", "Copper has moving protons, while sodium chloride has stationary electrons only", "All covalent compounds conduct, but all ionic compounds never conduct"],
        "Metallic bonding allows delocalized electrons to move through the solid. Solid sodium chloride contains charged ions, but those ions cannot travel through its rigid lattice. Sodium chloride can conduct when molten or dissolved because its ions then become mobile.",
    ),
    (
        "Structure of Ionic Solids and Metals",
        "When a sodium chloride crystal is struck, layers shift and the crystal can fracture. Which particle-level explanation best accounts for this brittleness?",
        "The shift can bring like-charged ions next to one another, creating repulsion",
        ["The shift converts all ionic bonds into hydrogen bonds", "The crystal's ions become uncharged atoms before fracturing", "Free electrons flow out and leave every ion positively charged"],
        "An ionic lattice alternates oppositely charged ions. Displacing a layer can align ions with the same charge, producing strong repulsive forces that split the crystal. Metallic bonding is less directional and permits layers to move while delocalized electrons maintain attraction.",
    ),
    (
        "Properties of Solids and Liquids",
        "Water and methane have similar molecular sizes but very different normal boiling points. Which interaction most directly explains water's much higher boiling point?",
        "Hydrogen bonding between water molecules",
        ["Covalent O–H bonds breaking during normal boiling", "Ionic bonds between neutral water molecules", "Methane having no intermolecular attractions at all"],
        "Water molecules form strong hydrogen-bonding interactions because H is bonded to highly electronegative O. Boiling separates molecules and overcomes intermolecular attractions; it does not normally break the covalent O–H bonds. Methane still experiences London dispersion forces.",
    ),
    (
        "Solutions and Mixtures",
        "A student dilutes 25.0 mL of 0.400 M NaCl solution to a final volume of 100.0 mL. What is the final NaCl concentration?",
        "0.100 M", ["0.0250 M", "0.400 M", "1.60 M"],
        "Dilution conserves moles of solute: M₁V₁ = M₂V₂. Therefore M₂ = (0.400)(25.0)/100.0 = 0.100 M. The final volume is 100.0 mL, not the amount of water added, and dilution lowers rather than raises concentration.",
    ),
    (
        "Concentration Changes Over Time",
        "A first-order reactant has a half-life of 10 minutes. If its initial concentration is 0.80 M, what concentration remains after 30 minutes?",
        "0.10 M", ["0.20 M", "0.40 M", "0.00 M"],
        "Thirty minutes is three half-lives, so [A] = 0.80(1/2)³ = 0.10 M. In a first-order process each half-life removes half of what remains, rather than subtracting the same absolute concentration each time.",
    ),
    (
        "Reaction Mechanisms and Elementary Reactions",
        "A proposed mechanism begins with the slow elementary step A + B → I, followed by the fast step I + B → P. If the first step controls the observed rate, which rate law is predicted?",
        "Rate = k[A][B]", ["Rate = k[A][B]²", "Rate = k[I][B]", "Rate = k[P]"],
        "For the stated rate-limiting elementary step, the rate depends on one molecule each of A and B, giving k[A][B]. The overall reaction A + 2B → P does not by itself determine the rate law; overall stoichiometric coefficients are not generally reaction orders.",
    ),
    (
        "Introduction to Equilibrium",
        "In a sealed container, a reversible reaction reaches dynamic equilibrium. Which statement is necessarily true?",
        "The forward and reverse reaction rates are equal",
        ["The reactant and product concentrations are equal", "Both reactions stop completely", "Every reactant has been converted to product"],
        "At dynamic equilibrium both directions continue at equal rates, so concentrations stay constant over time. Those concentrations need not be equal. A closed system can contain substantial quantities of both reactants and products at equilibrium.",
    ),
    (
        "Bronsted-Lowry Acids and Bases",
        "In NH₃ + H₂O ⇌ NH₄⁺ + OH⁻, which pair is a conjugate acid–base pair?",
        "NH₄⁺ and NH₃", ["NH₃ and OH⁻", "NH₄⁺ and OH⁻", "H₂O and NH₃"],
        "Conjugate partners differ by one proton. NH₃ accepts a proton to become NH₄⁺, so NH₄⁺ is its conjugate acid. H₂O and OH⁻ form the other conjugate pair. A pair does not qualify merely because one species is an acid and the other a base.",
    ),
    (
        "Weak Acid/Base Equilibria (Ka and Kb)",
        "At 25°C, a weak acid HA has Ka = 1.0 × 10⁻⁵. What is Kb for its conjugate base A⁻? Use Kw = 1.0 × 10⁻¹⁴.",
        "1.0 × 10⁻⁹", ["1.0 × 10⁻⁵", "1.0 × 10⁹", "1.0 × 10⁻¹⁹"],
        "For a conjugate acid–base pair at the same temperature, KaKb = Kw. Thus Kb = (1.0 × 10⁻¹⁴)/(1.0 × 10⁻⁵) = 1.0 × 10⁻⁹. Multiplying instead of dividing would incorrectly give 10⁻¹⁹.",
    ),
    (
        "Free Energy and Equilibrium",
        "At a fixed temperature, a reaction has an equilibrium constant K much greater than 1. What can be concluded about its standard Gibbs free-energy change ΔG°?",
        "ΔG° is negative", ["ΔG° is positive", "ΔG° must be zero", "The sign of ΔG° depends only on reaction speed"],
        "The relationship ΔG° = −RT ln K connects thermodynamics to equilibrium. When K > 1, ln K is positive and ΔG° is negative. This describes standard-state thermodynamics, not the instantaneous ΔG of any mixture or the reaction's kinetic speed.",
    ),
]
QUESTIONS = build_questions(UNITS, ITEMS)
