from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "da3f071810a37f4d8984a3fca56014fe18f40a02"
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///site.db"
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes