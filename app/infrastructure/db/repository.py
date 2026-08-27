from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models import Document

class DocumentRepository:
  def __init__(self, session: AsyncSession):
    self._session = session

  async def add(self, content: str, embedding: list[float]) -> Document:
    document = Document(content=content, embedding=embedding)
    self._session.add(document)
    await self._session.commit()
    await self._session.refresh(document)
    return document

  async def search(self, query_embedding: list[float], limit: int = 5) -> list[Document]:
    stmt = (
      select(Document)
      .order_by(Document.embedding.cosine_distance(query_embedding))
      .limit(limit)
    )
    result = await self._session.execute(stmt)
    return list(result.scalars().all())
