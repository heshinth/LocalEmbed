from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
from app.logger import setup_logger
from app.api.router import router

from app.services.embedder import preload_default_model

description = """
**LocalEmbed** provides a high-performance, local API for text embeddings. 🚀

### Features
* **Embeddings**: Generate vectors for text using local models.
* **Models**: List supported and ready-to-use embedding models from fastembed.
* **OpenAI-Compatible API**: Drop-in replacement for OpenAI's `v1/embeddings` endpoint.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks.
    setup_logger()
    logger.info("Starting up LocalEmbed API...")
    try:
        preload_default_model()
    except Exception as e:
        logger.error(f"Failed to preload models: {e}")
    yield
    # Perform any shutdown tasks here (e.g., clean up resources)
    logger.info("Shutting down LocalEmbed API...")


app = FastAPI(
    title="LocalEmbed",
    summary="A fast, local text embedding service using fastembed.",
    description=description,
    version="0.1.3",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {
        "Project": "LocalEmbed",
        "description": "A lightweight text embedding API designed as a drop-in replacement for the OpenAI embeddings endpoint. ",
    }


app.include_router(router)
