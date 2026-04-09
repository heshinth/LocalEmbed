from pydantic import BaseModel
from enum import Enum
from typing import Literal


class ModelType(str, Enum):
    DENSE = "Dense Text Embedding"
    SPARSE = "Sparse Text Embedding"
    RERANK = "Rerank Cross Encoder"


class ModelInfo(BaseModel):
    id: str
    """The model identifier, which can be referenced in the API endpoints."""

    type: ModelType
    """The type of the model, e.g., 'Dense embedding'."""

    dimensions: int | None = None
    """The dimensionality of the embedding vectors produced by the model."""

    description: str | None = None
    """A brief description of the model and its intended use cases."""

    license: str
    """The license under which the model is released."""

    size_in_GB: float
    """The size of the model in gigabytes."""


class ModelListResponse(BaseModel):
    object: Literal["list"]
    """Indicates that the response is a list of models."""

    data: list[ModelInfo]
    """A list of model information objects."""
