from fastapi import APIRouter, HTTPException
from app.api.schemas.create_embedding_request import CreateEmbeddingRequest
from app.api.schemas.create_embedding_response import CreateEmbeddingResponse

from app.services.embedder import embed_text
from app.services.model_registery import validate_model_id

router = APIRouter()


@router.post("/", response_model=CreateEmbeddingResponse)
def create_embedding(params: CreateEmbeddingRequest):
    raw_input = params.input

    if isinstance(raw_input, str):
        texts = [raw_input]
    elif isinstance(raw_input, list) and all(isinstance(x, str) for x in raw_input):
        texts = raw_input
    else:
        raise HTTPException(
            status_code=400, detail="input must be a string or list of strings"
        )
    model_id = params.model
    if not validate_model_id(model_id):
        raise HTTPException(status_code=404, detail=f"Invalid model_id: {model_id}")

    vectors = [vec.tolist() for vec in embed_text(texts, model_id=model_id)]

    return {
        "object": "list",
        "data": [
            {"object": "embedding", "index": i, "embedding": v}
            for i, v in enumerate(vectors)
        ],
        "model": model_id,
        "usage": {"prompt_tokens": 0, "total_tokens": 0},
    }
