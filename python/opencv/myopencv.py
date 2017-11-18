#!/usr/bin/env python
# coding: utf-8
'''
我的opencv代码例子
'''
import cv2

def show_image():
    '''
    展示图片
    '''
    img = cv2.imread("../../data/Pictures/1.jpg")
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_image()
