from work_controll import db
from enum import unique
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Department(db.Model):
    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), unique=True, nullable=False)
    user = relationship('User', backref='department', lazy=True)
    
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    department_id = db.Column(db.Integer, ForeignKey('department.id'), nullable=False)

"""
ForeignKey Fehler:
sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class User->user'. Original exception was:
Could not determine join condition between parent/child tables on relationship User.department - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.
"""