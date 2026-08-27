from functools import lru_cache

from app.application.agent.graph import build_agent_graph
from app.application.chat_service import ChatService
from app.infrastructure.llm.anthropic_client import AnthropicLLMClient

@lru_cache
def get_chat_service() -> ChatService:
  llm_client = AnthropicLLMClient()
  agent_graph = build_agent_graph(llm_client)
  return ChatService(agent_graph)
