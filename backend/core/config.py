from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    DATABASE_URL: str

    API_PREFIX: str = "/api"
    DEBUG: bool = True

    ALLOWED_ORIGINS: str = ""
    OPEN_AI_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value: str) -> List[str]:
        return value.split(",") if value else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensetive = True


settings = Settings()
