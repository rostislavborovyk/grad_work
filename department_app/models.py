"""
Models module, contains 2 main app models: Department, Employee
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from department_app import app
from department_app import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(30))
    employees = db.relationship('Employee', backref='department')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name})"


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50))
    department_id = db.Column('department_id', db.Integer, db.ForeignKey("department.id"))
    salary = db.Column('salary', db.Integer)
    birth_date = db.Column('birth_date', db.DATE)

    def __init__(self, name, department_id, salary, b_date):
        self.name = name
        self.department_id = department_id
        self.salary = salary
        self.birth_date = b_date

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name})"


# for migrations
if __name__ == '__main__':
    manager.run()
