# Audio Language Detection Microservice

A lightweight **FastAPI microservice** for detecting the language of audio files (e.g. `.mp3`) using OpenAI Whisper.

---

## Features

* Detects spoken language from audio files
* Returns transcription + language code
* Simple REST API
* Swagger UI for easy testing

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/audio-language-detector.git
cd audio-language-detector
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

#### Activate:

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate
```

> If blocked, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**Windows (alternative):**

```powershell
.\venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install FFmpeg

#### Windows (recommended):

```powershell
winget install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
```

> If not recognized, add FFmpeg `/bin` folder to your PATH and restart terminal.

---

## Running the Service

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## Testing the API

### Option 1: Swagger UI (recommended)

Open in browser:

```
http://localhost:8000/docs
```

Upload an audio file and click **Execute**

---

### Option 2: curl

```bash
curl -X POST "http://localhost:8000/detect" \
  -F "file=@audio.mp3"
```

### Windows (PowerShell):

```powershell
curl.exe -X POST "http://localhost:8000/detect" `
  -F "file=@C:\path\to\audio.mp3"
```

---

## API Endpoints

### `POST /detect`

Upload an audio file and detect language.

#### Request:

* Content-Type: `multipart/form-data`
* Field: `file`

#### Response:

```json
{
  "language": "en",
  "text": "Hello everyone, welcome to the demo"
}
```

---

## Authors

Shavit Trop & David Levy

This project took place as part of our Bsc Computer Since studies at HIT.
