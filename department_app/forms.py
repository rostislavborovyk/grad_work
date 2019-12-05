from flask_wtf import Form
from wtforms import DateField, ValidationError, StringField
from wtforms.validators import DataRequired


class BirthDaySearchForm(Form):
    date_from = DateField('Date from', validators=[DataRequired()])
    date_to = DateField('Date to', validators=[DataRequired()])


class AddEmployeeForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    birth_date = StringField('Birth Date', validators=[DataRequired()])
