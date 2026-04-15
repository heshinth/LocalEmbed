from pydantic import BaseModel
from typing import List


class CreateEmbeddingRequest(BaseModel):
    input: str | List[str]
    """Input text to embed, encoded as a string or array of strings."""

    model: str
    """ID of the model to use. See the /v1/models endpoint for a list of available models."""

    dimensions: int | None = None
    """The number of dimensions the resulting output embeddings should have."""
