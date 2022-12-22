from vanlife_blog import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(1000))
    lastName = db.Column(db.String(1000))
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

