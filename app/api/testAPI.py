#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import test
from flask import render_template, request, flash, redirect, url_for, json, jsonify, g

#首页
@test.route('/')
def index():

    return "OK"