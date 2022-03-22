from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'c9f4f657596e6bf5f7734b2612364239'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
login_manager.login_message = 'Para acessar essa página, faça login na sua conta ou cadastre-se'


from comunidadeimpressionadora import routes