# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI(
    title="Lesvos Autonomous AI Agent (Ollama)",
    description="Offline Ollama agent + online DuckDuckGo search",
    version="1.0.0"
)

# ----------------------------
# Request / Response models
# ----------------------------
class AgentRequest(BaseModel):
    task: str

class AgentResponse(BaseModel):
    task: str
    results: str
    saved: str

# ----------------------------
# API endpoint
# ----------------------------
@app.post("/run", response_model=AgentResponse)
def run(request: AgentRequest):
    return run_agent(request.task)
