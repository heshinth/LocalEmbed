from fastapi import APIRouter
from app.api.routes import embeddings_route, models_route


router = APIRouter(prefix="/v1")

router.include_router(
    embeddings_route.router, prefix="/embeddings", tags=["embeddings"]
)
router.include_router(models_route.router, prefix="/models", tags=["models"])


# Health check endpoint
@router.get("/health",tags=["health"])
def health_check():
    return {"status": "healthy", "message": "API is running"}
