import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_openid import OpenID

from config import basedir

# Instance of Flask
app = Flask(__name__)
app.config.from_object('config')

# Instance of SQLAlchemy and binding with Flask application
db = SQLAlchemy(app)

# Instance of LoginManager and binding with Flask app
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

# Instance of OpenID
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
