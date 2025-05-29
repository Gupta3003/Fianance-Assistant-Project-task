import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from fastapi import FastAPI
from api_service.utils import get_stock_data


app = FastAPI()

@app.get("/stock/{symbol}")
def fetch_stock(symbol: str):
    return get_stock_data(symbol)
