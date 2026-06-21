"""Document upload and management."""

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas import DocumentInfo, IngestResponse
from app.services.rag_service import RAGService

router = APIRouter(prefix="/documents", tags=["Documents"])

ALLOWED = {".txt", ".md", ".pdf"}


@router.post("/upload", response_model=IngestResponse)
async def upload_document(file: UploadFile = File(...)) -> IngestResponse:
    """Upload and index a document into the vector store."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename required")
    ext = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ALLOWED:
        raise HTTPException(status_code=400, detail=f"Allowed types: {', '.join(ALLOWED)}")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        result = RAGService().ingest_file(file.filename, content)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    return IngestResponse(**result)


@router.get("", response_model=list[DocumentInfo])
def list_documents() -> list[DocumentInfo]:
    docs = RAGService().list_documents()
    return [DocumentInfo(**d) for d in docs]


@router.delete("/{doc_id}", status_code=204)
def delete_document(doc_id: str) -> None:
    RAGService().delete_document(doc_id)
