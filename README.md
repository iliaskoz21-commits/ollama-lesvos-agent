# Ollama Lesvos Autonomous AI Agent

Autonomous Web Research Agent for real estate listings in Lesvos, Greece.

This project demonstrates a professional AI agent workflow:

- **Local LLM**: Mistral via Ollama
- **Web search**: DuckDuckGo for real-time online results
- **Memory**: Short-term session memory
- **Structured outputs**: JSON
- **API endpoint**: FastAPI for integration
- **Demo script**: `test.py` for local testing

Perfect as a **portfolio project** to showcase skills in Python, LLMs, and building autonomous AI agents.

---

## Features

1. **Autonomous search agent**
2. **Structured JSON output**
3. **Tool calling** (search + save)
4. **Short-term memory**
5. **FastAPI endpoint for integration**
6. **Offline LLM, online web search**
7. **Demo script** for quick testing

---

## Installation

```bash
# Clone repository
git clone https://github.com/iliaskoz21-commits/ollama-lesvos-agent.git
cd ollama-lesvos-agent

# Create virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows CMD
.venv\Scripts\activate.bat
# Mac / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
