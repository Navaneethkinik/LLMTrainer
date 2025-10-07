from fastapi import APIRouter
from app.services.train import start_training

router = APIRouter()

@router.post("/")
def trigger_training():
    """Kick off model fine-tuning (mock for now)."""
    job_id = start_training()
    return {"status": "Training started", "job_id": job_id}
