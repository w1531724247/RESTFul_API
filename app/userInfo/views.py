from flask import render_template, request, flash, redirect, url_for
from . import userInfo
from ..models import User
from .. import db

@userInfo.route('/')
def index():
    return "Hello userInfo"

@userInfo.route('/register', methods=['GET', 'POST'])
def register():
    name = request.form['name']

    return request.args['name']

@userInfo.route('/all', methods=['GET', 'POST'])
def show_all():
    users = User.query.all()
    lfc = users[1]
    return 'name:' + lfc.name + 'password:' + lfc.password