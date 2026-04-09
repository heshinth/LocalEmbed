from fastapi import APIRouter
from fastembed import TextEmbedding
from app.api.schemas.list_models import ModelListResponse, ModelInfo, ModelType

router = APIRouter()


@router.get("/", response_model=ModelListResponse)
def list_models():
    dense_models = TextEmbedding.list_supported_models()

    data = [
        ModelInfo(
            id=m["model"],
            type=ModelType.DENSE,
            dimensions=m.get("dim"),
            description=m.get("description"),
            license=m.get("license"),
            size_in_GB=m.get("size_in_GB"),
        )
        for m in dense_models
    ]

    return ModelListResponse(object="list", data=data)
