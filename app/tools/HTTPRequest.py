#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2, urllib, time, random, hashlib
from flask import json

class HTTPRequest():
    netEasyAppkey = '92bf851a021b70338c382258f3025984'
    netEasyAppSecret = '019bdb177012'

    def requestVerifyCode(self, phone=None):
        if phone is None:
            return False
        url = 'https://api.netease.im/sms/sendcode.action'
        params = {'mobile':phone}
        params_urlencode = urllib.urlencode(params)

        req = urllib2.Request(url=url, data=params_urlencode)
        req.add_header('AppKey', self.netEasyAppkey)
        curTime = str(time.time())
        req.add_header('CurTime', curTime)
        nonce = str(random.uniform(1000, 9999))
        req.add_header('Nonce', nonce)
        checkSum = hashlib.sha1(self.netEasyAppSecret + nonce + curTime).hexdigest()
        req.add_header('CheckSum', checkSum)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')

        res_data = urllib2.urlopen(req)
        res = res_data.read()

        return res

    def confirmVerifyCode(self,phone=None, code=None):
        if phone is None:
            return False
        elif code is None:
            return False

        url = 'https://api.netease.im/sms/verifycode.action'
        params = {'mobile':phone, 'code':code}
        params_urlencode = urllib.urlencode(params)

        req = urllib2.Request(url=url, data=params_urlencode)
        req.add_header('AppKey', self.netEasyAppkey)
        curTime = str(time.time())
        req.add_header('CurTime', curTime)
        nonce = str(random.uniform(1000, 9999))
        req.add_header('Nonce', nonce)
        checkSum = hashlib.sha1(self.netEasyAppSecret + nonce + curTime).hexdigest()
        req.add_header('CheckSum', checkSum)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        res_data = urllib2.urlopen(req)
        res = res_data.read()

        return res