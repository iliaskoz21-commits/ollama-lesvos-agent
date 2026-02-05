from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_run_endpoint():
    payload = {"task": "Test AI query"}
    response = client.post("/run", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "task" in data
    assert "results" in data
    assert "saved" in data
