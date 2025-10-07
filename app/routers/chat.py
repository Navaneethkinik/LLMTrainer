from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat_with_model(req: ChatRequest):
    """Mock chat endpoint (will later connect to real model)."""
    user_input = req.message
    response = f"Echo: {user_input} (This will be model output later)"
    return {"response": response}
