from functools import lru_cache

from app.application.chat_service import ChatService
from app.infrastructure.llm.anthropic_client import AnthropicLLMClient

@lru_cache
def get_chat_service() -> ChatService:
  llm_client = AnthropicLLMClient()
  return ChatService(llm_client)


