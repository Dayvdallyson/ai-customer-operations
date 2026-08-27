from abc import ABC, abstractmethod

class EmbeddingClient(ABC):
  @abstractmethod
  async def embed(self, text: str, input_type: str = "document") -> list[float]:
    ...

  @abstractmethod
  async def embed_batch(self, texts: list[str], input_type: str = "document") -> list[list[float]]:
    ...
