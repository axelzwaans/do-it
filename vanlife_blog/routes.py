from flask import Blueprint, render_template
from flask_login import login_required, current_user
from vanlife_blog import app, db

routes = Blueprint('routes', __name__)


@routes.route('/')
@login_required
def home():
    return render_template("home.html", name=current_user.username)


@routes.route('/create')
def create():
    return render_template("create.html")