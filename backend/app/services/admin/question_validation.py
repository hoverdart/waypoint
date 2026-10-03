from app.core.exceptions import DomainError
from app.schemas.admin import AdminQuestionCreate


def validate_question_content(data: AdminQuestionCreate) -> None:
    if not data.prompt.strip() or not data.correct_answer.strip():
        raise DomainError("Prompt and answer cannot be blank")
    labels = [option.label for option in data.options]
    if len(set(labels)) != len(labels):
        raise DomainError("Answer labels must be unique")
    if data.type == "mcq":
        if not 2 <= len(data.options) <= 6:
            raise DomainError("Multiple-choice questions need 2–6 options")
        correct = [o.label for o in data.options if o.is_correct]
        if correct != [data.correct_answer]:
            raise DomainError("Exactly one option must match the correct answer")
        if any(not o.text.strip() for o in data.options):
            raise DomainError("Answer options cannot be blank")
    else:
        if data.options:
            raise DomainError("Free-response questions cannot have answer options")
        checklist = (data.rubric_json or {}).get("checklist")
        if not isinstance(checklist, list) or not 1 <= len(checklist) <= 20:
            raise DomainError("Free-response questions need a rubric with 1–20 criteria")
        for criterion in checklist:
            if not isinstance(criterion, dict):
                raise DomainError("Invalid rubric criterion")
            point, points, keywords = criterion.get("point"), criterion.get("points"), criterion.get("keywords")
            if not isinstance(point, str) or not point.strip() or len(point) > 2000:
                raise DomainError("Rubric criteria need a short description")
            if type(points) is not int or not 1 <= points <= 20:
                raise DomainError("Rubric points must be integers between 1 and 20")
            if not isinstance(keywords, list) or not 1 <= len(keywords) <= 30 or any(not isinstance(k, str) or not k.strip() or len(k) > 200 for k in keywords):
                raise DomainError("Rubric criteria need 1–30 nonempty keywords")
    if any(e.option_label is not None and e.option_label not in labels for e in data.explanations):
        raise DomainError("An explanation refers to an unknown answer option")
    if len(data.explanations) > 20:
        raise DomainError("Too many explanations")
    if data.validation_status == "approved":
        explained = {e.option_label for e in data.explanations}
        if None not in explained and (data.type == "frq" or not set(labels).issubset(explained)):
            raise DomainError("Approved questions need a general explanation or explanations for every option")
