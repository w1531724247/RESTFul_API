#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import db
from datetime import datetime
from flask import jsonify

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name="", password="", phone=""):
        self.name = name
        self.phone = phone
        self.password = password
        pass

    def modelToDict(self):
        dict = {"name": self.name, "password": self.password, "phone": self.phone}
        return dict

    @classmethod
    def modelWithDictionary(cls, dict=None):
        name = dict["name"]
        password = dict["password"]
        phone = dict["phone"]
        user = User(name=name, password=password, phone=phone)
        return user

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

class ESResponse():
    code = 0
    data = None
    errorMsg = None
    def __init__(self, code=0, data=None, errorMsg=None):
        self.code = code
        self.data = data
        self.errorMsg = errorMsg
        pass

    def to_json(self):
        responseDict = {}
        responseDict["code"] = self.code

        if self.data is not None:
            responseDict["data"] = self.data
        if self.errorMsg is not None:
            responseDict["errorMsg"] = self.errorMsg

        return jsonify(responseDict)