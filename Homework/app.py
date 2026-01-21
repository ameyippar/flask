from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

def get_next_id():
    return max(task['id'] for task in TASKS) + 1 if TASKS else 1


@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'id': get_next_id(),
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority']
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)


@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))


@app.route('/update/<int:id>')
def update_task(id):
    for task in TASKS:
        if task['id'] == id:
            task['status'] = 'Completed'
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
