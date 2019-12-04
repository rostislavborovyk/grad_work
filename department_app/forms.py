from flask_wtf import Form
from wtforms import DateField, ValidationError
from wtforms.validators import DataRequired


class BirthDaySearchForm(Form):
    date_from = DateField('Date from', validators=[DataRequired()])
    date_to = DateField('Date to', validators=[DataRequired()])
