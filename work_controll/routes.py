from flask import render_template, request, url_for, Blueprint, redirect, flash
from flask_login import  login_required, login_user, logout_user, current_user
from . import app, bcrypt, db
from work_controll.forms import RegisterForm, LoginForm
from work_controll.models import Department, User
from sqlalchemy import select, update

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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html')

@app.route('/status')
@login_required
def status():
    return render_template('status.html', title="Status")

@app.route('/reset-password', methods=['GET', 'POST'])
@login_required
def reset():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            check_pw = bcrypt.check_password_hash(user.password, form.password.data)
            if check_pw:
                new_pw_hash = bcrypt.generate_password_hash(form.new_password.data)
                db.session.query(User).filter(User.id == user.id).update({User.password: new_pw_hash})
                db.session.commit()
            else:
                flash(f'altes Passwort ist Falsch!')
                print("altes Passwort ist Falsch")
            flash(f'Das Passwort wurde erfolgreich geändert')
            return redirect(url_for('home'))
        else:
            flash(f'Es ist ein Fehler unterlaufen. Kontrolliere deine Eingaben')
            return redirect(url_for('reset'))
    return render_template('auth/reset_password.html', title="reset password", form=form)
