from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY") or "secret_key"
    DATABASE_URL: str = os.getenv("DATABASE_URL") or "postgresql://aegis_user:aegis_password@localhost:5432/aegis_db"


settings = Settings()


if settings.DATABASE_URL.startswith("postgres://"):
    settings.DATABASE_URL = settings.DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    settings.DATABASE_URL = settings.DATABASE_URL