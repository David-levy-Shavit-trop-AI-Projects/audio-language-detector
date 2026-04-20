import whisper
import tempfile
import shutil
from fastapi import UploadFile
from src.app.core.config import settings

model = whisper.load_model(settings.WHISPER_MODEL)


async def detect_language(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        shutil.copyfileobj(file.file, tmp)
        path = tmp.name

    result = model.transcribe(path)

    return {
        "language": result.get("language", "unknown"),
        "text": result.get("text", "")
    }