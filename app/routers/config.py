from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ModelConfig(BaseModel):
    base_model: str
    epochs: int = 3
    learning_rate: float = 5e-5
    training_type: str = "lora"  # or "rag"

current_config = {}

@router.post("/")
def set_config(config: ModelConfig):
    global current_config
    current_config = config.dict()
    return {"status": "Config saved", "config": current_config}

@router.get("/")
def get_config():
    return {"current_config": current_config}
