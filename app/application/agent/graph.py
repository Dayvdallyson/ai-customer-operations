from langgraph.graph import END, START, StateGraph

from app.application.agent.nodes import make_agent_node, make_call_tool_node, route_after_agent
from app.application.agent.state import AgentState
from app.infrastructure.llm.base import LLMClient

def build_agent_graph(llm_client: LLMClient, tools: list):
  graph = StateGraph(AgentState)

  graph.add_node("agent", make_agent_node(llm_client, tools))
  graph.add_node("call_tool", make_call_tool_node(tools))

  graph.add_edge(START, "agent")
  graph.add_conditional_edges(
    "agent", route_after_agent, {"call_tool": "call_tool", "end": END}
  )
  graph.add_edge("call_tool", "agent")

  return graph.compile()
