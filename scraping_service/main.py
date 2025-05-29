import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from scraping_service.scraper import get_market_news

app = FastAPI()

@app.get("/news")
def get_news():
    return get_market_news()
