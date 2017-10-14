#!/usr/bin/env python
# coding:utf-8
'''
这是tcp客户端
'''
import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 9999

# 建立一个socket对象
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
CLIENT.connect((TARGET_HOST, TARGET_PORT))

# 发送一些数据
CLIENT.send("hello\r\n\r\n")

# 接收一些数据
RESPONSE = CLIENT.recv(4096)

print RESPONSE
