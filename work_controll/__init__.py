from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"]="EsperA3054!" #Secret key ist für Schutz gegen CSRF
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFIKATONS'] = False
db = SQLAlchemy(app)

from work_controll import routes


