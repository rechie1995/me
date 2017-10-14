#!/usr/bin/env python
# coding:utf-8
'''
这是一个udp客户端
'''
import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 80

# 建立一个socket对象
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
CLIENT.sendto("AAABBBCCC", (TARGET_HOST, TARGET_PORT))

# 接收一些数据
DATA, ADDR = CLIENT.recvfrom(4096)

print DATA
