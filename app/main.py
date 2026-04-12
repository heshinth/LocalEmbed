from fastapi import FastAPI
from app.api.router import router

description = """
**LocalEmbed** provides a high-performance, local API for text embeddings. 🚀

### Features
* **Embeddings**: Generate vectors for text using local models.
* **Models**: List supported and ready-to-use embedding models from fastembed.
* **OpenAI-Compatible API**: Drop-in replacement for OpenAI's `v1/embeddings` endpoint.
"""


app = FastAPI(
    title="LocalEmbed",
    summary="A fast, local text embedding service using fastembed.",
    description=description,
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"Project": "LocalEmbed", "description": "LocalEmbed"}


app.include_router(router)
