"""Simple persistent vector store (JSON) — no heavy deps; swap for Chroma/Pinecone in production."""

import json
import math
from pathlib import Path
from uuid import uuid4

from app.core.config import settings


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


class VectorStore:
    """Store chunk embeddings and run similarity search."""

    def __init__(self) -> None:
        self._path = Path(settings.chroma_persist_dir) / "vectors.json"
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._items: list[dict] = self._load()

    def _load(self) -> list[dict]:
        if self._path.exists():
            return json.loads(self._path.read_text())
        return []

    def _save(self) -> None:
        self._path.write_text(json.dumps(self._items))

    def add_chunks(
        self,
        doc_id: str,
        filename: str,
        chunks: list[str],
        embeddings: list[list[float]],
    ) -> int:
        for i, (text, emb) in enumerate(zip(chunks, embeddings)):
            self._items.append({
                "id": f"{doc_id}_{i}",
                "doc_id": doc_id,
                "filename": filename,
                "chunk_index": i,
                "text": text,
                "embedding": emb,
            })
        self._save()
        return len(chunks)

    def search(self, query_embedding: list[float], top_k: int | None = None) -> list[dict]:
        k = top_k or settings.top_k
        if not self._items:
            return []
        scored = [
            {
                "text": item["text"],
                "filename": item["filename"],
                "doc_id": item["doc_id"],
                "chunk_index": item["chunk_index"],
                "score": round(_cosine(query_embedding, item["embedding"]), 4),
            }
            for item in self._items
        ]
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:k]

    def delete_document(self, doc_id: str) -> None:
        self._items = [i for i in self._items if i["doc_id"] != doc_id]
        self._save()

    def list_documents(self) -> list[dict]:
        seen: dict[str, dict] = {}
        for item in self._items:
            doc_id = item["doc_id"]
            if doc_id not in seen:
                seen[doc_id] = {"doc_id": doc_id, "filename": item["filename"]}
        return list(seen.values())

    @staticmethod
    def new_doc_id() -> str:
        return str(uuid4())
