from fastapi import FastAPI
import pyttsx3

app = FastAPI()

engine = pyttsx3.init()

@app.post("/api/speak")
def speak(text: str):
    engine.say(text)
    engine.runAndWait()
    return {"status": "spoken"}