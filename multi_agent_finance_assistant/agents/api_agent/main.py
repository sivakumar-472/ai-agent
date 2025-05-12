from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/api/market_data")
def get_market_data(ticker: str = "TSM"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2d")
    if hist.empty:
        return {"error": "No data found"}
    return {
        "latest_close": hist["Close"].iloc[-1],
        "previous_close": hist["Close"].iloc[-2]
    }