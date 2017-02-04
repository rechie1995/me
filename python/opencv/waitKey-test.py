#!/usr/bin/env python

import cv2

img = cv2.imread("/home/rechie/Pictures/girls/1.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
k = cv2.waitKey(0)&0xFF
if k == 27:# esc
    cv2.destroyAllWindows()

