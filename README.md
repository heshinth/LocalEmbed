# LocalEmbed

![GitHub License](https://img.shields.io/github/license/heshinth/LocalEmbed?cacheSeconds=20)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)

A fast and simple local API for generating text embeddings.

## Features
- Generate text embeddings locally without external API dependencies.
- List available embedding models.
- Containerized with Docker for easy deployment.

## Getting Started

### Prerequisites
- Docker (Recommended)
- Python 3.12+ (for local development)

### Using Docker (Recommended)

The easiest and recommended way to run LocalEmbed is using the pre-built Docker image from Docker Hub.

```bash
docker run -d --name localembed -p 8000:8000 heshinth/localembed:latest
```
The API will be available at `http://localhost:8000`.

### Running Locally (Development)

1. Install the dependencies:
   ```bash
   uv sync # or your preferred method based on pyproject.toml
   ```

2. Run the FastAPI development server:
   ```bash
   fastapi dev app/main.py
   ```

### Building the Docker image manually

```bash
docker build -t localembed .
docker run -p 8000:8000 localembed
```

## Supported Models

LocalEmbed uses `fastembed` under the hood and supports all of its text embedding models out of the box. You can find the full list of supported dense models in the [FastEmbed Documentation](https://qdrant.github.io/fastembed/examples/Supported_Models/).

## API Endpoints

- `GET /v1/health` — Health check
- `POST /v1/embeddings` — Generate text embeddings using local models (OpenAI API compatible)
- `GET /v1/models` — List supported and ready-to-use embedding models

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