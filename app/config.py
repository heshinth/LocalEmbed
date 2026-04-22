from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """Config environment settings"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    HF_TOKEN: SecretStr | None = None
    """Hugging Face API token. Optional"""

    DEFAULT_EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"
    """The default embedding model to use."""

    EMBEDDING_THREADS: int = 8
    """Number of threads to use for embedding generation. Adjust based on your CPU capabilities."""

    BATCH_SIZE: int = 256
    """Batch size for embedding generation. Adjust based on your system's memory and performance."""


settings = Settings()
