from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """Config environment settings"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    HF_API_KEY: SecretStr | None = None
    """Hugging Face API key. Optional"""

    DEFAULT_EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"
    """The default embedding model to use."""


settings = Settings()
