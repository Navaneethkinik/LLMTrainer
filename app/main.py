from fastapi import FastAPI
from app.routers import upload, config, train, chat

app = FastAPI(title="LLM Trainer POC", version="0.1")

# Include routers
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(config.router, prefix="/config", tags=["Model Config"])
app.include_router(train.router, prefix="/train", tags=["Training"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "Welcome to LLM Trainer POC"}
