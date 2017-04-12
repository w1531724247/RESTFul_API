#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import db
from datetime import datetime
from flask import jsonify

class User(db.Document):
    user_id = db.StringField()
    name = db.StringField()
    phone = db.StringField()
    password = db.StringField()

    def to_dict(self):
        dict = {"name": self.name, "password": self.password, "phone": self.phone}
        return dict

    @classmethod
    def modelWithDictionary(cls, dict=None):
        name = dict["name"]
        password = dict["password"]
        phone = dict["phone"]
        user = User(name=name, password=password, phone=phone)
        return user

class Car(db.Document):
    car_id = db.StringField()
    brand = db.StringField()#品牌
    model = db.StringField()#型号
    style = db.StringField()#款式
    registerAddress = db.StringField()#注册地点
    registerTime = db.StringField()#注册时间
    divermMileage = db.StringField()#行使里程
    user_id = db.StringField()#所属的用户

class CarBrand(db.Document):
    id = db.StringField()
    brand_name = db.StringField()#品牌
    initial = db.StringField()#首字母
    update_time = db.StringField()

class CarSeries(db.Document):
    id = db.StringField()
    maker_type = db.StringField()
    series_name = db.StringField()
    series_group_name = db.StringField()
    update_time = db.StringField()

class City(db.Document):
    id = db.StringField()
    city_name = db.StringField()
    admin_code = db.StringField()
    initial = db.StringField()
    prov_id = db.StringField()
    prov_name = db.StringField()

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