from fastapi import FastAPI

app = FastAPI()

@app.get("/api/analyze")
def analyze(aum: float, asia_tech_percent: float, previous_percent: float):
    delta = asia_tech_percent - previous_percent
    return {
        "aum_exposure": f"{asia_tech_percent}% of AUM",
        "change": f"up from {previous_percent}%",
        "delta": delta
    }