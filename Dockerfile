# --- Stage 1: Build the environment ---
FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./

# We generate a standalone virtual environment
RUN uv sync --locked --no-dev --no-install-project --extra cpu

# --- Stage 2: Final Runtime Image ---
FROM python:3.12-slim-trixie

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the compiled virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv

# Copy your application code
COPY app ./app

# Add the virtual environment to PATH so it works natively
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Notice we can just run uvicorn natively since we added the venv to PATH
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]