# Multi-Agent Finance Assistant

## Project Overview

This project builds a **multi-source, multi-agent finance assistant** delivering spoken market briefs via a Streamlit app. It ingests financial data from APIs, web scraping, and document loaders, indexes embeddings in a vector store for Retrieval-Augmented Generation (RAG), and orchestrates specialized AI agents via FastAPI microservices.

### Use Case: Morning Market Brief

Every trading day at 8 AM, the assistant verbally summarizes your risk exposure and earnings surprises:

> “Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields.”

---

## Architecture

### Agent Roles and Responsibilities

| Agent            | Role                                                        | Description                                         |
|------------------|-------------------------------------------------------------|----------------------------------------------------|
| **API Agent**    | Polls real-time and historical market data                  | Calls AlphaVantage and Yahoo Finance APIs          |
| **Scraping Agent**| Crawls filings and financial documents                       | Uses Python loaders and scraping tools             |
| **Retriever Agent**| Indexes embeddings in FAISS or Pinecone and retrieves top-k relevant chunks | Vector search microservice                           |
| **Analysis Agent** | Performs quantitative analysis, risk metrics, and highlights| Custom analytics engine                              |
| **Language Agent** | Synthesizes natural language market briefs using LLM via LangGraph or CrewAI | Narrative generation and prompt orchestration       |
| **Voice Agent**    | Handles speech-to-text (Whisper), LLM query, and text-to-speech (TTS) pipelines | Manages voice input/output pipeline                  |

### System Workflow

Voice input → STT (Whisper) → Orchestrator → Retrieval & Analysis → LLM → TTS → Spoken response

Fallbacks prompt user clarification via voice if retrieval confidence is low.

---

## Project Structure

```
/finance-assistant
│
├── /data_ingestion/          # Scripts for API polling, web scraping, document loaders
├── /agents/                  # Microservices: API, scraping, retrieval, analysis, language, voice
├── /orchestrator/            # Service to route and manage inter-agent communication
├── /streamlit_app/           # Streamlit frontend UI with voice & text interface
├── /docs/                    # Documentation & AI tool usage logs
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

### Python Files and Descriptions

| File/Folder               | Purpose                                          |
|--------------------------|-------------------------------------------------|
| `/agents/api_agent.py`     | Polls market data from AlphaVantage, Yahoo      |
| `/agents/scraping_agent.py`| Scrapes financial filings and documents          |
| `/agents/retriever_agent.py`| Manages vector store indexing and retrieval       |
| `/agents/analysis_agent.py`| Runs quantitative market analytics                |
| `/agents/language_agent.py`| Generates natural language summaries              |
| `/agents/voice_agent.py`   | Manages speech recognition and TTS                |
| `/data_ingestion/`         | Helper scripts for API calls and scraping          |
| `/orchestrator/app.py`     | Orchestrates agent interactions and routing       |
| `/streamlit_app/app.py`    | Frontend app: voice/text interaction UI            |

---

## Technologies Used

| Category            | Tools & Frameworks                                  |
|---------------------|----------------------------------------------------|
| Backend Framework   | FastAPI (for microservices)                         |
| Vector Store        | FAISS / Pinecone                                   |
| LLM Orchestration   | LangGraph, CrewAI, LangChain (any chosen framework)|
| Speech Recognition  | Whisper (open-source STT)                          |
| Text-to-Speech      | Coqui TTS, pyttsx3, or other open-source TTS      |
| Web Scraping        | Python loaders, BeautifulSoup, alternative MCPs    |
| Frontend            | Streamlit                                          |
| Containerization    | Docker                                             |
| Data Sources        | AlphaVantage API, Yahoo Finance API                |

---

## Setup & Installation

### Prerequisites

- Python 3.9 or higher
- Docker (optional but recommended)
- API keys for AlphaVantage / Yahoo Finance

### Installation Steps

```bash
git clone https://github.com/yourusername/finance-assistant.git
cd finance-assistant

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env` file with your API keys:

```env
ALPHAVANTAGE_API_KEY=your_api_key_here
YAHOO_FINANCE_API_KEY=your_api_key_here
```

---

## Running Microservices

Start each agent service in separate terminals:

```bash
uvicorn agents.api_agent:app --host 0.0.0.0 --port 8001 --reload
uvicorn agents.scraping_agent:app --host 0.0.0.0 --port 8002 --reload
uvicorn agents.retriever_agent:app --host 0.0.0.0 --port 8003 --reload
uvicorn agents.analysis_agent:app --host 0.0.0.0 --port 8004 --reload
uvicorn agents.language_agent:app --host 0.0.0.0 --port 8005 --reload
uvicorn agents.voice_agent:app --host 0.0.0.0 --port 8006 --reload
```

Start the orchestrator:

```bash
uvicorn orchestrator.app:app --host 0.0.0.0 --port 8000 --reload
```

Launch the Streamlit frontend:

```bash
streamlit run streamlit_app/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Frontend Interface

### Screenshots

| Market Brief Example                  |
|--------------------------------------|
|![Screenshot (966)](https://github.com/user-attachments/assets/3ef9c042-2fd4-42e1-9d50-1078d40555b5)|


### Demo Video

[https://github.com/user-attachments/assets/d8f84034-7a30-4384-a0d3-75e3b8265d3](https://github.com/user-attachments/assets/298ebf0a-0d66-46f8-b548-e18b1f89be8f)

---

## Deployment

Build and run using Docker:

```bash
docker build -t finance-assistant .
docker run -p 8501:8501 finance-assistant
```

You can deploy on platforms like:

- Streamlit Cloud
- Heroku
- AWS ECS/EKS
- Azure App Services

---

## Documentation

- `/docs/ai_tool_usage.md` — AI prompt logs, code generation steps, model configs
- `/docs/architecture/` — System diagrams (UML, flowcharts)
- `/docs/performance/` — Benchmarks and evaluation metrics

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

---

## License

This project is licensed under the MIT License.
