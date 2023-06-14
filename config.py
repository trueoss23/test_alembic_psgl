from pydantic import BaseSettings
from functools import lru_cache

import os


class Settings(BaseSettings):
    app_name: str = "CRUD-1"
    app_port: int = os.getenv("PORT", 8000)
    db_user: str = os.getenv("DB_USER")
    db_pass: str = os.getenv("DB_PASS")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()