# agent.py
import os
import json
from datetime import datetime
from langchain_community.chat_models import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun

# ----------------------------
# 1. Local LLM (Ollama)
# ----------------------------
llm = ChatOllama(
    model="mistral",
    temperature=0.3,
    base_url="http://localhost:11434"
)

# ----------------------------
# 2. Search Tool
# ----------------------------
search_tool = DuckDuckGoSearchRun()

# ----------------------------
# 3. Save results function
# ----------------------------
def save_result(content, filename="data/results.json") -> str:
    os.makedirs("data", exist_ok=True)
    record = {
        "timestamp": datetime.now().isoformat(),
        "content": content
    }
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return "Results saved locally"

# ----------------------------
# 4. Short-term memory (session)
# ----------------------------
memory = []

# ----------------------------
# 5. Public agent function
# ----------------------------
def run_agent(task: str) -> dict:
    # Προσθήκη task στη μνήμη
    memory.append({"role": "user", "content": task})

    # Εκτέλεση αναζήτησης
    search_results = search_tool.run(task)

    # Αποθήκευση αποτελεσμάτων
    save_status = save_result(search_results)

    # Προσθήκη αποτελεσμάτων στη μνήμη
    memory.append({"role": "agent", "content": search_results})

    # Επιστροφή structured JSON
    return {
        "task": task,
        "results": search_results,
        "saved": save_status
    }
