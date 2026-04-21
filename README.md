# LocalEmbed

![GitHub License](https://img.shields.io/github/license/heshinth/LocalEmbed?cacheSeconds=20)
![Python](https://img.shields.io/badge/python-3.12-blue.svg?logo=python)
![Docker Image Version](https://img.shields.io/docker/v/heshinth/localembed?logo=docker)

A lightweight text embedding API designed as a drop-in replacement for the OpenAI embeddings endpoint. 

Built with FastAPI and `fastembed`, LocalEmbed is optimized for running local document processing and vector pipelines securely on your own infrastructure.

## Features

* **OpenAI SDK Compatible:** Natively mirrors the `/v1/embeddings` schema. Point your existing OpenAI client to `localhost` and it just works.
* **Privacy First:** 100% local execution. No data ever leaves your network.
* **Zero-Latency Starts:** Automatically pre-loads your default model into memory on server boot.
* **Container-Native:** Multi-stage Docker build utilizing `uv` for a minimal, highly optimized runtime footprint.

---

## Getting Started

### Prerequisites
- **Docker** (Recommended)
- Python 3.12+ (for local development)

### Configuration

LocalEmbed uses optional environment variables for configuration. Create a `.env` file in the root directory:

1. Copy the sample environment file from [here](./.env.sample):
   ```bash
   cp .env.sample .env
   ```
2. Open the `.env` file and set your desired configurations (like `DEFAULT_EMBEDDING_MODEL` or `HF_TOKEN`).

### Deployment (Docker)

The easiest and recommended way to run LocalEmbed is using the pre-built Docker image from Docker Hub.

#### Option 1: Docker CLI

```bash
docker run -d --pull=always --name localembed --env-file .env -p 8000:8000 heshinth/localembed:latest
```

#### Option 2: Using Docker Compose

The compose file includes environment variables directly within it.

Download the `docker-compose.yml` file from [here](./docker-compose.yml)

You can edit the file to configure it, then simply run:

```bash
docker compose up -d
```

**The API will be available at**: `http://localhost:8000`.

### Local Development

If you want to run the application natively without Docker:

1. Install the dependencies using `uv` (recommended):

   ```bash
   uv sync
   ```

2. Run the FastAPI development server:
   ```bash
   fastapi dev app/main.py
   ```

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