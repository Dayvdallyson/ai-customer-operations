from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.agent.graph import build_agent_graph
from app.application.chat_service import ChatService
from app.infrastructure.db.repository import DocumentRepository
from app.infrastructure.db.session import get_db_session
from app.infrastructure.embeddings.voyage_client import VoyageEmbeddingClient
from app.infrastructure.llm.anthropic_client import AnthropicLLMClient


@lru_cache
def get_chat_service() -> ChatService:
    llm_client = AnthropicLLMClient()
    agent_graph = build_agent_graph(llm_client)
    return ChatService(agent_graph)


@lru_cache
def get_embedding_client() -> VoyageEmbeddingClient:
    return VoyageEmbeddingClient()


def get_document_repository(
    session: AsyncSession = Depends(get_db_session),
) -> DocumentRepository:
    return DocumentRepository(session)
