#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @author: rechie

from cv2 import *

def erode_dilate():
    img = imread("/home/rechie/Pictures/6.jpg")
    
    # opencv定义的结构元素
    kernel = getStructuringElement(MORPH_RECT,(3,3))
    
    # 腐蚀图像
    eroded = erode(img, kernel)
    # 显示腐蚀后的图像
    imshow("Eroded Image", eroded)
    
    # 膨胀图像
    dilated = dilate(img, kernel)
    # 显示膨胀后的图像
    imshow("Dilated Image", dilated)
    
    # 原图像
    imshow("Origin", img)
    
    waitKey(0)
    destroyAllWindows()

if __name__ == '__main__':
    erode_dilate()
