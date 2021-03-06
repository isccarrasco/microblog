import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_openid import OpenID
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext

from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

from .momentjs import momentjs
from .customjsonencoder import CustomJSONEncoder

# Instance of Flask
app = Flask(__name__)
app.config.from_object('config')

# Instance of SQLAlchemy and binding with Flask application
db = SQLAlchemy(app)

# Instance of LoginManager and binding with Flask app
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
lm.login_message = lazy_gettext('Please log in to access this page.')

# Instance of OpenID
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# Instance of Mail
mail = Mail(app)

# Adding momentjs
app.jinja_env.globals['momentjs'] = momentjs

# Instance of Babel
babel = Babel(app)

# Encoder for lazy_text
app.json_encoder = CustomJSONEncoder

from app import views, models


# Uncomment the line below if you run on production
if not app.debug and os.environ.get('HEROKU') is None:
# if app.debug:
    import logging

    # Uncomment this if you want yo send email on each exception

    # from logging.handlers import SMTPHandler
    
    #credentials = None
    #if MAIL_USERNAME or MAIL_PASSWORD:
    #    credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    #
    #mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    #mail_handler.setLevel(logging.ERROR)
    #app.logger.addHandler(mail_handler)
    
    
    
    from logging.handlers import RotatingFileHandler
    
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')


if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')

