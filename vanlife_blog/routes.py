from flask import Blueprint, render_template
from flask_login import login_required, current_user
from vanlife_blog import app, db
from vanlife_blog.models import User, Post


@app.route('/')
# @login_required
def home():
    return render_template("home.html", user=current_user)