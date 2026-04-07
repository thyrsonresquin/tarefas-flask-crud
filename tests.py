import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    payload = {
        "title": "Nova tarefa de teste",
        "description": "Descrição da tarefa de teste"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Nova tarefa criada com sucesso"
    assert "id" in response.json()
    tasks.append(response.json()["id"])