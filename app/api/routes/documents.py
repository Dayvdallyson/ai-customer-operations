from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.dependencies import get_document_repository, get_embedding_client
from app.infrastructure.db.repository import DocumentRepository
from app.infrastructure.embeddings.base import EmbeddingClient

router = APIRouter()

class IngestRequest(BaseModel):
  content: str

class IngestResponse(BaseModel):
  id: int
  content: str


@router.post("/documents", response_model=IngestResponse)
async def ingest_document(
  request: IngestRequest,
  embedding_client: EmbeddingClient = Depends(get_embedding_client),
  repository: DocumentRepository = Depends(get_document_repository),
) -> IngestResponse:
  embedding = await embedding_client.embed(request.content, input_type="document")
  document = await repository.add(request.content, embedding)
  return IngestResponse(id=document.id, content=document.content)
