from app.application.agent.state import AgentState

class ChatService:
    def __init__(self, agent_graph):
        self._agent_graph = agent_graph

    async def ask(self, message: str) -> str:
        initial_state: AgentState = {
            "messages": [{"role": "user", "content": message}],
            "stop_reason": None,
            "answer": None,
        }
        final_state = await self._agent_graph.ainvoke(initial_state)
        return final_state["answer"]
