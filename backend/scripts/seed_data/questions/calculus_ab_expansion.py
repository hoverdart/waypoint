"""Original, offline-authored practice covering gaps in the Calculus AB bank.

These are independent study questions, not reproduced College Board exam items.
Each explanation is shown for every answer choice to make the reasoning available
regardless of the selected distractor.
"""

# topic, prompt, correct response, three distractors, reasoning
ITEMS = [
    (
        "Estimating Limits from Graphs and Tables",
        "Values of f(x) are 2.98, 2.998, 3.002, and 3.02 at x = 0.99, 0.999, 1.001, and 1.01, respectively. Also, f(1) = 7. Which value is best supported as an estimate of lim(x→1) f(x)?",
        "3", ["7", "1", "The limit cannot exist because f(1) = 7"],
        "The values approach 3 from both sides of x = 1. A limit describes nearby behavior, so changing the value at x = 1 to 7 does not change this estimate. A finite table supports an estimate rather than proving a limit.",
    ),
    (
        "Selecting Procedures for Determining Limits",
        "Which first step most directly resolves lim(x→4) (sqrt(x) − 2)/(x − 4)?",
        "Multiply numerator and denominator by sqrt(x) + 2",
        ["Substitute x = 4 and conclude the limit is zero", "Cancel x from the numerator and denominator", "Replace sqrt(x) by x/2 for all x near 4"],
        "Rationalizing gives (x − 4)/[(x − 4)(sqrt(x) + 2)]. For x ≠ 4 this equals 1/(sqrt(x) + 2), whose limit is 1/4. Direct substitution initially produces 0/0, not a value of the limit.",
    ),
    (
        "Determining Limits Using the Squeeze Theorem",
        "For x ≠ 0, let g(x) = x² sin(1/x). What is lim(x→0) g(x)?",
        "0", ["1", "−1", "The limit does not exist because sin(1/x) oscillates"],
        "Since −1 ≤ sin(1/x) ≤ 1, multiplying by x² gives −x² ≤ g(x) ≤ x². Both bounding functions approach 0, so the squeeze theorem gives a limit of 0 even though the sine factor oscillates.",
    ),
    (
        "Estimating Derivatives from Tables and Graphs",
        "A table gives s(1.9) = 7.22 meters and s(2.1) = 8.82 meters, where time is in seconds. Using the secant through these nearby times, estimate s′(2).",
        "8 meters per second", ["1.6 meters per second", "4 meters per second", "16 meters per second"],
        "The symmetric difference quotient is [s(2.1) − s(1.9)]/(2.1 − 1.9) = 1.60/0.20 = 8. The quotient estimates the instantaneous rate at the midpoint, and its units are meters per second.",
    ),
    (
        "Differentiating Inverse Functions",
        "An invertible differentiable function f satisfies f(2) = 5 and f′(2) = 3. What is (f⁻¹)′(5)?",
        "1/3", ["3", "1/5", "2/5"],
        "The inverse derivative formula is (f⁻¹)′(y) = 1/f′(f⁻¹(y)). Since f⁻¹(5) = 2, the required value is 1/f′(2) = 1/3. The derivative is evaluated at the preimage, not at 5.",
    ),
    (
        "Calculating Higher-Order Derivatives",
        "If f(x) = x⁴ − 2x³, what is f″(2)?",
        "24", ["8", "16", "48"],
        "Differentiate twice: f′(x) = 4x³ − 6x² and f″(x) = 12x² − 12x. At x = 2, this gives 48 − 24 = 24. The value f′(2) = 8 is the first derivative, not the second.",
    ),
    (
        "Interpreting the Meaning of the Derivative in Context",
        "C(t) is the concentration of a substance, in milligrams per liter, t minutes after an experiment begins. If C′(4) = −0.6, which interpretation is correct?",
        "At 4 minutes, concentration is decreasing at 0.6 milligrams per liter per minute",
        ["At 4 minutes, the concentration is −0.6 milligrams per liter", "The concentration falls by exactly 0.6 milligrams per liter during every minute", "After 4 minutes, a total of 0.6 milligrams has been removed"],
        "A derivative is an instantaneous rate. Its negative sign indicates a decrease, and its units are concentration divided by time. It does not give the concentration itself or guarantee a constant rate over an interval.",
    ),
    (
        "Rates of Change in Non-Motion Contexts",
        "The cost of producing q notebooks is C(q) = 500 + 4q + 0.01q² dollars. Use marginal cost at q = 100 to estimate the cost of producing one additional notebook.",
        "$6", ["$4", "$10", "$1,000"],
        "Marginal cost is C′(q) = 4 + 0.02q dollars per notebook. Thus C′(100) = 6. This approximates C(101) − C(100), whose exact value is $6.01; the fixed cost 500 does not contribute to the derivative.",
    ),
    (
        "Approximating Values Using Local Linearity and Linearization",
        "Use the tangent line to f(x) = sqrt(x) at x = 9 to approximate sqrt(9.12).",
        "3.02", ["3.12", "3.06", "3.002"],
        "The tangent line is L(x) = f(9) + f′(9)(x − 9) = 3 + (1/6)(x − 9). Substituting 9.12 gives 3 + 0.12/6 = 3.02. Because sqrt(x) is concave down, this tangent estimate is slightly above the exact value.",
    ),
    (
        "The Mean Value Theorem and Extreme Value Theorem",
        "For f(x) = x² on [1, 3], which value of c satisfies the conclusion of the Mean Value Theorem?",
        "2", ["1", "3", "4"],
        "The average slope is [f(3) − f(1)]/(3 − 1) = 8/2 = 4. Since f′(c) = 2c, setting 2c = 4 gives c = 2, which lies in (1, 3). The polynomial is continuous on the closed interval and differentiable on the open interval.",
    ),
    (
        "Determining Intervals of Increase and Decrease",
        "A function has derivative f′(x) = (x − 1)(x + 2). On which interval is f strictly decreasing?",
        "(−2, 1)", ["(−∞, −2)", "(1, ∞)", "(−∞, −2) and (1, ∞)"],
        "The derivative is negative between its zeros −2 and 1: x − 1 is negative and x + 2 is positive there. Outside that interval, the two factors share a sign, so the derivative is positive and the function increases.",
    ),
    (
        "Sketching Graphs of Functions and Their Derivatives",
        "On an interval, the graph of f is increasing and concave down. Which statement about the graph of f′ must hold on that interval, assuming f′ > 0 and f″ < 0 throughout?",
        "It lies above the x-axis and is decreasing",
        ["It lies below the x-axis and is increasing", "It lies above the x-axis and is increasing", "It lies below the x-axis and is decreasing"],
        "Increasing f corresponds to positive slope, so f′ is above the axis. Concave-down f has decreasing slopes, so f′ decreases. The sign of f′ and the direction of change of f′ express different features of f.",
    ),
    (
        "The Definite Integral and Accumulation of Change",
        "Water enters a tank at r(t) = 3t + 2 liters per minute for 0 ≤ t ≤ 2. There is no outflow. How much water is added during these two minutes?",
        "10 liters", ["8 liters", "5 liters", "16 liters"],
        "The added volume is the integral of the inflow rate: ∫₀²(3t + 2)dt = [(3/2)t² + 2t]₀² = 6 + 4 = 10 liters. The final rate r(2) = 8 has units of liters per minute and is not the accumulated volume.",
    ),
    (
        "Antiderivatives and Indefinite Integrals",
        "Which expression gives all antiderivatives of 6x² − 4x + 3?",
        "2x³ − 2x² + 3x + C",
        ["12x − 4 + C", "6x³ − 4x² + 3x + C", "2x³ − 4x² + 3x + C"],
        "Integrate term by term using ∫xⁿdx = xⁿ⁺¹/(n + 1) + C. This gives 2x³ − 2x² + 3x + C. Differentiating the result recovers every original coefficient; 12x − 4 is instead the derivative of the integrand.",
    ),
    (
        "Modeling Situations with Differential Equations",
        "A population P(t) grows at a rate proportional to its current size. Initially it contains 200 organisms, and its initial growth rate is 10 organisms per day. Which differential equation models this statement?",
        "dP/dt = 0.05P", ["dP/dt = 10", "dP/dt = 200P", "dP/dt = 0.05t"],
        "Proportional growth has the form P′ = kP. At t = 0, 10 = k(200), so k = 0.05 per day. A constant derivative of 10 would model linear growth rather than a rate proportional to population.",
    ),
    (
        "Verifying Solutions to Differential Equations",
        "Which function satisfies both y′ = 2y and y(0) = 3?",
        "y = 3e²ˣ", ["y = 2e³ˣ", "y = 3eˣ", "y = 6x + 3"],
        "For y = 3e^(2x), y′ = 6e^(2x) = 2y and y(0) = 3. The line 6x + 3 has the correct initial value and initial slope, but fails y′ = 2y away from x = 0. Both the equation and initial condition must hold.",
    ),
    (
        "Using Accumulation Functions and Definite Integrals in Applied Contexts",
        "A tank contains 20 liters at t = 0. Its net inflow rate is r(t) = 4 − t liters per minute for 0 ≤ t ≤ 3. How much water is in the tank at t = 3?",
        "27.5 liters", ["7.5 liters", "23 liters", "32 liters"],
        "The amount at time 3 is the initial amount plus net change: 20 + ∫₀³(4 − t)dt = 20 + 12 − 9/2 = 27.5. The value 7.5 is only the change, and r(3) = 1 is a rate rather than an amount.",
    ),
    (
        "Volumes with Cross Sections",
        "A solid has a base bounded by y = x, y = 0, and x = 2. Cross sections perpendicular to the x-axis are squares whose sides lie in the base. What is its volume?",
        "8/3 cubic units", ["2 cubic units", "4 cubic units", "8 cubic units"],
        "At position x, the vertical length in the base is x, so the square cross section has area A(x) = x². The volume is ∫₀² x² dx = [x³/3]₀² = 8/3. Integrating the side length instead would compute base area, not volume.",
    ),
]


def build_questions(units):
    topic_to_unit = {topic['name']: unit['name'] for unit in units for topic in unit['topics']}
    result = []
    for index, (topic, prompt, correct, distractors, reasoning) in enumerate(ITEMS):
        choices = list(distractors)
        position = index % 4
        choices.insert(position, correct)
        result.append({
            'unit_name': topic_to_unit[topic], 'topic_name': topic,
            'type': 'mcq', 'difficulty': 2 if index % 3 else 3,
            'prompt': prompt, 'correct_answer': 'ABCD'[position],
            'source': 'generated', 'validation_status': 'approved',
            'skill_tags': ['concept-application'], 'misconception_tags': [],
            'options': [{'label': 'ABCD'[i], 'text': text, 'is_correct': i == position}
                        for i, text in enumerate(choices)],
            'explanations': [{'option_label': 'ABCD'[i], 'explanation': reasoning,
                              'misconception_tag': None} for i in range(4)],
            'rubric_json': None,
        })
    return result
