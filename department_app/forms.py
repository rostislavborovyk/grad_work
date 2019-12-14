from flask_wtf import Form
from wtforms import DateField, ValidationError, StringField, IntegerField
from wtforms.validators import DataRequired, Regexp
import re


class BirthDaySearchForm(Form):
    date_from = DateField('Date from', validators=[DataRequired()])
    date_to = DateField('Date to', validators=[DataRequired()])


class AddEmployeeForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    birth_date = StringField('Birth Date', validators=[DataRequired()])


class DeleteEmployeeForm(Form):
    id = IntegerField('Id', validators=[DataRequired()])


class UpdateEmployeeForm(Form):
    name = StringField('Name', validators=[])
    department = StringField('Department', validators=[])
    salary = StringField('Salary', validators=[])
    birth_date = StringField('Birth Date', validators=[])
    id = IntegerField('Id', validators=[])
