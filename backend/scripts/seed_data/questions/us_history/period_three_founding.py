"""Original questions using public-domain founding texts, checked against NARA."""
from .builders import source_set

QUESTIONS = source_set(period='Period 3: 1754-1800', topic='Political Ideas of the Revolution', code='3.4',
 source_url='https://www.archives.gov/founding-docs/declaration-transcript', source_kind='primary excerpt',
 stimulus='Declaration of Independence, July 4, 1776: “Governments are instituted among Men, deriving their just powers from the consent of the governed”', items=[
 ('claims-evidence',2,'The passage locates legitimate political authority primarily in',1,[
 ('a ruler’s hereditary claim.','Hereditary succession is not the stated source of legitimate power.'),
 ('the agreement of those governed.','Consent of the governed supplies the justification for governmental power.'),
 ('the military strength of an empire.','The passage defines legitimacy through consent rather than force.'),
 ('the economic wealth of a monarch.','Royal wealth is not the basis identified in the excerpt.'),
 ]),
 ('sourcing',3,'In the context of the Declaration, this principle chiefly served to',2,[
 ('specify how federal judges would be appointed.','The Declaration justified separation; it did not create the later federal judicial system.'),
 ('promise loyalty to the king regardless of his actions.','The principle could justify rejecting authority that lacked legitimate consent.'),
 ('provide a justification for rejecting British rule.','A principle of consent supported the argument that the colonies could establish another government.'),
 ('end debate over how the new states would govern themselves.','A general justification for independence did not settle the structure of future governments.'),
 ]),
 ('contextualization',4,'Which additional evidence would be most useful for assessing the distance between this principle and political participation in the revolutionary era?',0,[
 ('State voting rules and records showing who could vote or hold office.','These reveal how access to political power compared with the stated principle.'),
 ('The number of signatures on a modern reproduction of the Declaration.','A modern reproduction does not establish eighteenth-century participation.'),
 ('The document’s handwriting style alone.','Handwriting cannot establish the legal boundaries of political participation.'),
 ('An assumption that every resident already had identical political rights.','That assumption bypasses the historical question rather than investigating it.'),
 ]),
 ('making-connections',3,'Which interpretation best distinguishes a statement of political ideals from evidence of social conditions?',3,[
 ('The principle proves that unequal legal status ended immediately in 1776.','A declared ideal does not establish immediate equality in law or practice.'),
 ('The continued existence of inequality makes the principle impossible to study.','The tension between ideals and practice is itself historically significant.'),
 ('Political ideals have no relationship to later claims for rights.','People can invoke stated ideals in later arguments, although specific connections need evidence.'),
 ('The principle could provide language for challenging exclusions even when those exclusions persisted.','An ideal can become a standard for criticism without accurately describing existing conditions.'),
 ]),
]) + source_set(period='Period 3: 1754-1800', topic='Constitutional Structure and Federal Power', code='3.9',
 source_url='https://www.archives.gov/founding-docs/constitution-transcript', source_kind='primary excerpt',
 stimulus='United States Constitution, Article I, Section 8 (1787), excerpt from the powers of Congress: “To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;”', items=[
 ('claims-evidence',2,'Which power does the excerpt explicitly assign to Congress?',2,[
 ('Appointing all state governors.','The passage addresses commerce, not state executive appointments.'),
 ('Eliminating all state governments.','The provision assumes the continued existence of several states.'),
 ('Regulating commerce among states.','Interstate commerce is expressly included in the listed power.'),
 ('Choosing every member of the judiciary without another branch.','Judicial appointments are not described in this excerpt.'),
 ]),
 ('comparison',3,'Compared with a system in which each state independently controls all interstate commercial relations, this provision',0,[
 ('creates a national basis for regulating trade across state boundaries.','Congress receives authority over commerce among the states.'),
 ('requires every state to maintain an entirely separate foreign policy.','The excerpt gives Congress a role in foreign commerce, not separate state foreign policies.'),
 ('prevents any national involvement in economic questions.','Regulating commerce is a national economic power.'),
 ('assigns commercial disputes exclusively to colonial governors appointed by Britain.','The Constitution establishes a United States government, not renewed British colonial rule.'),
 ]),
 ('sourcing',4,'What is an important limitation of using this clause alone to describe federal power in the early republic?',1,[
 ('A constitutional provision cannot provide evidence about institutions.','The clause directly defines an institutional authority.'),
 ('It identifies a granted power but does not show how officials interpreted or exercised it in particular disputes.','Practice and interpretation require additional evidence beyond the grant itself.'),
 ('It proves that no disagreements about commerce occurred after ratification.','A written grant does not establish universal agreement about its reach.'),
 ('It lists every power of all three branches.','The excerpt is one part of Congress’s enumerated powers.'),
 ]),
 ('causation',3,'Which problem would a supporter most plausibly argue this provision helped address?',3,[
 ('The absence of any trade between the states.','The provision does not imply that trade had been nonexistent.'),
 ('A requirement that all commerce be directed personally by the British king.','That is not the governmental arrangement the Constitution replaced.'),
 ('The need to make every state’s population identical.','Population equality is unrelated to the enumerated commerce power.'),
 ('Difficulty coordinating commercial rules that affected more than one state.','National authority could address problems crossing individual state jurisdictions.'),
 ]),
])
