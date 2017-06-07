#!/usr/bin/env python
# coding: utf-8

import socket
import cv2
import numpy as np


HOST = '192.168.31.221'
PORT = 8000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    data=s.recv(1024)
    datalist = list(data)
    datalist_np = np.array(datalist, dtype = int)
    print type(datalist_np)
    cv2.imshow("image",datalist_np)
s.close()
