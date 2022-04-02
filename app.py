from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.todolist import todolist
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(todolist)
