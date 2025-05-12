from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/api/brief")
def market_brief():
    aum = 10000000
    asia_tech_percent = 22
    previous_percent = 18

    analysis = requests.get("http://localhost:8003/api/analyze", params={
        "aum": aum,
        "asia_tech_percent": asia_tech_percent,
        "previous_percent": previous_percent
    }).json()

    earnings = [
        "TSMC beat estimates by 4%",
        "Samsung missed by 2%"
    ]

    narrative = requests.post("http://localhost:8004/api/narrate", json={
        "exposure": analysis["aum_exposure"],
        "earnings": earnings
    }).json()

    requests.post("http://localhost:8005/api/speak", params={"text": narrative["narrative"]})

    return {"narrative": narrative["narrative"]}