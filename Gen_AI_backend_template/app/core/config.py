from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    service_name: str
    environment: str
    log_level: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()