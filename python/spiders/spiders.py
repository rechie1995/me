#!/usr/bin/env python
# coding: utf-8
'''
爬虫demo
'''
import urllib
import urllib2

class Spiders(object):
    '''
    爬虫类
    '''
    def __init__(self):
        '''
        构造函数
        '''
        self.url = ""
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent}
        self.values = {}
        self.values['username'] = ""
        self.values['password'] = ""

    def getwebpage(self):
        '''
        获取原始网页
        '''
        self.url = "www.baidu.com"
        request = urllib2.urlopen(self.url)
        response = urllib2.urlopen(request)
        print response.read()

    def post(self):
        '''
        post方法
        '''
        data = urllib.urlencode(self.values)
        self.url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
        request = urllib2.Request(self.url, data)
        response = urllib2.urlopen(request)
        print response.read()

    def get(self):
        '''
        get 方法
        '''
        data = urllib.urlencode(self.values)
        self.url = "http://passport.csdn.net/account/login"
        geturl = self.url + "?"+data
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        print response.read()
