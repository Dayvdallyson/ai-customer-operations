from anthropic import AsyncAnthropic

from app.infrastructure.llm.base import LLMClient

class AnthropicLLMClient(LLMClient):
  def __init__(self, model: str = "claude-haiku-4-5-20251001", max_tokens: int = 500):
      self._client = AsyncAnthropic()
      self._model = model
      self._max_tokens = max_tokens

  async def generate(self, prompt: str) -> str:
     response = await self._client.messages.create(
        model=self._model,
        max_tokens=self._max_tokens,
        messages=[{"role": "user", "content": prompt}]
     )
     return response.content[0].text
