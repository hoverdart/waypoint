"""Badge definitions for gamified mode. Each `rule_json["type"]` must match an
evaluator registered in app.services.xp.badge_service.RULE_EVALUATORS."""

BADGES = [
    {
        "name": "First Steps",
        "description": "Complete your first practice session.",
        "icon": "🎯",
        "rule_json": {"type": "first_session"},
    },
    {
        "name": "Diagnostic Complete",
        "description": "Finish your first diagnostic and get a baseline.",
        "icon": "🧭",
        "rule_json": {"type": "diagnostic_complete"},
    },
    {
        "name": "On Fire",
        "description": "Practice 3 days in a row.",
        "icon": "🔥",
        "rule_json": {"type": "streak", "days": 3},
    },
    {
        "name": "Unstoppable",
        "description": "Practice 7 days in a row.",
        "icon": "⚡",
        "rule_json": {"type": "streak", "days": 7},
    },
    {
        "name": "Century Club",
        "description": "Earn 100 total XP.",
        "icon": "💯",
        "rule_json": {"type": "total_xp", "amount": 100},
    },
    {
        "name": "Perfect Session",
        "description": "Answer every question correctly in a session of 5 or more questions.",
        "icon": "⭐",
        "rule_json": {"type": "perfect_session", "min_questions": 5},
    },
]
