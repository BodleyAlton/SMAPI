from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:qwert@localhost/smapi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['SECRET_KEY']= "Pinkele234!"
app.config['UPLOAD_FOLDER']= "./app/static/client-invoice"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'login'

app.config.from_object(__name__)
from app import views