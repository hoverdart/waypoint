"""AP Chemistry units and topics, aligned to the College Board CED.

Unit names and exam weighting ranges match the official Course and Exam
Description's 9 units. Topic names follow the CED's topic list where known.
"""

UNITS = [
    {
        "name": "Atomic Structure and Properties",
        "description": "Covers atomic theory, mass spectrometry, electron configurations, periodic trends, and the forces that hold atoms and ions together.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 1,
        "topics": [
            {
                "name": "Moles and Molar Mass",
                "description": "Uses molar mass and Avogadro's number to convert between mass, moles, and number of particles.",
                "skill_tags": ["stoichiometry", "moles"],
                "display_order": 1,
            },
            {
                "name": "Mass Spectroscopy of Elements",
                "description": "Interprets mass spectra to determine isotopic composition and average atomic mass.",
                "skill_tags": ["atomic-structure", "isotopes"],
                "display_order": 2,
            },
            {
                "name": "Electron Configuration and Orbitals",
                "description": "Describes the arrangement of electrons in atoms using orbital notation, electron configuration, and quantum numbers.",
                "skill_tags": ["electron-configuration"],
                "display_order": 3,
            },
            {
                "name": "Periodic Trends",
                "description": "Explains trends in atomic radius, ionization energy, and electronegativity across periods and down groups.",
                "skill_tags": ["periodic-trends"],
                "display_order": 4,
            },
            {
                "name": "Ionic and Metallic Bonding",
                "description": "Relates the formation of ionic and metallic bonds to coulombic attraction and periodic properties.",
                "skill_tags": ["bonding", "ionic-bonding"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Molecular and Ionic Compound Structure and Properties",
        "description": "Explores covalent bonding, Lewis structures, molecular geometry, and how structure determines the physical properties of compounds.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 2,
        "topics": [
            {
                "name": "Lewis Diagrams",
                "description": "Constructs Lewis structures, including resonance forms and formal charge, for molecules and polyatomic ions.",
                "skill_tags": ["lewis-structures"],
                "display_order": 1,
            },
            {
                "name": "VSEPR and Bond Hybridization",
                "description": "Predicts molecular geometry and hybridization using valence shell electron pair repulsion theory.",
                "skill_tags": ["molecular-geometry", "vsepr"],
                "display_order": 2,
            },
            {
                "name": "Bond Polarity and Molecular Polarity",
                "description": "Determines bond and molecular polarity from electronegativity differences and geometry.",
                "skill_tags": ["polarity"],
                "display_order": 3,
            },
            {
                "name": "Structure of Ionic Solids and Metals",
                "description": "Describes the properties of ionic solids and metallic structures in terms of lattice arrangement and bonding.",
                "skill_tags": ["ionic-solids"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Intermolecular Forces and Properties",
        "description": "Examines intermolecular forces, states of matter, solutions, and how these forces explain macroscopic physical properties.",
        "ap_weight_min": 18.0,
        "ap_weight_max": 22.0,
        "display_order": 3,
        "topics": [
            {
                "name": "Intermolecular Forces",
                "description": "Distinguishes London dispersion, dipole-dipole, and hydrogen bonding forces and relates them to boiling and melting points.",
                "skill_tags": ["intermolecular-forces"],
                "display_order": 1,
            },
            {
                "name": "Properties of Solids and Liquids",
                "description": "Relates structure and intermolecular forces to properties such as viscosity, surface tension, and vapor pressure.",
                "skill_tags": ["states-of-matter"],
                "display_order": 2,
            },
            {
                "name": "Ideal Gas Law",
                "description": "Applies the ideal gas law and kinetic molecular theory to relate pressure, volume, temperature, and moles of gas.",
                "skill_tags": ["gas-laws", "ideal-gas-law"],
                "display_order": 3,
            },
            {
                "name": "Solutions and Mixtures",
                "description": "Describes solution formation, concentration units, and factors affecting solubility.",
                "skill_tags": ["solutions", "solubility"],
                "display_order": 4,
            },
            {
                "name": "Colligative Properties",
                "description": "Calculates boiling point elevation, freezing point depression, and osmotic pressure from solute concentration.",
                "skill_tags": ["colligative-properties"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Chemical Reactions",
        "description": "Introduces representations of chemical reactions, including net ionic equations, stoichiometry, and physical/chemical changes.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 4,
        "topics": [
            {
                "name": "Introduction to Reactions",
                "description": "Classifies physical and chemical changes and represents reactions with balanced chemical equations.",
                "skill_tags": ["chemical-reactions"],
                "display_order": 1,
            },
            {
                "name": "Net Ionic Equations",
                "description": "Writes net ionic equations for precipitation, acid-base, and other reactions in aqueous solution.",
                "skill_tags": ["net-ionic-equations"],
                "display_order": 2,
            },
            {
                "name": "Stoichiometry and Limiting Reagents",
                "description": "Uses mole ratios from balanced equations to calculate reactant and product quantities, including limiting reagent problems.",
                "skill_tags": ["stoichiometry", "limiting-reagent"],
                "display_order": 3,
            },
        ],
    },
    {
        "name": "Kinetics",
        "description": "Covers reaction rates, rate laws, reaction mechanisms, and the effect of catalysts on reaction rate.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 5,
        "topics": [
            {
                "name": "Rate Law and Reaction Order",
                "description": "Determines rate laws and reaction order from experimental concentration-versus-time data.",
                "skill_tags": ["kinetics", "rate-law"],
                "display_order": 1,
            },
            {
                "name": "Concentration Changes Over Time",
                "description": "Uses integrated rate laws to relate concentration, time, and half-life for zero-, first-, and second-order reactions.",
                "skill_tags": ["kinetics", "integrated-rate-law"],
                "display_order": 2,
            },
            {
                "name": "Reaction Mechanisms and Elementary Reactions",
                "description": "Proposes reaction mechanisms consistent with an experimentally determined rate law, identifying the rate-determining step.",
                "skill_tags": ["reaction-mechanisms"],
                "display_order": 3,
            },
            {
                "name": "Effect of Temperature and Catalysts on Rate",
                "description": "Explains how temperature and catalysts affect reaction rate using collision theory and the Arrhenius equation.",
                "skill_tags": ["catalysts", "arrhenius-equation"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Thermodynamics",
        "description": "Explores energy changes in chemical and physical processes, including enthalpy, Hess's law, and calorimetry.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 6,
        "topics": [
            {
                "name": "Endothermic and Exothermic Processes",
                "description": "Distinguishes endothermic and exothermic processes using energy diagrams and enthalpy sign conventions.",
                "skill_tags": ["thermochemistry", "enthalpy"],
                "display_order": 1,
            },
            {
                "name": "Calorimetry",
                "description": "Calculates heat transfer and specific heat capacity using calorimetry data.",
                "skill_tags": ["calorimetry"],
                "display_order": 2,
            },
            {
                "name": "Hess's Law and Bond Energies",
                "description": "Calculates reaction enthalpy using Hess's law, formation enthalpies, and average bond energies.",
                "skill_tags": ["hess-law", "bond-energy"],
                "display_order": 3,
            },
        ],
    },
    {
        "name": "Equilibrium",
        "description": "Covers the equilibrium state, the equilibrium constant, Le Chatelier's principle, and solubility equilibria.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 7,
        "topics": [
            {
                "name": "Introduction to Equilibrium",
                "description": "Describes the dynamic nature of chemical equilibrium and writes equilibrium constant expressions.",
                "skill_tags": ["equilibrium"],
                "display_order": 1,
            },
            {
                "name": "Calculating the Equilibrium Constant",
                "description": "Calculates Kc and Kp from equilibrium concentrations or pressures using ICE tables.",
                "skill_tags": ["equilibrium-constant", "ice-table"],
                "display_order": 2,
            },
            {
                "name": "Le Chatelier's Principle",
                "description": "Predicts the direction of equilibrium shift in response to changes in concentration, volume, pressure, or temperature.",
                "skill_tags": ["le-chateliers-principle"],
                "display_order": 3,
            },
            {
                "name": "Solubility Equilibria (Ksp)",
                "description": "Uses the solubility product constant to calculate molar solubility and predict precipitate formation.",
                "skill_tags": ["ksp", "solubility-equilibria"],
                "display_order": 4,
            },
        ],
    },
    {
        "name": "Acids and Bases",
        "description": "Covers Bronsted-Lowry acid-base theory, pH calculations, buffers, and acid-base titrations.",
        "ap_weight_min": 11.0,
        "ap_weight_max": 15.0,
        "display_order": 8,
        "topics": [
            {
                "name": "Bronsted-Lowry Acids and Bases",
                "description": "Identifies conjugate acid-base pairs and predicts the direction of proton transfer reactions.",
                "skill_tags": ["acids-and-bases"],
                "display_order": 1,
            },
            {
                "name": "pH and pOH Calculations",
                "description": "Calculates pH, pOH, [H+], and [OH-] for strong and weak acid and base solutions.",
                "skill_tags": ["ph-calculations"],
                "display_order": 2,
            },
            {
                "name": "Weak Acid/Base Equilibria (Ka and Kb)",
                "description": "Uses Ka and Kb expressions and ICE tables to calculate the pH of weak acid and weak base solutions.",
                "skill_tags": ["ka-kb", "weak-acid-equilibria"],
                "display_order": 3,
            },
            {
                "name": "Buffers",
                "description": "Explains buffer action and uses the Henderson-Hasselbalch equation to calculate buffer pH.",
                "skill_tags": ["buffers", "henderson-hasselbalch"],
                "display_order": 4,
            },
            {
                "name": "Acid-Base Titrations",
                "description": "Interprets titration curves and calculates concentrations using titration data and equivalence points.",
                "skill_tags": ["titrations"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Applications of Thermodynamics",
        "description": "Extends thermodynamics to entropy, Gibbs free energy, electrochemistry, and galvanic/electrolytic cells.",
        "ap_weight_min": 7.0,
        "ap_weight_max": 9.0,
        "display_order": 9,
        "topics": [
            {
                "name": "Entropy and Gibbs Free Energy",
                "description": "Predicts reaction spontaneity using entropy, enthalpy, and the Gibbs free energy equation.",
                "skill_tags": ["entropy", "gibbs-free-energy"],
                "display_order": 1,
            },
            {
                "name": "Free Energy and Equilibrium",
                "description": "Relates the sign and magnitude of Gibbs free energy to the equilibrium constant and reaction favorability.",
                "skill_tags": ["gibbs-free-energy", "equilibrium"],
                "display_order": 2,
            },
            {
                "name": "Galvanic and Electrolytic Cells",
                "description": "Analyzes galvanic and electrolytic cells, calculating standard cell potentials from half-reactions.",
                "skill_tags": ["electrochemistry", "galvanic-cells"],
                "display_order": 3,
            },
        ],
    },
]
