#!/usr/bin/python
import os
import subprocess
import sys

subprocess.call(['virtualenv', 'flask'])
if sys.platform == 'win32':
  bin = 'Scripts'
else:
  bin = 'bin'

subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-login'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-openid'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-mail'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-sqlalchemy'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'sqlalchemy-migrate'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-whooshAlchemy'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-wtf'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flask-babel'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'guess_language'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'flipflop'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'coverage'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--upgrade', 'psycopg2'])

