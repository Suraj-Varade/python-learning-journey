import os
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# force load .env from project root (even when running from subfolder)
# dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
# load_dotenv(dotenv_path)
load_dotenv()


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = os.getenv("ENV_STATE", "dev")

    class Config:
        env_file: str = ".env"
        extra = "ignore"


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    MAIL_APP_SENDER: Optional[str] = None
    MAIL_APP_PASSWORD: Optional[str] = None


class DevConfig(GlobalConfig):
    DATABASE_URL: str  # = os.getenv("DEV_DATABASE_URL", "sqlite:///data.db")
    MAIL_APP_SENDER: Optional[str]
    MAIL_APP_PASSWORD: Optional[str]

    class Config:
        env_prefix: str = "DEV_"


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True  ## only for test environment.

    class Config:
        env_prefix: str = "TEST_"


class ProdConfig(GlobalConfig):
    class Config:
        env_prefix: str = "PROD_"


## caching - lru_cache - it will cache the keys and values based on env_state.


@lru_cache()
def get_config(env_state: str):
    configs = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
    return configs[env_state]()


config = get_config(BaseConfig().ENV_STATE)
print(">>> Using environment:", BaseConfig().ENV_STATE)
print(">>> Database URL:", config.DATABASE_URL)
# print(">>> Sender Email:", config.MAIL_APP_SENDER)
