from pydantic import BaseSettings
from functools import lru_cache

import os


class Settings(BaseSettings):
    app_name: str = "CRUD-1"
    app_port: int = os.getenv("PORT", 8000)
    app_secret_key: str = \
        'e6f73607f6160ca4df753e95a23055e30cc04fc03398930733df09841c462a49'

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
