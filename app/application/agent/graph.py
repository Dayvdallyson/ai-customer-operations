from langgraph.graph import END, START, StateGraph

from app.application.agent.nodes import call_tool, make_agent_node, route_after_agent
from app.application.agent.state import AgentState
from app.infrastructure.llm.base import LLMClient


def build_agent_graph(llm_client: LLMClient):
    graph = StateGraph(AgentState)

    graph.add_node("agent", make_agent_node(llm_client))
    graph.add_node("call_tool", call_tool)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent", route_after_agent, {"call_tool": "call_tool", "end": END}
    )
    graph.add_edge("call_tool", "agent")

    return graph.compile()
