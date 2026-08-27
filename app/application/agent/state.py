from typing import Any, Optional, TypedDict

class AgentState(TypedDict):
    messages: list[dict[str, Any]]
    stop_reason: Optional[str]
    answer: Optional[str]
