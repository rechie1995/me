#!/usr/bin/env python
# coding:utf-8

import serial

com = serial.Serial('/dev/ttyS1',115200)
print com.portstr
while True:
    n = com.inWaiting()
    if (n != 0):
        print n
        data = com.read(n)
        print data
        if(data == "@,1,5,1,#"):
            com.write("@,18,3,ok,#")
        if(data == "@,14,5,14,#"):
            com.write("@,18,3,ok,#")
