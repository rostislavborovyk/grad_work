from department_app import api, db
from flask_restful import Resource, reqparse, abort
from flask import jsonify
from department_app.models import Employee, Department
import re
import datetime

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('department', type=int)
parser.add_argument('salary', type=int)
parser.add_argument('birth_date', type=str)


class EmployeeApi(Resource):
    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        if not list(Department.query.filter(Department.id == args['department'])):
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

        employee = Employee(
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

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(EmployeeApi, '/employees/api')
