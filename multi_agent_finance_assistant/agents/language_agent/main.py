from fastapi import FastAPI

app = FastAPI()

@app.post("/api/narrate")
def narrate(payload: dict):
    exposure = payload.get("exposure", "unknown")
    earnings = payload.get("earnings", [])
    summary = f"Asia tech allocation is {exposure}. "
    summary += " ".join(earnings)
    return {"narrative": summary}