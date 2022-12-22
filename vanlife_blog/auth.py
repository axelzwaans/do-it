from flask import Blueprint, render_template, request, flash, redirect, url_for
from vanlife_blog import app, db
from vanlife_blog.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', 'success')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Password is incorrect.', 'error')
        else:
            flash('Email does not exist', 'error')

    return render_template('login.html', user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()

        if email_exists:
            flash('This email address is already in use.', 'error')
        elif len(email) < 4:
            flash('Please enter a valid email address.', 'error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters', 'error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 characters', 'error')
        elif password != password2:
            flash('Passwords must match', 'error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', 'error')
        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created', 'success')
            return redirect(url_for('home'))

    return render_template("register.html", user=current_user)


@app.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))