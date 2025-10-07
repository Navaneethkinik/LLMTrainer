from fastapi import APIRouter, File, UploadFile, HTTPException
import os
import logging
from app.services.data_processor import process_uploaded_file

# Initialize router
router = APIRouter()

# Setup upload directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)

@router.post("/")
async def upload_data(file: UploadFile = File(...)):
    """
    Upload and process a training file (PDF, DOCX, TXT).
    """
    logger.info(f"Received file upload request: {file.filename}")

    # Validate file type
    allowed_extensions = {".pdf", ".docx", ".txt"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_extensions:
        logger.warning(f"Unsupported file type: {file.filename}")
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}'. Allowed: {', '.join(allowed_extensions)}",
        )

    # Save file
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(filepath, "wb") as f:
            content = await file.read()
            f.write(content)
        logger.info(f"File saved successfully: {filepath} ({len(content)} bytes)")
    except Exception as e:
        logger.error(f"Error saving file {file.filename}: {e}")
        raise HTTPException(status_code=500, detail="Failed to save uploaded file")

    # Process file
    try:
        processed_data = process_uploaded_file(filepath)
        logger.info(f"File processed successfully: {file.filename}, chunks={len(processed_data)}")
        return {"filename": file.filename, "chunks": len(processed_data)}
    except Exception as e:
        logger.exception(f"Error processing file {file.filename}: {e}")
        # Clean up file if processing fails
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Removed file after processing failure: {filepath}")
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")
