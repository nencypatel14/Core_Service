from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    FROM_MOBILE_NUMBER: str
    ACCOUNT_SID: str
    AUTH_TOKEN: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    class config:
        env_file = './.env'

setting = Settings()
