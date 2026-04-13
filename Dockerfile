FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy project specification files first (for better Docker layer caching)
COPY pyproject.toml uv.lock README.md ./

# Install the project and dependencies globally in the container using uv
RUN uv sync  --locked --no-cache --no-dev --no-install-project

# Copy the rest of the application code
COPY app ./app

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]