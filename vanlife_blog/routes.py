from flask import Blueprint, render_template
from flask_login import UserMixin, login_required, LoginManager, current_user, logout_user, login_user
from vanlife_blog import app, db
from vanlife_blog.models import User, Post


# @login_manager.user_loader
# def load_user(id):
#     return User.get(int(id))


@app.route('/')
# @login_required
def home():
    return render_template("home.html")


@app.route('/blog')
# @login_required
def blog():
    return render_template("blog.html")