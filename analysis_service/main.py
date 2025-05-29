import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from analysis_service.analysis import analyze_stock

app = FastAPI()

@app.get("/analyze/{symbol}")
def analyze(symbol: str):
    return analyze_stock(symbol)