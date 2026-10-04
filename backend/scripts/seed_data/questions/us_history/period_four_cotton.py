"""Original questions on the distinct stages of cotton production and coercion."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 4: 1800-1848', topic='The Cotton Revolution and the Expansion of Slavery', code='4.13', set_id='gin-labor',
    source_url='https://www.archives.gov/milestone-documents/patent-for-cotton-gin',
    source_kind='original instructional summary',
    stimulus='The cotton gin accelerated the separation of seeds from cotton fibers. It did not mechanize planting or picking. As commercial cotton cultivation expanded, enslavers sought more land and forced labor to supply the crop. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Why could a labor-saving processing device coexist with increased demand for enslaved field labor?', 1, [
            ('The gin made harvesting slower in order to preserve jobs in the fields.', 'The gin changed processing after harvest; it did not slow harvesting to preserve employment.'),
            ('Faster processing encouraged expansion of cultivation, which still required extensive field labor.', 'Saving labor at one production stage could increase the scale of other labor-intensive stages.'),
            ('The gin substituted machinery for planting and picking as well as seed removal.', 'The stimulus explicitly distinguishes seed removal from unmechanized field work.'),
            ('The gin required every cotton planter to emancipate workers before using it.', 'The device imposed no such legal condition, and cotton cultivation expanded under slavery.'),
        ]),
        ('claims-evidence', 3, 'Which finding would most directly support the relationship described in the summary?', 2, [
            ('A patent record specifying the dimensions of a gin’s mechanical parts.', 'A patent describes machinery, but does not by itself establish changes in acreage or forced labor.'),
            ('A newspaper advertisement praising a gin as an ingenious invention.', 'Promotional praise is weaker evidence of actual changes in production and labor.'),
            ('Plantation records documenting expanded cotton acreage and acquisitions of enslaved workers after processing capacity increased.', 'Linked records connect processing capacity, cultivation, and demand for forced labor.'),
            ('A shipping manifest listing the final destination of a single cotton bale.', 'One shipment’s destination does not establish changes in cultivation or labor demand.'),
        ]),
        ('argumentation', 4, 'Which revision would make an explanation of cotton expansion more historically adequate?', 0, [
            ('Consider market demand, access to land, and laws sustaining slavery alongside processing technology.', 'Technology operated within economic and political conditions rather than independently causing every outcome.'),
            ('Treat the patent date as sufficient proof that all later changes resulted from the invention.', 'Chronological precedence alone cannot establish the full causal explanation.'),
            ('Assume that increasing output demonstrates improving living conditions for enslaved workers.', 'Output measures do not establish workers’ welfare under coercive labor conditions.'),
            ('Infer that regions without cotton gins could have no enslaved labor.', 'Slavery existed in many activities and regions beyond cotton processing.'),
        ]),
    ],
)
