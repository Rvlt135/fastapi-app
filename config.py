from pydantic import BaseSettings
import os
from dotenv import load_dotenv


from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    server_host: str
    server_port: int = 8000
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER_DOCKER: str = os.getenv("POSTGRES_SERVER_DOCKER", "172.26.0.3")
    POSTGRES_SERVER_LOCALHOST: str = os.getenv("POSTGRES_SERVER_LOCALHOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    PGADMIN_DEFAULT_EMAIL: str = os.getenv("PGADMIN_DEFAULT_EMAIL")
    PGADMIN_DEFAULT_PASSWORD: str = os.getenv("PGADMIN_DEFAULT_PASSWORD")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_DOCKER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    ASYNC_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_DOCKER}:{POSTGRES_PORT}/{POSTGRES_DB}"


class Secrets(Settings):
    secret_key_auth_jwt = "SECRET"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8')