from datetime import datetime

from pydantic import BaseModel


class TopicMasteryRead(BaseModel):
    topic_id: int
    topic_name: str
    mastery_score: float
    confidence_score: float
    retention_score: float
    topic_timer: float
    attempts_count: int
    last_practiced_at: datetime | None


class UnitMasteryRead(BaseModel):
    unit_id: int
    unit_name: str
    mastery_score: float
    confidence_score: float
    topics: list[TopicMasteryRead] = []


class SubjectMasteryResponse(BaseModel):
    subject_id: int
    subject_name: str
    mastery_score: float
    confidence_score: float
    predicted_ap_score: int
    units: list[UnitMasteryRead] = []
