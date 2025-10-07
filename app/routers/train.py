from fastapi import APIRouter
from app.services.trainer import start_training
from fastapi import Form, HTTPException

router = APIRouter()

@router.post("/")
def trigger_training(
    dataset_path: str = Form(...),
    method: str = Form("lora"),
    base_model: str = Form("mistralai/Mistral-7B-v0.1"),
    epochs: int = Form(1),
    lr: float = Form(2e-4)
):
    config = {
        "dataset_path": dataset_path,
        "method": method,
        "base_model": base_model,
        "epochs": epochs,
        "lr": lr
    }

    result = start_training(config)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"status": "success", "details": result}