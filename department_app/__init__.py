"""
Setup for project
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import pymysql

app = Flask(__name__)

app.config.from_object('department_app.config.DevelopmentConfig')
# installing driver
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

# flask restful api
api = Api(app)
