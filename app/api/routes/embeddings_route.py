from fastapi import APIRouter
from openai.types.embedding_create_params import EmbeddingCreateParams
from openai.types.create_embedding_response import CreateEmbeddingResponse


router = APIRouter()


@router.post("/", response_model=CreateEmbeddingResponse)
async def create_embedding(params: EmbeddingCreateParams):
    return {"testing": "tests"}
