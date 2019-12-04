from . import app
from flask import render_template, redirect, url_for
from .models import db
from .forms import BirthDaySearchForm


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

    bday_search_form = BirthDaySearchForm()
    if bday_search_form.validate_on_submit():
        date_from = bday_search_form.date_from.data
        date_to = bday_search_form.date_to.data
        if (date_to - date_from).days < 0:
            return redirect(url_for('.employees'))
        data_query = db.session.execute(
            f"SELECT e.name, d.name, e.salary, e.birth_date FROM employee e "
            f"JOIN department d ON e.department_id = d.id "
            f"WHERE (e.birth_date >= \'{str(date_from)}\') AND (e.birth_date <= \'{str(date_to)}\')"
        )
    else:
        data_query = db.session.execute(
            "SELECT e.name, d.name, e.salary, e.birth_date FROM employee e"
            " JOIN department d ON e.department_id = d.id"
        )
    table_data = [[str(j) for j in i] for i in data_query.fetchall()]
    table_head.extend(table_data)
    return render_template('employees.html', table_data=table_head, form=bday_search_form)
