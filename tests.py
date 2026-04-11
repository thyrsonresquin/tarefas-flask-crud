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

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert "total_tasks" in data
    assert isinstance(data["tasks"], list)
    assert data["total_tasks"] == len(data["tasks"])

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Nova tarefa de teste"
        assert data["description"] == "Descrição da tarefa de teste"
    else:
        pytest.skip("Nenhuma tarefa criada para testar")