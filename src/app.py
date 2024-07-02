from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# Global Variable
todos = [
    {"label": "My firts task", "done": False},
    {"label": "My second task", "done": False}
]

# Get Todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Post Todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Inconming request with the following body", request_body)
    if request_body.get("label") is None or request_body.get("done") is None:
        return jsonify({"Message": "Error, label is required"}), 400
    todos.append(request_body)
    return jsonify(todos), 200

# Delete todo
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    if 0 <= position < len(todos):
        todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3245, debug=True)