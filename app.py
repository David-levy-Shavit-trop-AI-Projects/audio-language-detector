from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile
import shutil

app = FastAPI(title="Audio Language Detector")

# Load model once at startup (important for performance)
model = whisper.load_model("base")


@app.post("/detect")
async def detect_language(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        shutil.copyfileobj(file.file, tmp)
        temp_path = tmp.name

    # Run Whisper
    result = model.transcribe(temp_path)

    return {
        "language": result.get("language", "unknown"),
        "text": result.get("text", "")
    }