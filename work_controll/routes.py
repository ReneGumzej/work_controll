from distutils.log import Log
from flask import render_template, request, url_for, redirect, flash
from flask_login import  login_required, login_user, logout_user, current_user
from . import app, bcrypt, db
from work_controll.forms import RegisterForm, LoginForm, ResetPasswordForm
from work_controll.models import User
from sqlalchemy import select

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home") # die Parameter in render_template können über Jinja dem HTML template zur verfügung gestellt werden.

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() #der erste Eintrag mit der jeweiligen Email. Da sie Unique sind gibt es sowieso immer nur eine bzw. erste
        if user:
            checked_pw = bcrypt.check_password_hash(user.password, form.password.data)
            if checked_pw:
                login_user(user)
                if current_user.username == "Admin":
                    return redirect(url_for('register'))
                else:
                    return redirect(url_for('status'))

        else:
            flash(f'Login war nicht erfolgreich. Bitte überprüfe deine Email oder das Passwort', 'danger')
            return redirect(url_for('login'))
    return render_template('auth/login.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=pw_hash, department_id=form.dep.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Registrierung erfolgreich für {form.username.data}', 'succses')
        return redirect(url_for('register'))
    return render_template('auth/register.html', title="Register", form=form)

@app.route('/reset-password', methods=['GET', 'POST'])
@login_required
def reset():
    form = ResetPasswordForm()
    if form.is_submitted():
        new_hashed_pw = bcrypt.generate_password_hash(form.new_password.data)
        user = db.session.query(User).filter(User.email == form.email.data).first()
        if user:
            checked_pw = bcrypt.check_password_hash(new_hashed_pw, form.confirm_new_password.data)
            if checked_pw:
                user.password = new_hashed_pw
                db.session.commit()
                flash(f'Dein Passwort wurde geändert!', 'succses')
            else:
                flash(f'Passwörter stimmen nicht überein!', 'danger')
        else:
            flash(f'Bitte kontrolliere deine Email-Adresse!', 'danger')
    return render_template('auth/reset_password.html', title="reset password", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html')

@app.route('/status')
@login_required
def status():
    users = []
    query = 'SELECT username FROM User'
    result = db.session.execute(query)
    for u in result:
        users.append(u[0])   
    print(users)
    return render_template('status.html', title="Status", users=users)
