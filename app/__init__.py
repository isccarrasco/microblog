from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instance of Flask
app = Flask(__name__)
app.config.from_object('config')

# Instance of SQLAlchemy and binding with Flask application
db = SQLAlchemy(app)

from app import views, models

