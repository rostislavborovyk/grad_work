from department_app import app
from department_app import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

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


# db.create_all()
# new_employee = Employee('DineshChugtai', 3, 3500, "1983-01-20")
# db.session.add(new_employee)
# db.session.commit()

# SELECT (SELECT AVG(salary) FROM employee WHERE department = d.id) FROM department d
# for migrations
if __name__ == '__main__':
    manager.run()
    # data_query = db.session.query(Employee, Department).join(Department, Employee.department_id == Department.id).\
    #     filter(Employee.birth_date >= '2000-10-08').filter(Employee.birth_date <= '2000-10-08').\
    #     from_self(Employee.name, Department.name, Employee.salary, Employee.birth_date)
    # table_data = [i for i in data_query]
    # print(table_data)

