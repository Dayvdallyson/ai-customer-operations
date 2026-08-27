from fastapi import APIRouter, Depends

from app.api.dependencies import get_chat_service
from app.application.chat_service import ChatService
from app.domain.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(
  request: ChatRequest,
  chat_service: ChatService = Depends(get_chat_service),
):
  answer = await chat_service.ask(request.message)
  return ChatResponse(answer=answer)
