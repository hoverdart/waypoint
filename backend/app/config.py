from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = "development"
    database_url: str = "postgresql+psycopg://waypoint:waypoint@localhost:5432/waypoint_dev"

    # Auth (Clerk)
    auth_provider: str = "clerk"
    clerk_secret_key: str = ""
    clerk_publishable_key: str = ""
    admin_user_ids: list[str] = []

    # AI (Anthropic) - capped, optional runtime explanations
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-haiku-4-5"
    ai_free_weekly_cap: int = 5
    ai_premium_weekly_cap: int = 30

    # Jobs
    jobs_trigger_secret: str = ""
    run_seed_on_boot: bool = False

    # CORS
    cors_allowed_origins: list[str] = ["http://localhost:3000"]

    # Diagnostic / planner tuning
    diagnostic_question_count: int = 20
    topic_timer_max: float = 30.0


@lru_cache
def get_settings() -> Settings:
    return Settings()
