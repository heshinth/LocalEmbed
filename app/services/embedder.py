from typing import Iterable
from pydantic import BaseModel
from fastembed import TextEmbedding

DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


class EmbeddingResult(BaseModel):
    vectors: list[list[float]]
    prompt_tokens: int
    model_used: str


def embed_text(
    texts: Iterable[str] | str, model_id: str = DEFAULT_EMBEDDING_MODEL
) -> EmbeddingResult:
    try:
        model = TextEmbedding(model_id)
    except Exception as e:
        print(f"Error initializing embedding model: {e}")
        raise

    try:
        # model.embed natively batches an iterable of documents giving an iterable of numpy arrays
        vectors = [vec.tolist() for vec in model.embed(texts)]

        # token_count returns an iterator of ints (tokens per document), so we sum them
        total_tokens = sum(model.token_count(texts))

        return EmbeddingResult(vectors=vectors, prompt_tokens=total_tokens, model_used=model_id)
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        raise
