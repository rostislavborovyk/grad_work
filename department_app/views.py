from . import app
from flask import render_template
from .models import db


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/departments', methods=['GET', 'POST'])
def departments():
    table_head = [("Department name", "Number of employees", "Average salary")]
    data_query = db.session.execute(
        "SELECT d.name, (SELECT COUNT(*) FROM employee e WHERE e.department_id = d.id),"
        " (SELECT AVG(e.salary) FROM employee e WHERE e.department_id = d.id) FROM department d"
    )
    table_data = [[str(j) for j in i] for i in data_query.fetchall()]
    table_head.extend(table_data)

    return render_template('departments.html', table_data=table_head)


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    table_head = [("Name", "Department", "Salary", "Birth date")]
    data_query = db.session.execute(
        "SELECT e.name, d.name, e.salary, e.birth_date FROM employee e"
        " JOIN department d ON e.department_id = d.id"
    )
    table_data = [[str(j) for j in i] for i in data_query.fetchall()]
    table_head.extend(table_data)
    return render_template('employees.html', table_data=table_head)
