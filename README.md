# Lesvos Autonomous AI Agent (Ollama)

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101-green)
![Build](https://img.shields.io/github/workflow/status/iliaskoz21-commits/ollama-lesvos-agent/CI)

## Quick Intro
Offline **Ollama LLM** + online **DuckDuckGo search** AI agent for tasks and question answering.

- FastAPI backend
- Main file: `app.py`
- Agent logic: `agent.py`
- Version: 1.0.0

---

## Demo

```bash
curl -X POST "http://localhost:8000/run" -H "Content-Type: application/json" -d "{\"task\": \"Find restaurants in Lesvos\"}"
Example response:

{
  "task": "Find restaurants in Lesvos",
  "results": "...",
  "saved": "..."
}
Installation & Run
Locally (Python)
git clone https://github.com/iliaskoz21-commits/ollama-lesvos-agent.git
cd ollama-lesvos-agent
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app:app --reload
Open in browser: http://localhost:8000/docs

Docker
docker build -t ollama-lesvos-agent .
docker run -p 8000:8000 ollama-lesvos-agent
Open in browser: http://localhost:8000/docs

Quick API
Method	Path	Request	Response
POST	/run	{ "task": "..." }	{ "task": "...", "results": "...", "saved": "..." }
Deployment / Cloud (Optional)
Run online via:

Fly.io

Render

Railway

AWS ECS / Fargate

💡 Tip: Use environment variables for API keys or agent configs.

Technologies
Python 3.11 | FastAPI | Ollama | Pydantic | Docker | Pytest