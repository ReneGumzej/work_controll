from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(users):
    print(User.query.get(int(users)))
    return User.query.get(int(users))

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref='department')
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)