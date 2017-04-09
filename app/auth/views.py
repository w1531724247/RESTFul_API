#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import auth
from ..models import User, Car
from .. import db, login_manager
from flask_login import login_user, logout_user, current_user, login_required

@auth.route('/register', methods=['POST'])
def register():
    parameters = request.get_data()
    dict = json.loads(parameters)

    name = dict.get('name')
    password = dict.get('password')
    password2 = dict.get('password2')
    phone = dict.get('phone')
    #判断用户是否已经注册过了
    user = User.query.filter_by(name=name).first()
    if user is not None:
        return u"您已经注册过了!请登录!"

    newUser = User(name=name, password=password, phone=phone)
    db.session.add(newUser)
    db.session.commit()

    return "register"

@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    # parameters = request.get_data()
    name = request.form['name']#dict.get('name')
    password = request.form['password']#dict.get('password')

    user = User.query.filter_by(name=name, password=password).first()
    login_user(user)
    response = {"name": user.name, "password": user.password, "phone": user.phone}

    return jsonify(response)

@auth.route('/log_out', methods=['GET', 'POST'])
def log_out():
    logout_user()
    return "log_out"

@auth.route('/myInfo', methods=['POST'])
@login_required
def myInfo():
    user = current_user
    response = {"name": user.name, "password": user.password, "phone": user.phone}
    return jsonify(response)

@auth.route('/addCar', methods=['POST'])
@login_required
def addCar():
    user = current_user
    car = Car(id="1", brand="奥迪", model="A6", style="2016",registerAddress="上海",registerTime="2016",divermMileage="3000")
    user.cars = car
    res = user.cars.brand

    return res