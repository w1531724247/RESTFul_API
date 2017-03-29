from . import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name="", password="", email=""):
        self.email = email
        self.name = name
        self.password = password
        return

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

