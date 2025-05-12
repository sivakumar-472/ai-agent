# Data ingestion: Load and preprocess data

# agents/scraping_agent/loader.py

import requests
from bs4 import BeautifulSoup


def scrape_financial_news(url="https://www.cnbc.com/technology/"):
    """
    Scrapes top technology-related financial news headlines from CNBC or any finance source.

    Args:
        url (str): URL to scrape financial news from.

    Returns:
        List[str]: A list of cleaned headlines.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []
        for item in soup.find_all("a", class_="LatestNews-headline"):
            text = item.get_text(strip=True)
            if text:
                headlines.append(text)

        return headlines or ["No headlines found."]
    except Exception as e:
        return [f"Scraping error: {str(e)}"]


if __name__ == "__main__":
    # For testing purposes
    scraped_data = scrape_financial_news()
    print("Top Financial News Headlines:")
    for headline in scraped_data:
        print("-", headline)

