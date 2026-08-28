from app.application.agent.state import AgentState
from app.infrastructure.memory.base import ConversationStore

class ChatService:
    def __init__(self, agent_graph, conversation_store: ConversationStore):
        self._agent_graph = agent_graph
        self._conversation_store = conversation_store

    async def ask(self, session_id: str, message: str) -> str:
        history = await self._conversation_store.get_messages(session_id)
        history.append({"role": "user", "content": message})

        initial_state: AgentState = {
            "messages": history,
            "stop_reason": None,
            "answer": None,
        }
        final_state = await self._agent_graph.ainvoke(initial_state)

        await self._conversation_store.save_messages(session_id, final_state["messages"])
        return final_state["answer"]
