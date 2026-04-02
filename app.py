from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# CRUD (create, read, update and delete - criar, ler, atualizar e deletar) - operações básicas de um banco de dados

tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    new_task = Task(id=task_id_counter, title=data['title'], description=data.get('description', ''))
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify({"message": "Nova tarefa criada com sucesso"}), 201


if __name__ == '__main__':
    app.run(debug=True)