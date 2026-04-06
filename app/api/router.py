from fastapi import APIRouter
from api.routes import embeddings_route


router = APIRouter(prefix="/v1")

router.include_router(
    embeddings_route.router, prefix="/embeddings", tags=["embeddings"]
)


# Health check endpoint
@router.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}
