#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import base
from ..models import City
from .. import db, login_manager
from flask_login import current_user, login_required
import os

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

