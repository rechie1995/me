#!/usr/bin/env python
# coding: utf-8
'''
爬虫demo
'''
import urllib
import urllib2

def get_web_page():
    '''
    获取网页
    '''
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()

def get_url_list():
    '''
    获取URL列表
    '''

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

if __name__ == '__main__':
    get_web_page()
    