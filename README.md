# LocalEmbed

![GitHub License](https://img.shields.io/github/license/heshinth/LocalEmbed?cacheSeconds=20)
![Python](https://img.shields.io/badge/python-3.12-blue.svg?logo=python)
![Docker Image Version](https://img.shields.io/docker/v/heshinth/localembed?logo=docker)
![Docker Pulls](https://img.shields.io/docker/pulls/heshinth/localembed?logo=docker)


A lightweight text embedding API designed as a drop-in replacement for the OpenAI embeddings endpoint. 

Built with FastAPI and `fastembed`, LocalEmbed is optimized for running local document processing and vector pipelines securely on your own infrastructure.

## Features

* **OpenAI SDK Compatible:** Natively mirrors the `/v1/embeddings` schema. Point your existing OpenAI client to `localhost` and it just works.
* **Privacy First:** 100% local execution. No data ever leaves your network.
* **Zero-Latency Starts:** Automatically pre-loads your default model into memory on server boot.
* **Container-Native:** Multi-stage Docker build utilizing `uv` for a minimal, highly optimized runtime footprint.
* **CPU + GPU Ready:** Published Docker images for both CPU (`latest`) and NVIDIA GPU (`latest-gpu`) deployments.

---

## Getting Started

### Prerequisites
- **Docker** (Recommended)
- **For GPU deployment:** NVIDIA GPU + drivers + NVIDIA Container Toolkit
- Python 3.12+ (for local development)

### Configuration

LocalEmbed uses optional environment variables for configuration. Create a `.env` file in the root directory:

1. Copy the sample environment file from [here](./.env.sample):
   ```bash
   cp .env.sample .env
   ```
2. Open the `.env` file and set your desired configurations (like `DEFAULT_EMBEDDING_MODEL` or `HF_TOKEN`).

Environment variables:

- `DEFAULT_EMBEDDING_MODEL`: model to preload on startup
- `HF_TOKEN`: optional, useful to avoid model download rate limits
- `MODEL_CACHE_LIMIT`: max number of models kept in memory (LRU eviction)
- `EMBEDDING_THREADS`: CPU threads for embedding computation
- `BATCH_SIZE`: number of inputs processed per batch
- `USE_GPU`: set `true` to force CUDA provider in local/non-GPU-image runs

### Deployment (Docker)

The easiest and recommended way to run LocalEmbed is using the pre-built Docker image from Docker Hub.

#### Option 1: Docker CLI (CPU)

```bash
docker run -d --pull=always --name localembed --env-file .env -p 8000:8000 heshinth/localembed:latest
```

#### Option 2: Docker CLI (GPU)

```bash
docker run -d --pull=always --gpus all --name localembed-gpu --env-file .env -p 8000:8000 heshinth/localembed:latest-gpu
```

#### Option 3: Docker Compose (CPU)

The compose file includes environment variables directly within it.

Download the `docker-compose.yml` file from [here](./docker-compose.yml)

You can edit the file to configure it, then simply run:

```bash
docker compose up -d
```

#### Option 4: Docker Compose (GPU)

Download the `docker-compose.gpu.yml` file from [here](./docker-compose.gpu.yml), then run:

```bash
docker compose -f docker-compose.gpu.yml up -d
```

### Docker Tag Scheme

For a release tag like `v0.1.3`, published image tags are:

- CPU: `latest`, `0.1.3`, `0.1`
- GPU: `latest-gpu`, `0.1.3-gpu`, `0.1-gpu`

**The API will be available at**: `http://localhost:8000/v1`.

### Local Development

If you want to run the application natively without Docker:

1. Install dependencies for CPU mode:

   ```bash
   uv sync --extra cpu
   ```

2. Run the FastAPI development server:

   ```bash
   fastapi dev app/main.py
   ```

For local GPU mode:

1. Install dependencies for GPU mode:

   ```bash
   uv sync --extra gpu
   ```

2. Start with GPU provider enabled:

   ```bash
   USE_GPU=true fastapi dev app/main.py
   ```
---
## API Endpoints

- `GET /v1/health` — Health check
- `POST /v1/embeddings` — Generate text embeddings using local models (OpenAI API compatible)
- `GET /v1/models` — List supported and ready-to-use embedding models

## Supported Models

LocalEmbed supports all dense text embedding models provided by `fastembed`.

You can view the full list of supported models in the [FastEmbed Documentation](https://qdrant.github.io/fastembed/examples/Supported_Models/), or programmatically query your running instance via the API:

```http
GET http://localhost:8000/v1/models
```

## Usage with OpenAI SDK

Since the `/v1/embeddings` endpoint is OpenAI API compatible, you can easily use the official `openai` Python package to interact with it just like the real OpenAI API:

```python
from openai import OpenAI

# Initialize the client pointing to the local base URL
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="sk-no-key-required"
)

# Generate an embedding
response = client.embeddings.create(
    input=["Hello, world!"],
    model="BAAI/bge-small-en-v1.5"  # Replace with any supported model
)

print(response.data[0].embedding)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
