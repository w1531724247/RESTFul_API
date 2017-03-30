#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
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
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)#品牌
    model = db.Column(db.String)#型号
    style = db.Column(db.String)#款式
    registerAddress = db.Column(db.String)#注册地点
    registerTime = db.Column(db.String)#注册时间
    divermMileage = db.Column(db.String)#行使里程

class CarBrand(db.Model):
    __tablename__ = 'carBrand'
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String)#品牌
    initial = db.Column(db.String)#首字母
    update_time = db.Column(db.DateTime)

class CarSeries(db.Model):
    __tablename__ = 'carSeries'
    id = db.Column(db.Integer, primary_key=True)
    series_name = db.Column(db.String)
    series_group_name = db.Column(db.String)
    update_time = db.Column(db.DateTime)

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String)
    admin_code = db.Column(db.String)
    initial = db.Column(db.String)
    prov_id = db.Column(db.String)
    prov_name = db.Column(db.String)