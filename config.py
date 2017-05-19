# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'this-is-my-super-secret-key-i-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = 'postgresql://test_user:test_pass@localhost:5432/microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '711315752236767',
        'secret': '7dc308b063b0960332a0f13f642ff974'
    },
    'twitter': {
        'id': 'sYDQZ91SinKhYDomrhx7ZzAiZ',
        'secret': 'GUwKB5Nsrn2q2VObfWxq5suQh8JmX60MgepJFfTJKofmgxR9ON'
    }
}

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'user@gmail.com'
MAIL_PASSWORD = 'pass'


# administrator list
ADMINS = ['isccarrasco@icloud.com']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = '*****' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = '*****' # enter your MS translator app secret here

SQLALCHEMY_RECORD_QUERIES = True
# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

