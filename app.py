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
    task_id_counter += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        return jsonify(task.to_dict())
    else:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    
'''
@app.route('/user/<username>')
def show_user_profile(username):
    return f'Perfil do usuário: {username}'
'''



if __name__ == '__main__':
    app.run(debug=True)