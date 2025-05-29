import requests
from bs4 import BeautifulSoup

def get_market_news():
    url = "https://www.moneycontrol.com/news/business/markets/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    headlines = [x.text for x in soup.select('h2')][:5]
    return {"news": headlines}
