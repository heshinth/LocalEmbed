from fastembed import TextEmbedding

DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


def embed_text(
    text: list[str], model_id: str = DEFAULT_EMBEDDING_MODEL
) -> list[list[float]]:
    try:
        model = TextEmbedding(model_id)
    except Exception as e:
        print(f"Error initializing embedding model: {e}")
        raise
    try:
        return model.embed(text)
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        raise
