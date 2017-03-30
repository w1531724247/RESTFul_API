#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import base
from ..models import City, Car, CarBrand, CarSeries
from ..tools import cww_crawler
from .. import db, login_manager
from flask_login import current_user, login_required
import os, urllib, urllib2


projectDir = os.getcwd()

@base.route('/province_list', methods=['GET'])
def province_list():
    return

@base.route('/init_city', methods=['GET'])
def init_city():
    filePath = projectDir + "/resource/Insure_getAllCity.json"
    jsonFile = open(filePath)
    jsonObj = json.loads(jsonFile.read())
    city_list = jsonObj.get('city_list')
    count = 0
    for index in range(0, len(city_list)):
        dict = city_list[index]
        admin_code = dict.get('admin_code')
        city_id = dict.get('city_id')
        city_name = dict.get('city_name')
        initial = dict.get('initial')
        prov_id = dict.get('prov_id')
        prov_name = dict.get('prov_name')

        city = City(id=city_id,city_name=city_name,initial=initial,admin_code=admin_code,prov_id=prov_id,prov_name=prov_name)
        db.session.add(city)
        count += 1

    db.session.commit()
    return jsonify(count)

@base.route('/delete_allCity', methods=['GET'])
def delete_allCity():
    citys = City.query.all()
    for obj in citys:
        db.session.delete(obj)
    db.session.commit()
    return "Delete all!"

@base.route('/allCity', methods=['GET'])
def allCity():
    citys = City.query.all()
    dicts = []
    for model in citys:
        dict = {}
        dict['city_name'] = model.city_name
        dict['admin_code'] = model.admin_code
        dict['id'] = model.id
        dict['initial'] = model.initial
        dict['prov_id'] = model.prov_id
        dict['prov_name'] = model.prov_name
        dicts.append(dict)

    return jsonify(dicts)

@base.route('/init_cars', methods=['GET'])
def init_cars():
    filePath = projectDir + "/resource/Insure_getCarBrandList.json"
    jsonFile = open(filePath)
    jsonObj = json.loads(jsonFile.read())
    car_list = jsonObj.get('brand_list')
    count = 0
    for index in range(0, len(car_list)):
        car_brand = car_list[index]
        brand_id = car_brand.get('brand_id')
        brand_name = car_brand.get('brand_name')
        initial = car_brand.get('initial')
        update_time = car_brand.get('update_time')

        brand = CarBrand(id=brand_id, brand_name=brand_name,initial=initial,update_time=update_time)
        db.session.add(brand)
        count += 1

    db.session.commit()
    return jsonify(count)

@base.route('/init_serise', methods=['GET'])
def init_serise():
    brandArray = CarBrand.query.all()
    count = 0
    for brand in brandArray:
        brandid = str(brand.id)
        res = cww_crawler.cheWaWaCarSeriseList(brandid=brandid)
        jsonObj = json.loads(res)
        series_list = jsonObj.get('series_list')
        for ser in series_list:
            maker_type = ser.get('maker_type')
            series_group_name = ser.get('series_group_name')
            series_id = ser.get('series_id')
            series_name = ser.get('series_name')
            update_time = ser.get('update_time')

            car_ser = CarSeries(id=series_id, series_name=series_name,update_time=update_time,series_group_name=series_group_name,maker_type=maker_type)
            db.session.add(car_ser)
            count += 1

        db.session.commit()
    return jsonify(count)

@base.route('/getOther', methods=['GET'])
def getOther():
    res = cww_crawler.cheWaWaCarSeriseList(brandid='6')
    return res