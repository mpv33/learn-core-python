"""Split text into overlapping chunks for embedding."""

from app.core.config import settings


def chunk_text(text: str, chunk_size: int | None = None, overlap: int | None = None) -> list[str]:
    """Split text into chunks with overlap to preserve context at boundaries."""
    size = chunk_size or settings.chunk_size
    ov = overlap or settings.chunk_overlap
    if not text.strip():
        return []

    chunks: list[str] = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = min(start + size, text_len)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= text_len:
            break
        start = end - ov

    return chunks
