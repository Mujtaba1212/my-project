from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This is your data / backend logic (you can change later)
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({"name": task, "done": False})
    return jsonify({"status": "success", "tasks": tasks})

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return jsonify({"status": "success", "tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)