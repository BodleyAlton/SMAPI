from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:qwert@localhost/smapi"
db = SQLAlchemy(app)
