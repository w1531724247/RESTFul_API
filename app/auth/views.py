#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, json, jsonify, g
from . import auth
from ..models import User, Car, ESResponse
from .. import db
from ..tools import httpRequest
from flask_tokenauth import TokenAuth, TokenManager

secret_key = 'shanghaienshengqichefuwuyouxiangongsi'
token_auth = TokenAuth(secret_key=secret_key)
token_manager = TokenManager(secret_key=secret_key)

#获取验证码
@auth.route('/getVerifyCode')
def sendVerifyCode():
    phone = request.form['phone']
    res = httpRequest.requestVerifyCode(phone=phone)

    #{"code":200,"msg":"1","obj":"6560"}
    dict = json.loads(res)
    resCode = dict.get('code')
    if resCode == 200:
        return ESResponse(code=200, data=dict).to_json()
    else:
        return ESResponse(code=400, data=dict).to_json()

#校验验证码
@auth.route('/confirmVerifyCode')
def confirmVerifyCode():
    phone = request.form['phone']
    code = request.form['code']

    res = httpRequest.requestVerifyCode(phone=phone,code=code)
    dict = json.loads(res)
    resCode = dict.get('code')
    if resCode == 200:
        return ESResponse(code=200,data=dict).to_json()
    else:
        return False

@auth.route('/register', methods=['POST'])
def register():
    phone = request.form['phone']
    name = request.form['name']
    password = request.form['password']
    password2 = request.form['password2']

    #判断用户是否已经注册过了
    user = User.objects(phone=phone).first()
    if user is not None:
        return ESResponse(code=400, errorMsg="您已经注册过了, 请登录!").to_json()

    newUser = User(name=name, password=password, phone=phone)
    newUser.save()

    return ESResponse(code=200).to_json()

@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    phone = request.form['phone']
    password = request.form['password']

    user = User.objects(phone=phone, password=password).first()
    if user is None:
        return ESResponse(code=400, errorMsg="用户名或密码错误").to_json()
    else:
        userDict = user.to_dict()
        token = token_manager.generate(phone)

    tokenDict = {"token":token}
    return ESResponse(code=200, data=tokenDict).to_json()

@auth.route('/log_out', methods=['GET', 'POST'])
@token_auth.token_required
def log_out():
    g.current_user = None
    return ESResponse(code=200).to_json()

@auth.route('/myInfo', methods=['POST'])
@token_auth.token_required
def myInfo():
    user = g.current_user
    userDict = {"phone":g.current_user}
    return ESResponse(code=200, data=userDict).to_json()

@auth.route('/addCar', methods=['POST'])
@token_auth.token_required
def addCar():
    user = g.current_user
    car = Car(id="1", brand="奥迪", model="A6", style="2016",registerAddress="上海",registerTime="2016",divermMileage="3000")
    user.cars = car
    res = user.cars.brand

    return res

@token_auth.verify_token
def verify_token(token):
    phone = token_manager.verify(token)
    user = User.objects(phone=phone).first()
    if user is not None:
        print(user.phone)
        g.current_user = phone
        return True
    return False
