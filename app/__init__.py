# app/__init__.py

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
