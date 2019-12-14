from . import app
from flask import render_template, redirect, url_for
from .models import db, Department, Employee
from .forms import BirthDaySearchForm, AddEmployeeForm, DeleteEmployeeForm, UpdateEmployeeForm
import requests


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
        data_query = db.session.query(Employee, Department)\
            .join(Department, Employee.department_id == Department.id)\
            .filter(Employee.birth_date >= str(date_from)).filter(Employee.birth_date <= str(date_to))\
            .from_self(Employee.name, Department.name, Employee.salary, Employee.birth_date)
        table_data = [i for i in data_query]

    else:
        data_query = db.session.execute(
            "SELECT e.name, d.name, e.salary, e.birth_date FROM employee e"
            " JOIN department d ON e.department_id = d.id"
        )
        table_data = [[str(j) for j in i] for i in data_query.fetchall()]
    table_head.extend(table_data)
    return render_template('employees/employees.html', table_data=table_head, form=bday_search_form)


@app.route('/add_employee', methods=['POST', 'GET'])
def add_employee():
    add_employee_form = AddEmployeeForm()
    if add_employee_form.validate_on_submit():
        name = add_employee_form.name.data
        birth_date = add_employee_form.birth_date.data
        department = add_employee_form.department.data
        salary = add_employee_form.salary.data
        data = {"name": name, "department": department, "salary": salary, "birth_date": birth_date}
        response = requests.post(url="http://localhost:5000/employees/api", json=data)
        if response.status_code == 400:
            return render_template('employees/add_employee.html', form=add_employee_form, invalid_data=True)
        return redirect(url_for('employees'))
    return render_template('employees/add_employee.html', form=add_employee_form)


@app.route('/delete_employee', methods=['POST', 'GET'])
def delete_employee():
    delete_employee_form = DeleteEmployeeForm()
    if delete_employee_form.validate_on_submit():
        employee_id = delete_employee_form.id.data
        response = requests.delete(f"http://localhost:5000/employees/api/{employee_id}")
        if response.status_code == 400:
            return render_template('employees/delete_employee.html', form=delete_employee_form,
                                   invalid_data=True)
        return redirect(url_for('employees'))

    return render_template('employees/delete_employee.html', form=delete_employee_form)


@app.route('/update_employee', methods=['POST', 'GET'])
def update_employee():
    update_employee_form = UpdateEmployeeForm()
    if update_employee_form.validate_on_submit():
        data = {
            "name": update_employee_form.name.data,
            "department": update_employee_form.department.data,
            "salary": update_employee_form.salary.data,
            "birth_date": update_employee_form.birth_date.data
        }
        filtered_data = {i[0]: i[1] for i in data.items() if i[1]}  # filter out values that are not set
        response = requests.put(f"http://localhost:5000/employees/api/{update_employee_form.id.data}",
                                data=filtered_data)
        if response.status_code == 400:
            return render_template('employees/update_employee.html', form=update_employee_form,
                                   invalid_data=True)
        return redirect(url_for('employees'))
    return render_template('employees/update_employee.html', form=update_employee_form)
