from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from secrets import token_hex


app = Flask(__name__)
app.config["SECRET_KEY"]="token_hex(16)" #Secret key ist für Schutz gegen CSRF
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SQLALCHEMY_TRACK_MODIFIKATONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Bitte Anmelden"
login_manager.login_message_category = 'info'

from . import routes, models

