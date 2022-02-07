from flask import render_template, request, url_for, Blueprint, redirect, flash
from work_controll import app
from work_controll.forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

"""
@app.route('/admin-home')
def adminhome():
    return render_template('auth/admin_home.html', title="Admin Home")
"""
@app.route('/login')
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash(f'Login war erfolgreich', 'succses')
        return redirect(url_for('register'))
    return render_template('auth/login.html', title="Login", form=form)

@app.route('/admin-login', methods=['GET','POST'])
def adminlogin():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash(f'Login war erfolgreich', 'succses')
        return redirect(url_for('register'))
    return render_template('auth/admin_login.html', title="Admin Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Registrierung erfolgreich für {form.username.data}', 'succses')
        return redirect(url_for('home'))
    return render_template('auth/register.html', title="Register", form=form)

    