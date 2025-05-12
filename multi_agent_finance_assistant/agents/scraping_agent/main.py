from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/api/filings")
def get_filings(url: str = "https://www.sec.gov/edgar/browse/"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [tag.get_text() for tag in soup.find_all("h4")]
    return {"filings": titles[:5]}