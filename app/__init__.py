from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views

app = Flask(__name__)

db = SQLAlchemy(app)