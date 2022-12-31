from flask import render_template, request, flash, redirect, url_for
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
                flash('You are logged in', 'success')
                login_user(user, remember=True)
                return redirect(url_for('dashboard'))
            else:
                flash('Password is incorrect', 'error')
        else:
            flash('Email does not exist', 'error')

    return render_template('login.html', user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('This email address is already in use', 'error')
        elif username_exists:
            flash('This username is already taken', 'error')
        elif len(email) < 4:
            flash('Please enter a valid email address', 'error')
        elif len(username) < 2:
            flash('Username must be greater than 1 characters', 'error')
        elif password != password2:
            flash('Passwords must match', 'error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', 'error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created', 'success')
            return redirect(url_for('dashboard'))

    return render_template("register.html", user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))