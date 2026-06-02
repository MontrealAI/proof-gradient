from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PROOF_GRADIENT_", extra="ignore")

    env: str = "local"
    database_url: str = "sqlite:///./proof_gradient.db"
    provider: str = "mock"
    max_cost_usd: float = 1.0
    max_latency_seconds: int = 120


settings = Settings()
