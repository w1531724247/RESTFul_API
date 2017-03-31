#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name="", password="", phone=""):
        self.name = name
        self.phone = phone
        self.password = password
        return

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)#品牌
    model = db.Column(db.String)#型号
    style = db.Column(db.String)#款式
    registerAddress = db.Column(db.String)#注册地点
    registerTime = db.Column(db.String)#注册时间
    divermMileage = db.Column(db.String)#行使里程
    user_id = db.Column(db.String)#所属的用户

class CarBrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String)#品牌
    initial = db.Column(db.String)#首字母
    update_time = db.Column(db.String)

class CarSeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maker_type = db.Column(db.String)
    series_name = db.Column(db.String)
    series_group_name = db.Column(db.String)
    update_time = db.Column(db.String)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String)
    admin_code = db.Column(db.String)
    initial = db.Column(db.String)
    prov_id = db.Column(db.String)
    prov_name = db.Column(db.String)