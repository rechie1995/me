#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: rechie

import cv2 
import time


def main():
    video = "http://192.168.31.221:10244"
    capture = cv2.VideoCapture(video) # 打开一个视频文件
    if capture is None:
        print 'Video does not load !!!'
    while True:
        ret, frame = capture.read()
        cv2.imshow("camera", frame)   # 显示
        key = cv2.waitKey(10)&0xFF
        if key == ord('s'):
            cv2.imwrite("file.jpg", frame)
            print 'saved'
        if key == 27:  #ESC
            print 'ESC pressed. Exiting...'
            break
        
if __name__ == '__main__':
    main()
