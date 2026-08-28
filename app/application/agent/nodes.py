from app.application.agent.state import AgentState
from app.application.tools.registry import get_tool_schemas
from app.infrastructure.llm.base import LLMClient

def make_agent_node(llm_client: LLMClient, tools: list):
    tool_schemas = get_tool_schemas(tools)

    async def agent(state: AgentState) -> AgentState:
        response = await llm_client.create_message(
            messages=state["messages"], tools=tool_schemas
        )
        state["stop_reason"] = response.stop_reason

        content = [block.model_dump() for block in response.content]
        state["messages"].append({"role": "assistant", "content": content})

        if response.stop_reason != "tool_use":
            state["answer"] = "".join(
                block["text"] for block in content if block["type"] == "text"
            )
        return state
    return agent

def make_call_tool_node(tools: list):
    tool_map = {tool.name: tool for tool in tools}

    async def call_tool(state: AgentState) -> AgentState:
        last_message = state["messages"][-1]
        tool_results = []

        for block in last_message["content"]:
            if block["type"] == "tool_use":
                tool = tool_map[block["name"]]
                result = await tool.run(**block["input"])
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block["id"], "content": str(result)}
                )

        state["messages"].append({"role": "user", "content": tool_results})
        return state
    return call_tool

def route_after_agent(state: AgentState) -> str:
    return "call_tool" if state["stop_reason"] == "tool_use" else "end"
