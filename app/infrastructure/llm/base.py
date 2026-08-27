from abc import ABC, abstractmethod
from typing import Any

class LLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        ...

    @abstractmethod
    async def create_message(
        self, messages: list[dict[str, Any]], tools: list[dict[str, Any]] | None = None
    ) -> Any:
        """Returns the raw provider response so the caller can inspect
           stop_reason and content blocks - needed for tool-calling loops.
        """
