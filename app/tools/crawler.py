#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib, urllib2

class Crawler():
    def cheWaWaCarSeriseList(self, brandid=''):
        #POST请求
        url = 'http://api.chewawa.com.cn/myapi/Insure_getCarSeriesList'
        params = {'brandid':brandid}
        params_urlencode = urllib.urlencode(params)
        req = urllib2.Request(url=url, data=params_urlencode)

        res_data = urllib2.urlopen(req)
        res = res_data.read()

        return res

'''
#GET请求
url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
'''