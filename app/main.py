from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.routes import chat

load_dotenv()

app = FastAPI()
app.include_router(chat.router)

@app.get("/")
async def root():
  return {"message": "Hello World"}
