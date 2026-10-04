"""Original questions on the 1947 federal loyalty program."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 8: 1945-1980', topic='The Red Scare', code='8.3', set_id='federal-loyalty',
    source_url='https://www.trumanlibrary.gov/library/executive-orders/9835/executive-order-9835',
    source_kind='primary excerpt',
    stimulus='Executive Order 9835, issued by President Harry Truman on March 21, 1947, established procedures for an employee loyalty program in the executive branch. Its preamble called for protection against infiltration and stated: “equal protection from unfounded accusations of disloyalty must be afforded the loyal employees of the Government”. The quoted sentence expresses a stated objective, not a finding about the program’s effects.',
    items=[
        ('contextualization', 2, 'Which development most directly explains the setting for the order?', 1, [
            ('The postwar dissolution of the executive branch in favor of congressional administration.', 'The executive branch continued to function; the order concerned its employees.'),
            ('Growing Cold War concern that ideological conflict and espionage threatened institutions within the United States.', 'The loyalty program shows how international ideological tensions shaped domestic federal employment policy.'),
            ('A constitutional amendment requiring all employment disputes to be settled by state legislatures.', 'No such amendment explains the federal executive loyalty program.'),
            ('The completion of a settlement that ended political rivalry between the United States and Soviet Union.', 'The order emerged amid mounting rivalry, not after a settlement ending it.'),
        ]),
        ('sourcing', 3, 'What is the most defensible use of the preamble as historical evidence?', 2, [
            ('Proof that employees never faced unsupported accusations during the program.', 'A stated protection cannot establish that implementation always fulfilled it.'),
            ('A complete account of how accused employees experienced hearings.', 'The president’s policy statement does not supply employees’ accounts of their experiences.'),
            ('Evidence that the administration presented protection of loyal employees as compatible with its security program.', 'The preamble identifies a justification and intended safeguard; separate evidence is needed to evaluate practice.'),
            ('Evidence that federal loyalty investigations were prohibited by the order.', 'The order established procedures for investigations while stating protective aims.'),
        ]),
        ('argumentation', 4, 'A historian argues that the program adequately protected employees against unfounded accusations. Which research approach would most directly test the claim?', 0, [
            ('Compare case files, the evidence available to employees, hearing procedures, appeal outcomes, and employee accounts.', 'These sources allow evaluation of how the stated protection operated in actual cases, including procedural limits and contested outcomes.'),
            ('Count how often the word loyalty appears in the preamble.', 'Word frequency does not establish the fairness or reliability of case decisions.'),
            ('Use the order’s security rationale as sufficient proof of every investigation’s accuracy.', 'The rationale explains the policy’s justification, not the accuracy of each accusation.'),
            ('Treat the existence of any espionage case as proof that all investigated employees were disloyal.', 'Evidence about particular cases cannot establish guilt for all people investigated.'),
        ]),
    ],
)
