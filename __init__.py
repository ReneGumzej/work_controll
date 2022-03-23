from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"]="EsperA3054!" #Secret key ist für Schutz gegen CSRF
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\gumzej\\OneDrive - ESPERA-WERKE GmbH\\Dokumente\\vscode\\python\\work_controll\\site.db"
app.config['SQLALCHEMY_TRACK_MODIFIKATONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Bitte Anmelden"
login_manager.login_message_category = 'info'

from . import routes, models #relativer Pfad. "." = "work_controll" 

