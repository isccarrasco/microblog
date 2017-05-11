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

SQLALCHEMY_DATABASE_URI = 'postgresql://test_user:test_pass@localhost:5432/microblog'
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
