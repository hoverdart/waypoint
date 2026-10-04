"""Original questions on national labor action and railroad regulation."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 6: 1865-1898', topic='Labor and the Rise of Unions', code='6.7', set_id='pullman-boycott',
    source_url='https://home.nps.gov/pull/learn/historyculture/the-strike-of-1894.htm',
    source_kind='original instructional summary',
    stimulus='In 1894, a strike by Pullman factory workers developed into a wider American Railway Union boycott of handling Pullman cars. Because the cars traveled on many railroads, the boycott disrupted national transportation. Federal officials obtained an injunction and deployed troops, invoking protection of interstate commerce and mail delivery. The union was defeated. This is an original instructional summary; the local factory strike and the broader railroad boycott were related but distinct actions.',
    items=[
        ('causation', 2, 'Which feature of the railroad economy best explains how this local dispute became a national conflict?', 1, [
            ('Most railway employees worked directly for the Pullman factory under identical contracts.', 'The boycott extended beyond the factory workforce through workers on interconnected railroads.'),
            ('The use of Pullman cars across an interconnected transportation network allowed a boycott to affect many routes.', 'The network linked the company’s cars to national rail operations, widening the effects of refusal to handle them.'),
            ('Railroads primarily served isolated local markets with little movement between states.', 'The national disruption depended on interstate connections rather than isolated local service.'),
            ('The factory strike automatically transferred ownership of participating railroads to the union.', 'The workers used collective refusal of labor, not an automatic transfer of railroad ownership.'),
        ]),
        ('contextualization', 3, 'Federal intervention in this conflict most directly demonstrates which limitation on organized labor’s power?', 2, [
            ('Federal courts treated transportation disputes as outside all national authority.', 'The injunction asserted national authority over conduct affecting commerce and the mail.'),
            ('Union recognition required approval from every state legislature before workers could organize.', 'The episode concerns judicial and executive intervention, not a universal state-legislature approval procedure.'),
            ('Government action to protect commerce could undermine a union’s use of a widespread work stoppage.', 'The injunction and troops constrained the boycott and weakened the union’s bargaining strategy.'),
            ('The federal government required employers to accept union demands whenever mail service was disrupted.', 'Intervention worked against the boycott rather than compelling acceptance of the workers’ demands.'),
        ]),
        ('argumentation', 4, 'Which comparison would best investigate whether industrial interdependence strengthened workers without guaranteeing successful strikes?', 0, [
            ('The geographic reach of work stoppages alongside employer coordination, court orders, and strike outcomes.', 'These sources distinguish the ability to disrupt a network from the institutional forces shaping whether disruption secured concessions.'),
            ('The number of miles of track alone, treated as a direct measure of concessions won by workers.', 'Track mileage does not by itself establish bargaining outcomes or the effects of intervention.'),
            ('The union’s announced demands alone, treated as proof that employers accepted them.', 'A statement of demands identifies goals, not their achievement.'),
            ('A company’s annual profits without evidence about union action or the government’s response.', 'Profits may supply context but cannot alone explain the relationship between collective action and its outcome.'),
        ]),
    ],
)

QUESTIONS += source_set(
    period='Period 6: 1865-1898', topic='Government and Economic Controversies', code='6.12', set_id='interstate-commerce',
    source_url='https://www.archives.gov/milestone-documents/interstate-commerce-act',
    source_kind='original instructional summary',
    stimulus='Complaints about discriminatory railroad charges helped produce the Interstate Commerce Act of 1887. The act established the Interstate Commerce Commission and rules governing railroad practices, including discriminatory rates. It placed federal oversight over aspects of privately operated interstate transportation rather than transferring the railroads into public ownership. Early enforcement faced significant limitations. This is an original instructional summary.',
    items=[
        ('comparison', 2, 'Which distinction best describes the policy created by the act?', 3, [
            ('It replaced privately operated railroads with a federally owned transportation system.', 'The act regulated private carriers rather than generally nationalizing railroad ownership.'),
            ('It left interstate rate disputes exclusively to individual state governments.', 'The commission represented a federal regulatory response to interstate transportation issues.'),
            ('It guaranteed that all shippers would pay an identical total price regardless of distance or service.', 'Restrictions on discrimination should not be confused with one identical total charge for every shipment.'),
            ('It introduced federal regulation of private business practices while retaining private ownership.', 'The commission and statutory rules increased public oversight without making the railroads government-owned.'),
        ]),
        ('causation', 3, 'Why could discriminatory rates encourage farmers and small shippers to demand government intervention?', 0, [
            ('Dependence on rail transport could expose them to charges less favorable than those obtained by large shippers.', 'Unequal bargaining power and access to favorable rates could make regulation attractive to smaller customers.'),
            ('Farmers generally owned the major interstate railroads and sought to prevent any oversight of their prices.', 'The grievances described concern users’ dependence on carriers rather than general farmer ownership of the major lines.'),
            ('Federal regulation would necessarily eliminate all production risks faced by agricultural businesses.', 'Railroad regulation could address transport practices without removing weather, crop, or market risks.'),
            ('The law would prohibit transporting agricultural goods across state boundaries.', 'The act regulated interstate transportation practices; it did not generally ban agricultural shipments.'),
        ]),
        ('argumentation', 4, 'Which evidence would best evaluate the difference between the act’s regulatory ambition and its early practical effects?', 1, [
            ('The creation of the commission alone, interpreted as proof that rate discrimination immediately ended.', 'Creating an institution establishes authority and intent, not full implementation.'),
            ('Statutory provisions compared with complaints, commission decisions, court rulings, and subsequent carrier practices.', 'These records connect formal powers with enforcement and outcomes, allowing the historian to assess practical limitations.'),
            ('A later period’s regulatory powers projected backward onto the commission’s original authority.', 'Later powers cannot be assumed to describe the agency’s authority or effectiveness in 1887.'),
            ('A single favorable editorial treated as a complete account of the experience of all shippers.', 'An editorial supplies a perspective but cannot establish outcomes for all affected customers.'),
        ]),
    ],
)
