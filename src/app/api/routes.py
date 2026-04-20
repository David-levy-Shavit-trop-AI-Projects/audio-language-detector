from fastapi import APIRouter, UploadFile, File
from src.app.services.detector_service import detect_language

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    return await detect_language(file)