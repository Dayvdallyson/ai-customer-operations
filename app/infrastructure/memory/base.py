from abc import ABC, abstractmethod

class ConversationStore(ABC):
    @abstractmethod
    async def get_messages(self, session_id: str) -> list[dict]:
        ...

    @abstractmethod
    async def save_messages(self, session_id: str, messages: list[dict]) -> None:
        ...
