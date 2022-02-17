from flask import render_template, request, url_for, Blueprint, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user
from . import app, bcrypt, db, login_manager
from work_controll.forms import RegisterForm, LoginForm
from work_controll.models import Department, User

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home") # die Parameter in render_template können über Jinja dem HTML template zur verfügung gestellt werden.

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first() #der erste Eintrag mit der jeweiligen Email. Da sie Unique sind gibt es sowieso immer nur eine bzw. erste
        checked_pw = bcrypt.check_password_hash(user.password, form.password.data)
        if user and checked_pw:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        flash(f'Login war erfolgreich', 'succses')
        return redirect(url_for('register'))
    else:
        flash(f'Login war nicht erfolgreich. Bitte überprüfe deine Email oder das Passwort', 'danger')
    return render_template('auth/login.html', title="Login", form=form)

@app.route('/admin-login', methods=['GET','POST'])
def adminlogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first() #der erste Eintrag mit der jeweiligen Email. Da sie Unique sind gibt es sowieso immer nur eine bzw. erste
        checked_pw = bcrypt.check_password_hash(user.password, form.password.data)
        if user and checked_pw:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        flash(f'Login war erfolgreich', 'succses')
        return redirect(url_for('register'))
    else:
        flash(f'Login war nicht erfolgreich. Bitte überprüfe deine Email oder das Passwort', 'danger')
    return render_template('auth/admin_login.html', title="Admin Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=pw_hash, department=form.department.data)
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