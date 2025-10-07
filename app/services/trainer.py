import time
import uuid
from typing import Dict
from app.services.training_methods.lora import _train_lora
from app.services.training_methods.full_finetune import _train_full_finetune 
from app.services.training_methods.rag import _train_rag

def start_training(config: Dict):
    """
    Unified training function.
    config = {
        "method": "lora",
        "dataset_path": "...",
        "base_model": "...",
        "epochs": 1,
        "lr": 2e-4
    }
    """

    method = config.get("method", "").lower()
    dataset_path = config.get("dataset_path")
    base_model = config.get("base_model", "mistralai/Mistral-7B-v0.1")
    epochs = config.get("epochs", 1)
    lr = config.get("lr", 2e-4)

    if method == "lora":
        return _train_lora(dataset_path, base_model, epochs, lr)
    elif method == "rag":
        return _train_rag(dataset_path, base_model, epochs, lr)
    elif method == "full-finetune":
        return _train_full_finetune(dataset_path, base_model, epochs, lr)
    else:
        # Method not implemented yet
        return {"error": f"Training method '{method}' is not implemented yet."}

