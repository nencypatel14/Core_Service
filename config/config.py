from pydantic import BaseConfig


class Settings(BaseConfig):
    DEBUG: bool = False
    FROM_MOBILE_NUMBER: str
    ACCOUNT_SID: str
    AUTH_TOKEN: str

    class config:
        env_file = './.env'


setiings = Settings()
