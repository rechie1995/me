#!/usr/bin/env python
# coding: utf-8
'''
打印本机host_name和IP地址
'''
import socket

def print_machine_info():
    '''
    打印主机名称及IP地址
    '''
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address

if __name__ == '__main__':
    print_machine_info()
