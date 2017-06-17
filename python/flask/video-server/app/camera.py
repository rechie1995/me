import cv2
import socket

import numpy as np 

class VideoCamera(object):
    address = "http://192.168.2.1:8080/?action=stream"
    cascade_ad = "/home/rechie/git/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"

    def __init__(self):
        self.video = cv2.VideoCapture(self.address)
        self.cascade = cv2.CascadeClassifier(self.cascade_ad)

    def __del__(self):
        self.video.release()
    
    def detect(self,img, cascade):
        rects = cascade.detectMultiScale(img,scaleFactor=1.3,minNeighbors=4,minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

    def draw_rects(self,img, rects,color):
        for x1,y1,x2,y2 in rects:
		cv2.rectangle(img,(x1,y1),(x2,y2),color,2)


    def get_frame(self):
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        vis = image.copy()
        rects = self.detect(gray, self.cascade)
        self.draw_rects(vis, rects, (0, 255, 0))
        ret, jpeg = cv2.imencode('.jpg', vis)
        return jpeg.tostring()
