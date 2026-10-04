"""Original questions on diplomacy and the Revolutionary War."""
from .builders import source_set

QUESTIONS = source_set(
    period='Period 3: 1754-1800', topic='The American Revolutionary War', code='3.5',
    source_url='https://history.state.gov/milestones/1776-1783/french-alliance', source_kind='original instructional summary',
    stimulus='France aided the American cause before concluding a formal alliance in 1778. News of the British surrender at Saratoga helped persuade French officials to commit. French troops, supplies, and naval forces subsequently contributed to the American victory, including the surrender at Yorktown. This is an original instructional summary, not a primary-source quotation.',
    items=[
        ('causation', 2, 'Saratoga contributed to the American war effort beyond the battlefield primarily by', 1, [
            ('ending all fighting immediately.', 'Fighting continued after Saratoga; Yorktown came in 1781.'),
            ('helping secure a formal alliance with France.', 'The British surrender strengthened the case for French commitment to the American cause.'),
            ('placing the colonies back under French colonial government.', 'France allied with the United States rather than becoming its colonial ruler.'),
            ('eliminating the need for naval support.', 'Naval support remained important, particularly in the Yorktown campaign.'),
        ]),
        ('contextualization', 3, 'Which broader circumstance best explains French willingness to aid the Americans?', 3, [
            ('France’s obligation to obey laws passed by the Continental Congress.', 'France was a sovereign power and was not subject to the Continental Congress.'),
            ('The French Revolution had already established a republic allied with all other republics.', 'The French Revolution began in 1789; France was a monarchy during the American alliance.'),
            ('Britain and France had permanently ended imperial competition in 1763.', 'Rivalry continued after the Seven Years’ War and helped motivate French intervention.'),
            ('France saw an opportunity to weaken a longstanding imperial rival.', 'British difficulties in America offered France a strategic opportunity after its earlier defeat.'),
        ]),
        ('argumentation', 4, 'Which interpretation best accounts for both American resistance and French assistance?', 0, [
            ('American military efforts and international rivalry interacted to make independence possible.', 'American successes encouraged foreign support, which in turn increased American military capabilities.'),
            ('Foreign aid meant Americans played no role in securing independence.', 'Recognizing French assistance does not erase American military and diplomatic efforts.'),
            ('The war’s outcome was determined entirely by isolated colonial events.', 'French intervention shows that international developments mattered to the outcome.'),
            ('A shared republican form of government was necessary for military cooperation.', 'Monarchical France cooperated with the American republic, demonstrating that strategic interests could bridge political differences.'),
        ]),
        ('claims-evidence', 3, 'Which additional evidence would most directly support the claim that French assistance affected the Yorktown campaign?', 2, [
            ('A list of French court ceremonies held after the war.', 'Court ceremonies do not directly show a contribution to the military campaign.'),
            ('A copy of an unrelated colonial tax law from 1700.', 'An earlier tax law does not establish the effects of French intervention at Yorktown.'),
            ('Operational records documenting French naval action restricting British reinforcement or evacuation.', 'Such records would connect French action to constraints on British forces during the campaign.'),
            ('A statement that every American supported the alliance.', 'Public unanimity would not itself demonstrate the military effect of French assistance.'),
        ]),
    ],
)
