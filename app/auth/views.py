#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, json, jsonify, g
from . import auth
from ..models import User, Car, ESResponse
from .. import db
from flask_tokenauth import TokenAuth, TokenManager
import urllib2, urllib
import time
import random
import hashlib

secret_key = 'shanghaienshengqichefuwuyouxiangongsi'
token_auth = TokenAuth(secret_key=secret_key)
token_manager = TokenManager(secret_key=secret_key)

netEasyAppkey = '92bf851a021b70338c382258f3025984'
netEasyAppSecret = '019bdb177012'

#获取验证码
@auth.route('/getVerifyCode')
def getVerifyCode():


    url = 'https://api.netease.im/sms/sendcode.action'
    params = {'mobile':'18321165691'}
    params_urlencode = urllib.urlencode(params)

    req = urllib2.Request(url=url, data=params_urlencode)
    req.add_header('AppKey', netEasyAppkey)
    curTime = str(time.time())
    req.add_header('CurTime', curTime)
    nonce = str(random.uniform(1000, 9999))
    req.add_header('Nonce', nonce)
    checkSum = hashlib.sha1(netEasyAppSecret + nonce + curTime).hexdigest()
    req.add_header('CheckSum', checkSum)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    #{"code":200,"msg":"1","obj":"6560"}
    print(res)
    return "OK"

#校验验证码
@auth.route('/confirmVerifyCode')
def confirmVerifyCode():
    url = 'https://api.netease.im/sms/verifycode.action'
    params = {'mobile':'18321165691', 'code':'6560'}
    params_urlencode = urllib.urlencode(params)

    req = urllib2.Request(url=url, data=params_urlencode)
    req.add_header('AppKey', netEasyAppkey)
    curTime = str(time.time())
    req.add_header('CurTime', curTime)
    nonce = str(random.uniform(1000, 9999))
    req.add_header('Nonce', nonce)
    checkSum = hashlib.sha1(netEasyAppSecret + nonce + curTime).hexdigest()
    req.add_header('CheckSum', checkSum)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    res_data = urllib2.urlopen(req)
    res = res_data.read()

    return "OK"

@auth.route('/register', methods=['POST'])
def register():
    parameters = request.get_data()
    dict = json.loads(parameters)

    name = dict.get('name')
    password = dict.get('password')
    password2 = dict.get('password2')
    phone = dict.get('phone')
    #判断用户是否已经注册过了
    user = User.query.filter_by(phone=phone).first()
    if user is not None:
        return ESResponse(code=400, errorMsg="您已经注册过了, 请登录!").to_json()

    newUser = User(name=name, password=password, phone=phone)
    db.session.add(newUser)
    db.session.commit()

    return ESResponse(code=200).to_json()

@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    phone = request.form['phone']
    password = request.form['password']

    user = User.query.filter_by(phone=phone, password=password).first()
    if user is None:
        return ESResponse(code=400, errorMsg="用户名或密码错误").to_json()
    else:
        userDict = user.modelToDict()
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
    user = User.query.filter_by(phone=phone).first()
    if user is not None:
        print(user.phone)
        g.current_user = phone
        return True
    return False
