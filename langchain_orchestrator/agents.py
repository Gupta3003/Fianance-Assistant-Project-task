import requests

def orchestrate_response(symbol):
    stock = requests.get(f"http://localhost:8000/stock/{symbol}").json()
    if "error" in stock:
        return {"brief": f"Stock API error: {stock['error']}"}

    news = requests.get("http://localhost:8001/news").json()
    analysis = requests.get(f"http://localhost:8003/analyze/{symbol}").json()

    combined = f"Stock Data: {stock}\nNews: {news['news']}\nAnalysis: {analysis['analysis']}"
    return {"brief": combined}
