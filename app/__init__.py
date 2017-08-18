#  app/__init__.py
""" Initialization file """
from flask import Flask

APP = Flask(__name__)
APP.config['DEBUG'] = False