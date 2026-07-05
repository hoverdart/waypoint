from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.core.exceptions import DomainError
from app.routers import (
    ai,
    auth,
    coach,
    daily_plan,
    dashboard,
    diagnostic,
    internal,
    mastery,
    onboarding,
    practice,
    question_reports,
    subjects,
    users,
)
from app.routers.admin import questions as admin_questions
from app.routers.admin import topics as admin_topics
from app.routers.admin import units as admin_units

settings = get_settings()

app = FastAPI(title="WayPoint API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(DomainError)
def handle_domain_error(request: Request, exc: DomainError) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": str(exc)})


@app.exception_handler(Exception)
def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
    if settings.environment == "development":
        raise exc
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(subjects.router)
app.include_router(onboarding.router)
app.include_router(diagnostic.router)
app.include_router(dashboard.router)
app.include_router(daily_plan.router)
app.include_router(practice.router)
app.include_router(mastery.router)
app.include_router(ai.router)
app.include_router(question_reports.router)
app.include_router(coach.router)
app.include_router(internal.router)
app.include_router(admin_questions.router)
app.include_router(admin_units.router)
app.include_router(admin_topics.router)
