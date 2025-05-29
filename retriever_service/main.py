import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from retriever_service.rag import load_and_query

app = FastAPI()

@app.get("/retriever/{query}")
def get_docs(query: str):
    return load_and_query(query)
