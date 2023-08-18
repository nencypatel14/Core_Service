from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    FROM_MOBILE_NUMBER: str
    ACCOUNT_SID: str
    AUTH_TOKEN: str

    class config:
        env_file = './.env'


setiings = Settings()
