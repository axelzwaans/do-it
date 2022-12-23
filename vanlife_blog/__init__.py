import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from vanlife_blog import routes, auth
from vanlife_blog.models import User, Post

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))