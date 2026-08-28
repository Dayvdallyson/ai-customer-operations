from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.agent.graph import build_agent_graph
from app.application.chat_service import ChatService
from app.application.tools.document_tools import SearchDocumentsTool
from app.application.tools.order_tools import GetOrderStatusTool
from app.infrastructure.db.repository import DocumentRepository
from app.infrastructure.db.session import get_db_session
from app.infrastructure.embeddings.voyage_client import VoyageEmbeddingClient
from app.infrastructure.llm.anthropic_client import AnthropicLLMClient
from app.infrastructure.memory.redis_store import RedisConversationStore

@lru_cache
def get_embedding_client() -> VoyageEmbeddingClient:
    return VoyageEmbeddingClient()

def get_document_repository(
    session: AsyncSession = Depends(get_db_session),
) -> DocumentRepository:
    return DocumentRepository(session)

@lru_cache
def get_conversation_store() -> RedisConversationStore:
    return RedisConversationStore()

@lru_cache
def get_chat_service() -> ChatService:
    llm_client = AnthropicLLMClient()
    embedding_client = get_embedding_client()
    tools = [GetOrderStatusTool(), SearchDocumentsTool(embedding_client)]
    agent_graph = build_agent_graph(llm_client, tools)
    conversation_store = get_conversation_store()
    return ChatService(agent_graph, conversation_store)
