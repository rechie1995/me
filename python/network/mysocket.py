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
    ip_address_list = socket.gethostbyname_ex(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address
    print ip_address_list

def get_remote_machine_info():
    '''
    获取远程主机信息
    '''
    remote_host = 'rechie.top'
    print "Host name: %s" % remote_host
    try:
        print "IP address: %s" %socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

def find_service_name():
    '''
    获取服务名称
    '''
    protocolname = 'tcp'
    for port in [80, 25, 21, 22]:
        servicename = socket.getservbyport(port, protocolname)
        print "Port: %s => service name: %s" %(port, servicename)

if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info()
    find_service_name()
