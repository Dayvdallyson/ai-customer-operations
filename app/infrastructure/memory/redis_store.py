import json
import os

from redis.asyncio import Redis

from app.infrastructure.memory.base import ConversationStore

class RedisConversationStore(ConversationStore):
    def __init__(self, ttl_seconds: int = 3600):
        self._client = Redis.from_url(os.environ["REDIS_URL"])
        self._ttl = ttl_seconds

    async def get_messages(self, session_id: str) -> list[dict]:
        raw = await self._client.get(f"conversation:{session_id}")
        return json.loads(raw) if raw else []

    async def save_messages(self, session_id: str, messages: list[dict]) -> None:
        await self._client.set(
            f"conversation:{session_id}", json.dumps(messages), ex=self._ttl
        )
