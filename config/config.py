from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Extra

class Settings(BaseSettings):
    model_config= SettingsConfigDict(extra=Extra.allow, env_file='./.env', env_file_encoding='utf-8')
    DEBUG: bool = False
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

settings = Settings()
