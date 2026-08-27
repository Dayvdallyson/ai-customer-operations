from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from app.api.routes import chat, documents

app = FastAPI()
app.include_router(chat.router)
app.include_router(documents.router)

@app.get("/")
async def root():
  return {"message": "Hello World"}
