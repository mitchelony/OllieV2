from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="forbid",
        case_sensitive=True,
        populate_by_name=True,
    )

    env: str = Field(default="dev", validation_alias="ENV")
    database_url: str = Field(validation_alias="DATABASE_URL")
    cors_origins: str = Field(default="http://localhost:5173", validation_alias="CORS_ORIGINS")


settings = Settings()