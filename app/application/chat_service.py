from app.infrastructure.llm.base import LLMClient

class ChatService:
  def __init__(self, llm_client: LLMClient):
    self._llm_client = llm_client

  async def ask(self, message: str) -> str:
    return await self._llm_client.generate(message)
