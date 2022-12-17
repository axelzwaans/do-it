from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return redirect(url_for('routes.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash('This email address is already in use.', 'error')
        elif username_exists:
            flash('This Username is already in use.', 'error')
        elif len(email) < 4:
            flash('Please enter a valid email address.', 'error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters', 'error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 characters', 'error')
        elif password1 != password2:
            flash('Passwords must match', 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', 'error')
        else:
            new_user = User(email=email, username=username, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Success', 'success')
            return redirect(url_for('views.home'))

    return render_template("register.html")

