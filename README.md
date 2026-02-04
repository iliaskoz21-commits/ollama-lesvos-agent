# Ollama Lesvos Autonomous AI Agent

**Autonomous Web Research Agent** for real estate listings in Lesvos, Greece.

- **Local LLM:** Mistral via Ollama
- **Agent architecture:** Python functions + short-term memory
- **Web search:** DuckDuckGoSearchRun (online)
- **Memory:** Short-term session memory
- **API:** FastAPI with JSON output
- **Storage:** Results saved locally as JSON

---

## Features

1. **Autonomous search agent**
2. **Structured JSON output**
3. **Tool calling** (search + save)
4. **Short-term memory**
5. **FastAPI endpoint for integration**
6. **Offline LLM, online web search**

---

## Installation

```bash
# Clone repository
git clone https://github.com/<username>/ollama-lesvos-agent.git
cd ollama-lesvos-agent

# Create virtual environment
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Mac / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
