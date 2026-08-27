from app.application.tools.order_tools import GetOrderStatusTool

AVAILABLE_TOOLS = [GetOrderStatusTool()]
TOOL_MAP = {tool.name: tool for tool in AVAILABLE_TOOLS}


def get_tool_schemas() -> list[dict]:
    return [
        {"name": t.name, "description": t.description, "input_schema": t.input_schema}
        for t in AVAILABLE_TOOLS
    ]
