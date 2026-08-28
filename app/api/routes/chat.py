from uuid import uuid4

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.dependencies import get_chat_service
from app.application.chat_service import ChatService

router = APIRouter()

class ChatRequest(BaseModel):
  message: str
  session_id: str | None = None

class ChatResponse(BaseModel):
  answer: str
  session_id: str

@router.post("/chat", response_model=ChatResponse)
async def chat(
  request: ChatRequest,
  chat_service: ChatService = Depends(get_chat_service)
) -> ChatResponse:
  session_id = request.session_id or str(uuid4())
  answer = await chat_service.ask(session_id, request.message)
  return ChatResponse(answer=answer, session_id=session_id)
