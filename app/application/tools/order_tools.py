class GetOrderStatusTool:
  name = "get_order_status"
  description = "Get the current shipping status of a customer's order by ID."
  input_schema = {
    "type": "object",
    "properties": {
      "order_id": {"type": "string", "description": "The order ID, e.g '123'"},
    },
    "required": ["order_id"]
  }

  async def run(self, order_id: str) -> dict:
    return {"order_id": order_id, "status": "shipped"}

