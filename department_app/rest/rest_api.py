"""
Rest api for app, allows to contact with db via api
"""

import datetime
import re

from flask_restful import Resource, reqparse, abort
from flask import jsonify

from department_app import api, db
import department_app.models as models

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('department', type=int)
parser.add_argument('salary', type=int)
parser.add_argument('birth_date', type=str)


class EmployeeApi(Resource):
    """
    Employee api, implements the crud interface
    """

    def get(self, employee_id):
        employee = models.Employee.query.filter(models.Employee.id == employee_id).first()
        birth_date = f"{employee.birth_date.year}-{employee.birth_date.month}-{employee.birth_date.day}"
        response = jsonify(id=employee.id,
                           name=employee.name,
                           department_id=employee.department_id,
                           salary=employee.salary,
                           birth_date=birth_date)
        response.status_code = 201
        return response

    def post(self):
        args = parser.parse_args()
        print(args)
        if not list(models.Department.query.filter(models.Department.id == args['department'])):
            abort(400)
        if args['salary'] < 0:
            abort(400)
        if re.fullmatch(re.compile(r'\d{4}-\d\d-\d\d'), args['birth_date']):  # if date like yyyy-mm-dd
            try:
                datetime.date(*map(int, str(args['birth_date']).split('-')))
            except ValueError:
                abort(400)
        else:

            abort(400)

        employee = models.Employee(
            args['name'],
            args['department'],
            args['salary'],
            args['birth_date'],
        )
        db.session.add(employee)
        db.session.commit()
        response = jsonify(message="Employee was added successfully!")
        response.status_code = 201
        return response

    def put(self, employee_id):
        args = parser.parse_args()
        employee = db.session.query(models.Employee).filter(models.Employee.id == employee_id)
        new_data = {i[0]: i[1] for i in args.items() if i[1]}  # filter out values that are not set
        employee.update(new_data, synchronize_session=False)
        db.session.commit()
        response = jsonify(message="Employee was updated successfully!")
        response.status_code = 201
        return response

    def delete(self, employee_id):
        employee = db.session.query(models.Employee).filter(models.Employee.id == employee_id)
        if not employee.first():
            abort(400)
        employee.delete()
        db.session.commit()
        response = jsonify(message="Employee was removed successfully!")
        response.status_code = 201
        return response


api.add_resource(EmployeeApi, '/employees/api', '/employees/api/<int:employee_id>')
