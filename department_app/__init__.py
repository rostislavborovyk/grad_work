from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config.from_pyfile('config.py')

# installing driver
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

