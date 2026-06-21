"""RAG platform tests."""

from app.services.chunker import chunk_text


def test_chunk_text_splits_with_overlap() -> None:
    text = "A" * 1000
    chunks = chunk_text(text, chunk_size=300, overlap=50)
    assert len(chunks) >= 3
    assert all(len(c) <= 300 for c in chunks)


def test_chunk_text_empty() -> None:
    assert chunk_text("") == []
    assert chunk_text("   ") == []
