import os

import voyageai

from app.infrastructure.embeddings.base import EmbeddingClient

class VoyageEmbeddingClient(EmbeddingClient):
  def __init__(self, model: str = "voyage-3"):
    self._client = voyageai.AsyncClient(api_key=os.environ["VOYAGE_API_KEY"])
    self._model = model

  async def embed(self, text: str, input_type: str = "document") -> list[float]:
    result = await self._client.embed([text], model=self._model, input_type=input_type)
    return result.embeddings[0]

  async def embed_batch(self, texts: list[str], input_type: str = "document") -> list[list[float]]:
    result = await self._client.embed(texts, model=self._model, input_type=input_type)
    return result.embeddings
