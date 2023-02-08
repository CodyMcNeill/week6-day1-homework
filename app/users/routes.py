from flask import render_template, request, redirect, url_for, Blueprint, flash
from .forms import registrationForm, loginForm, editForm
from ..models import User, db
from flask_login import login_user, logout_user, current_user, login_required

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def registerUserPage():
    form = registrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.username.data
            password = form.password.data
            # print(username, email, password)
            #adding user to DB
            user = User(username, email, password)
            user.saveToDB()
            return redirect(url_for('users.loginUserPage'))
    return render_template('register.html', form = form)

@users.route('/login', methods=['GET', 'POST'])
def loginUserPage():
    form = loginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if user.password == password:
                    login_user(user)
                    flash(f'You have successfully logged in!')
                    return redirect(url_for('main.homePage'))
                else:
                    flash(f'Wrong Password')
                    return render_template('login.html', form = form)
        else:
            flash(f'User does not exist')
            return render_template('login.html', form = form)               
    return render_template('login.html', form = form)

@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logoutUserPage():
        logout_user()
        flash(f'Succesfully logged out!')
        return redirect(url_for('main.homePage'))
            

@users.route('/profile', methods=['GET', 'POST'])
@login_required
def profilePage():
    form = editForm()
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.currentPassword.data == user.password:
                newPassword = form.confirm_password.data
                user.password = newPassword
                user.saveToDB()
            else:
                flash('Wrong password, please try again')
    return render_template('profile.html', form=form)