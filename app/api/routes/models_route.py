from fastapi import APIRouter
from app.api.schemas.list_models import ModelListResponse
from app.services.model_registery import get_dense_models

router = APIRouter()


@router.get("/", response_model=ModelListResponse)
def list_models():
    dense_model_data = get_dense_models()

    return ModelListResponse(object="list", data=dense_model_data)
