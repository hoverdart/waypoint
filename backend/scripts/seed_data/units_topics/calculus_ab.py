"""AP Calculus AB units and topics, aligned to the College Board CED (2020-21 revision).

Unit names and exam weighting ranges match the official Course and Exam
Description. Topic names/numbering follow the CED's topic list where known
(e.g. 1.1, 2.1, etc. correspond to CED sub-topic numbering within each unit).
"""

UNITS = [
    {
        "name": "Limits and Continuity",
        "description": "Introduces the limit as the foundational concept of calculus, including limit laws, asymptotic and unbounded behavior, and continuity.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 12.0,
        "display_order": 1,
        "topics": [
            {
                "name": "Defining Limits and Using Limit Notation",
                "description": "Introduces the intuitive definition of a limit and how to express it using proper notation.",
                "skill_tags": ["limits", "notation"],
                "display_order": 1,
            },
            {
                "name": "Estimating Limits from Graphs and Tables",
                "description": "Uses graphical and numerical evidence to estimate the value of a limit.",
                "skill_tags": ["limits", "graphical-analysis"],
                "display_order": 2,
            },
            {
                "name": "Determining Limits Using Algebraic Properties",
                "description": "Applies limit laws, direct substitution, factoring, and rationalization to evaluate limits.",
                "skill_tags": ["limits", "algebraic-manipulation"],
                "display_order": 3,
            },
            {
                "name": "Selecting Procedures for Determining Limits",
                "description": "Chooses appropriate strategies, including squeeze theorem, for more complex limit problems.",
                "skill_tags": ["limits", "problem-solving"],
                "display_order": 4,
            },
            {
                "name": "Determining Limits Using the Squeeze Theorem",
                "description": "Uses the squeeze (sandwich) theorem to evaluate limits of bounded oscillating functions.",
                "skill_tags": ["limits", "squeeze-theorem"],
                "display_order": 5,
            },
            {
                "name": "Connecting Limits, Asymptotes, and Continuity",
                "description": "Relates infinite limits and limits at infinity to vertical and horizontal asymptotes, and defines continuity at a point and on an interval.",
                "skill_tags": ["limits", "continuity", "asymptotes"],
                "display_order": 6,
            },
        ],
    },
    {
        "name": "Differentiation: Definition and Fundamental Properties",
        "description": "Defines the derivative using limits, connects differentiability to continuity, and establishes basic derivative rules.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 12.0,
        "display_order": 2,
        "topics": [
            {
                "name": "Defining Average and Instantaneous Rates of Change",
                "description": "Distinguishes between average rate of change over an interval and instantaneous rate of change at a point.",
                "skill_tags": ["rates-of-change"],
                "display_order": 1,
            },
            {
                "name": "Defining the Derivative and Using Derivative Notation",
                "description": "Defines the derivative as a limit of a difference quotient and introduces Leibniz and prime notation.",
                "skill_tags": ["derivatives", "notation"],
                "display_order": 2,
            },
            {
                "name": "Estimating Derivatives from Tables and Graphs",
                "description": "Approximates derivative values using numerical data and graphical slope analysis.",
                "skill_tags": ["derivatives", "graphical-analysis"],
                "display_order": 3,
            },
            {
                "name": "Connecting Differentiability and Continuity",
                "description": "Explores how differentiability implies continuity and identifies points where a function fails to be differentiable.",
                "skill_tags": ["differentiability", "continuity"],
                "display_order": 4,
            },
            {
                "name": "Applying Basic Differentiation Rules",
                "description": "Applies the constant, power, sum, and difference rules to compute derivatives.",
                "skill_tags": ["derivatives", "power-rule"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Differentiation: Composite, Implicit, and Inverse Functions",
        "description": "Extends differentiation rules to products, quotients, compositions, implicit relations, and inverse functions.",
        "ap_weight_min": 9.0,
        "ap_weight_max": 13.0,
        "display_order": 3,
        "topics": [
            {
                "name": "The Chain Rule",
                "description": "Differentiates composite functions using the chain rule.",
                "skill_tags": ["chain-rule", "derivatives"],
                "display_order": 1,
            },
            {
                "name": "Implicit Differentiation",
                "description": "Differentiates equations that are not explicitly solved for y with respect to x.",
                "skill_tags": ["implicit-differentiation"],
                "display_order": 2,
            },
            {
                "name": "Differentiating Inverse Functions",
                "description": "Uses the relationship between a function and its inverse to find derivatives of inverse functions.",
                "skill_tags": ["inverse-functions", "derivatives"],
                "display_order": 3,
            },
            {
                "name": "Differentiating Inverse Trigonometric Functions",
                "description": "Applies known derivative formulas for arcsin, arccos, and arctan.",
                "skill_tags": ["inverse-trig", "derivatives"],
                "display_order": 4,
            },
            {
                "name": "Calculating Higher-Order Derivatives",
                "description": "Computes second and higher-order derivatives and interprets them in context.",
                "skill_tags": ["higher-order-derivatives"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Contextual Applications of Differentiation",
        "description": "Applies derivatives to problems involving motion, related rates, linearization, and L'Hospital's Rule.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 15.0,
        "display_order": 4,
        "topics": [
            {
                "name": "Interpreting the Meaning of the Derivative in Context",
                "description": "Connects the derivative to rates of change in applied, real-world scenarios.",
                "skill_tags": ["derivatives", "applications"],
                "display_order": 1,
            },
            {
                "name": "Straight-Line Motion: Position, Velocity, and Acceleration",
                "description": "Uses derivatives to analyze position, velocity, speed, and acceleration of a particle.",
                "skill_tags": ["motion", "velocity", "acceleration"],
                "display_order": 2,
            },
            {
                "name": "Rates of Change in Non-Motion Contexts",
                "description": "Applies derivatives to model rates of change in non-motion applied problems.",
                "skill_tags": ["rates-of-change", "applications"],
                "display_order": 3,
            },
            {
                "name": "Introduction to Related Rates",
                "description": "Solves related rates problems by differentiating equations relating multiple changing quantities.",
                "skill_tags": ["related-rates"],
                "display_order": 4,
            },
            {
                "name": "Approximating Values Using Local Linearity and Linearization",
                "description": "Uses tangent line approximations to estimate function values near a point.",
                "skill_tags": ["linearization", "tangent-line"],
                "display_order": 5,
            },
            {
                "name": "Using L'Hospital's Rule for Indeterminate Forms",
                "description": "Applies L'Hospital's Rule to evaluate limits resulting in indeterminate forms.",
                "skill_tags": ["lhopitals-rule", "limits"],
                "display_order": 6,
            },
        ],
    },
    {
        "name": "Analytical Applications of Differentiation",
        "description": "Uses derivatives to characterize function behavior, including extrema, concavity, and optimization, and connects derivatives to graphical behavior via the Mean Value Theorem.",
        "ap_weight_min": 15.0,
        "ap_weight_max": 18.0,
        "display_order": 5,
        "topics": [
            {
                "name": "The Mean Value Theorem and Extreme Value Theorem",
                "description": "Applies the Mean Value Theorem and Extreme Value Theorem to justify conclusions about a function on an interval.",
                "skill_tags": ["mean-value-theorem", "extreme-value-theorem"],
                "display_order": 1,
            },
            {
                "name": "Determining Intervals of Increase and Decrease",
                "description": "Uses the first derivative to determine where a function is increasing or decreasing.",
                "skill_tags": ["increasing-decreasing", "first-derivative-test"],
                "display_order": 2,
            },
            {
                "name": "Using the First Derivative Test for Relative Extrema",
                "description": "Identifies local maxima and minima by analyzing sign changes in the first derivative.",
                "skill_tags": ["first-derivative-test", "extrema"],
                "display_order": 3,
            },
            {
                "name": "Using the Second Derivative Test for Concavity and Extrema",
                "description": "Uses the second derivative to determine concavity, points of inflection, and confirm relative extrema.",
                "skill_tags": ["second-derivative-test", "concavity"],
                "display_order": 4,
            },
            {
                "name": "Sketching Graphs of Functions and Their Derivatives",
                "description": "Connects the graphical behavior of f, f prime, and f double prime to one another.",
                "skill_tags": ["curve-sketching", "graphical-analysis"],
                "display_order": 5,
            },
            {
                "name": "Solving Optimization Problems",
                "description": "Uses derivatives to find absolute maximum and minimum values in applied optimization problems.",
                "skill_tags": ["optimization"],
                "display_order": 6,
            },
        ],
    },
    {
        "name": "Integration and Accumulation of Change",
        "description": "Introduces the definite integral as a limit of Riemann sums, the Fundamental Theorem of Calculus, and antidifferentiation techniques.",
        "ap_weight_min": 17.0,
        "ap_weight_max": 20.0,
        "display_order": 6,
        "topics": [
            {
                "name": "Estimating Definite Integrals Using Riemann Sums",
                "description": "Approximates area under a curve using left, right, midpoint Riemann sums and trapezoidal sums.",
                "skill_tags": ["riemann-sums", "definite-integrals"],
                "display_order": 1,
            },
            {
                "name": "The Definite Integral and Accumulation of Change",
                "description": "Interprets the definite integral as an accumulation of a rate of change over an interval.",
                "skill_tags": ["definite-integrals", "accumulation"],
                "display_order": 2,
            },
            {
                "name": "The Fundamental Theorem of Calculus and Definite Integrals",
                "description": "Uses the Fundamental Theorem of Calculus to evaluate definite integrals and connect derivatives and integrals.",
                "skill_tags": ["fundamental-theorem-of-calculus"],
                "display_order": 3,
            },
            {
                "name": "Antiderivatives and Indefinite Integrals",
                "description": "Finds antiderivatives using reverse power rule and basic antidifferentiation rules.",
                "skill_tags": ["antiderivatives", "indefinite-integrals"],
                "display_order": 4,
            },
            {
                "name": "Integrating Using Substitution",
                "description": "Uses u-substitution to evaluate indefinite and definite integrals of composite functions.",
                "skill_tags": ["u-substitution", "integration"],
                "display_order": 5,
            },
            {
                "name": "Using Accumulation Functions and the Second Fundamental Theorem",
                "description": "Differentiates functions defined by an integral with a variable bound using the Second Fundamental Theorem of Calculus.",
                "skill_tags": ["accumulation-functions", "fundamental-theorem-of-calculus"],
                "display_order": 6,
            },
        ],
    },
    {
        "name": "Differential Equations",
        "description": "Explores differential equations, slope fields, and exponential growth and decay models.",
        "ap_weight_min": 6.0,
        "ap_weight_max": 12.0,
        "display_order": 7,
        "topics": [
            {
                "name": "Modeling Situations with Differential Equations",
                "description": "Translates verbal descriptions of rates of change into differential equations.",
                "skill_tags": ["differential-equations", "modeling"],
                "display_order": 1,
            },
            {
                "name": "Verifying Solutions to Differential Equations",
                "description": "Confirms whether a given function is a solution to a differential equation.",
                "skill_tags": ["differential-equations", "verification"],
                "display_order": 2,
            },
            {
                "name": "Sketching and Interpreting Slope Fields",
                "description": "Draws and interprets slope fields to visualize solution curves of a differential equation.",
                "skill_tags": ["slope-fields"],
                "display_order": 3,
            },
            {
                "name": "Solving Separable Differential Equations",
                "description": "Uses separation of variables to find general and particular solutions to differential equations.",
                "skill_tags": ["separable-differential-equations"],
                "display_order": 4,
            },
            {
                "name": "Exponential Models with Differential Equations",
                "description": "Applies separable differential equations to model exponential growth and decay.",
                "skill_tags": ["exponential-growth-decay", "differential-equations"],
                "display_order": 5,
            },
        ],
    },
    {
        "name": "Applications of Integration",
        "description": "Uses definite integrals to compute average value, area between curves, and volumes of solids, and models particle motion.",
        "ap_weight_min": 10.0,
        "ap_weight_max": 15.0,
        "display_order": 8,
        "topics": [
            {
                "name": "Average Value of a Function",
                "description": "Uses the definite integral to compute the average value of a function on an interval.",
                "skill_tags": ["average-value", "definite-integrals"],
                "display_order": 1,
            },
            {
                "name": "Position, Velocity, and Acceleration Using Integrals",
                "description": "Uses definite and indefinite integrals to find position and velocity functions from acceleration or velocity.",
                "skill_tags": ["motion", "integration"],
                "display_order": 2,
            },
            {
                "name": "Using Accumulation Functions and Definite Integrals in Applied Contexts",
                "description": "Applies definite integrals to solve applied accumulation problems.",
                "skill_tags": ["accumulation", "applications"],
                "display_order": 3,
            },
            {
                "name": "Finding the Area Between Curves",
                "description": "Sets up and evaluates definite integrals to find the area between two or more curves.",
                "skill_tags": ["area-between-curves"],
                "display_order": 4,
            },
            {
                "name": "Volumes with Cross Sections",
                "description": "Computes volumes of solids with known cross-sections perpendicular to an axis.",
                "skill_tags": ["volume", "cross-sections"],
                "display_order": 5,
            },
            {
                "name": "Volume of Solids of Revolution Using Disc and Washer Methods",
                "description": "Uses the disc and washer methods to find volumes of solids formed by revolving a region about an axis.",
                "skill_tags": ["volume", "disc-washer-method"],
                "display_order": 6,
            },
        ],
    },
]
