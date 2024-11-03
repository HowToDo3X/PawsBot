from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    USE_REF: bool = True
    REF_ID: str = 'RrbBYTPa'

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [5, 80]

    SLEEP_TIME_IN_MINUTES: list[int] = [60 * 20, 60 * 24]

    ENABLE_AUTO_TASKS: bool = True
    UNSAFE_ENABLE_JOIN_TG_CHANNELS: bool = False # NOT RECOMMENDED

    DISABLE_IN_NIGHT: bool = False
    NIGHT_TIME: list[int] = [23, 6]

    BOOSTS_BLACK_LIST: list[str] = []
    TASKS_TODO_LIST: list[str] = []

    USE_PROXY_FROM_FILE: bool = True

    MAX_RETRIES: int = 3

    ENABLE_SSL: bool = False

settings = Settings()


