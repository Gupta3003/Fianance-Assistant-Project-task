import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from fastapi import FastAPI
from langchain_orchestrator.agents import orchestrate_response

app = FastAPI()

@app.get("/orchestrate/{symbol}")
def orchestrate(symbol: str):
    return orchestrate_response(symbol)
