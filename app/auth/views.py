#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import auth
from ..models import User
from .. import db, login_manager
from flask_login import login_user, logout_user, current_user, login_required

@auth.route('/register', methods=['POST'])
def register():
    parameters = request.get_data()
    dict = json.loads(parameters)

    name = dict.get('name')
    password = dict.get('password')
    password2 = dict.get('password2')
    email = dict.get('email')
    #判断用户是否已经注册过了
    user = User.query.filter_by(name=name).first()
    if user is not None:
        return u"您已经注册过了!请登录!"

    newUser = User(name=name, password=password, email=email)
    db.session.add(newUser)
    db.session.commit()

    return "register"

@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    parameters = request.get_data()
    dict = json.loads(parameters)

    name = dict.get('name')
    password = dict.get('password')

    user = User.query.filter_by(name=name, password=password).first()
    login_user(user)
    return "log_in: " + user.name

@auth.route('/log_out', methods=['GET', 'POST'])
def log_out():
    logout_user()
    return "log_out"

@auth.route('/myInfo', methods=['POST'])
@login_required
def myInfo():
    user = current_user
    response = {"name": user.name, "password": user.password, "email": user.email}
    return jsonify(response)