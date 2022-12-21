import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env
# from os import path
# from flask_migrate import Migrate
# from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'secret_key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#     db.init_app(app)
#     migrate = Migrate(app, db)
#     from .routes import routes
#     from .auth import auth

#     app.register_blueprint(routes, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')

#     from .models import User

#     login_manager = LoginManager()
#     login_manager.login_view = "auth.login"
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     return app


# def create_database(app):
#     if not path.exists("vanlife_blog/" + DB_NAME):
#         with app.app_context():
#             db.create_all()
#             print("Created database!")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from vanlife_blog import routes