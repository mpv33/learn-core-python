"""RAG pipeline — ingest documents and answer questions with citations."""

from pathlib import Path

from pypdf import PdfReader

from app.core.config import settings
from app.services.chunker import chunk_text
from app.services.embeddings import EmbeddingService
from app.services.llm_client import LLMClient
from app.services.vector_store import VectorStore

RAG_SYSTEM = """You are a company knowledge assistant.
Answer ONLY using the provided context. If the answer is not in the context, say "I don't have that information in the uploaded documents."
Cite sources using [1], [2], etc. matching the context numbers."""

PLAIN_SYSTEM = """You are a helpful assistant. Answer the user's question based on your general knowledge.
Note: you do NOT have access to private company documents in this mode."""


class RAGService:
    """Orchestrates document ingestion and RAG queries."""

    def __init__(self) -> None:
        self.embeddings = EmbeddingService()
        self.vectors = VectorStore()
        self.llm = LLMClient()
        Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)

    def ingest_file(self, filename: str, content: bytes) -> dict:
        """Save file, extract text, chunk, embed, and index."""
        doc_id = VectorStore.new_doc_id()
        save_path = Path(settings.upload_dir) / f"{doc_id}_{filename}"
        save_path.write_bytes(content)

        text = self._extract_text(filename, content)
        chunks = chunk_text(text)
        if not chunks:
            raise ValueError("No text could be extracted from the file")

        embeddings = self.embeddings.embed(chunks)
        count = self.vectors.add_chunks(doc_id, filename, chunks, embeddings)

        return {
            "doc_id": doc_id,
            "filename": filename,
            "chunks_indexed": count,
            "characters": len(text),
        }

    def query(self, question: str, use_rag: bool = True) -> dict:
        """Answer a question with optional RAG retrieval."""
        if use_rag:
            return self._rag_query(question)
        answer = self.llm.chat(PLAIN_SYSTEM, question)
        return {"answer": answer, "sources": [], "mode": "plain_llm"}

    def _rag_query(self, question: str) -> dict:
        query_embedding = self.embeddings.embed([question])[0]
        sources = self.vectors.search(query_embedding)

        if not sources:
            return {
                "answer": "No documents indexed yet. Please upload company documents first.",
                "sources": [],
                "mode": "rag",
            }

        context = "\n\n".join(f"[{i + 1}] (from {s['filename']})\n{s['text']}" for i, s in enumerate(sources))
        user_prompt = f"Context:\n{context}\n\nQuestion: {question}"
        answer = self.llm.chat(RAG_SYSTEM, user_prompt)

        return {"answer": answer, "sources": sources, "mode": "rag"}

    def list_documents(self) -> list[dict]:
        return self.vectors.list_documents()

    def delete_document(self, doc_id: str) -> None:
        self.vectors.delete_document(doc_id)

    @staticmethod
    def _extract_text(filename: str, content: bytes) -> str:
        lower = filename.lower()
        if lower.endswith(".pdf"):
            import io
            reader = PdfReader(io.BytesIO(content))
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        return content.decode("utf-8", errors="ignore")
