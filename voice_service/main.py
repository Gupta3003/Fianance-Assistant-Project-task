import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, UploadFile, File
from voice_service.stt import transcribe
from voice_service.tts import speak

app = FastAPI()

@app.post("/voice")
async def voice(file: UploadFile = File(...)):
    try:
        path = f"/tmp/{file.filename}"
        with open(path, "wb") as f:
            f.write(await file.read())

        text = transcribe(path)
        if not text:
            return {"error": "Transcription failed or returned empty."}

        speak(f"Transcribed: {text}")
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
  
