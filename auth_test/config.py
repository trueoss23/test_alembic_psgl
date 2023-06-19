from pydantic import BaseSettings
from functools import lru_cache

import os


class Settings(BaseSettings):
    app_name: str = "Auth"
    app_port: int = os.getenv("APP_PORT", 8000)
    app_secret_key: str = os.getenv("APP_SECRET_KEY")
    app_refresh_secret_key: str = os.getenv("APP_REFRESH_SECRET_KEY")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
