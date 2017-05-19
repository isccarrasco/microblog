i#!flask/bin/python
import os

os.environ['DATABASE_URL'] = 'postgresql://test_user:test_pass@localhost:5432/microblog'

from flipflop import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app).run()

