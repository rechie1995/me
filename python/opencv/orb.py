#!/usr/bin/env python
# coding: utf-8

# ORB: Oriented Fast and Rotated BRIEF
# 它是OpenCV_Labs在2011年提出的，首先它是免费的，而SIFT和SURF是受专利保护，并且要收费的，
# ORB是他们的一个替代品，在计算能力有限的设备上适合这个东西。
#
# 它的效果：sift > orb > surf, 计算速度 orb > surf > sift


import cv2

img = cv2.imread('../../data/Pictures/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(gray, None)
print len(kp)
kp, des = orb.compute(gray, kp)
print len(kp)

img2 = cv2.drawKeypoints(gray, kp, (255,0,0), 1)

cv2.imshow('orb', img2)
cv2.waitKey(0)
