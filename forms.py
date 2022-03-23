
from flask_wtf import FlaskForm
from numpy import integer
from wtforms import  StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from work_controll.models import User


class RegisterForm(FlaskForm):
    
    DEP_CHOISES = [("", ""),(2, "CC-Technical"), (3, "CC-Commercial"), (4, "Dev-Software")]

    username = StringField('Benutzername',validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    dep = SelectField('Abteilung', choices=DEP_CHOISES)
    password = PasswordField('Passwort', validators=[DataRequired()])
    confirm_password = PasswordField('Passwort bestätigen',
                                     validators=[DataRequired(), EqualTo('password')])
    new_password = PasswordField('Neues Passwort', validators=[DataRequired()])
    confirm_new_password = PasswordField('Neues Passwort bestätigen',
                                     validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Registrieren')
    submit_reset = SubmitField('Passwort ändern')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Dieser Benutzername ist vergeben. Wähle einen anderen.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Diese Email ist vergeben. Wähle einen andere.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Login')