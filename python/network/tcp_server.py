#!/usr/bin/env python
# coding:utf-8
'''
这是tcp服务器
'''

import socket
import threading

BIND_IP = "0.0.0.0"
BIND_PORT = 9999

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 确定服务器需要监听的IP地址和端口
SERVER.bind((BIND_IP, BIND_PORT))

# 启动监听，并将最大连接数设为5
SERVER.listen(5)

print "[*] Listening on %s:%d" % (BIND_IP, BIND_PORT)

def handle_client(client_socket):
    '''
    这是客户端处理线程
    '''

    # 打印出客户端发送得到内容
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # 返还一个数据包
    client_socket.send("ACK!")

    client_socket.close()

while True:

    # 将接收到的客户端套接字对象保存到client变量中。
    # 将远程连接的细节保存到addr变量中。
    CLIENT, ADDR = SERVER.accept()

    print "[*] Accepted connection from: %s:%d" % (ADDR[0], ADDR[1])

    # 挂起客户端线程，处理传入的数据
    CLIENT_HANDLER = threading.Thread(target=handle_client, args=(CLIENT,))
    CLIENT_HANDLER.start()
    