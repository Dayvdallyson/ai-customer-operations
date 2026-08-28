from app.infrastructure.db.repository import DocumentRepository
from app.infrastructure.db.session import async_session_factory
from app.infrastructure.embeddings.base import EmbeddingClient

class SearchDocumentsTool:
  name = "search_documents"
  description = "Search the knowledge base for documents relevant to a query."
  input_schema = {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "what to search for."}
    },
    "required": ["query"],
  }

  def __init__(self, embedding_client: EmbeddingClient):
    self._embedding_client = embedding_client

  async def run(self, query: str) -> dict:
    query_embedding = await self._embedding_client.embed(query, input_type="query")

    async with async_session_factory() as session:
      repository = DocumentRepository(session)
      documents = await repository.search(query_embedding, limit=5)

    return {"results": [{"id": doc.id, "content": doc.content} for doc in documents]}

  
