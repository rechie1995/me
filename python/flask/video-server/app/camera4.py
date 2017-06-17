import cv2
import socket
import time
import numpy as np
from common import draw_str 

class VideoCamera(object):
    address = "http://192.168.2.1:8080/?action=stream"
    cascade_ad = "/home/rechie/git/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"
    pre_frame = None
    fps = 20

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
        start = time.time()
        success, image = self.video.read()
        end = time.time()
        seconds = end - start
        if seconds < 1.0/self.fps:
            time.sleep(1.0/self.fps - seconds)


        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray1 = gray.copy()
        gray2 = gray.copy()
        gray1 = cv2.equalizeHist(gray1)
        gray2 = cv2.resize(gray2, (500, 500))
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
        vis = image.copy()
        rects = self.detect(gray1, self.cascade)
        self.draw_rects(vis, rects, (0, 255, 0))
        if self.pre_frame is None:
            self.pre_frame = gray2
        else:
            img_delta = cv2.absdiff(self.pre_frame, gray2)
            thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
            img1, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv2.contourArea(c) < 1000:
                    continue
                else:
                    print("diff")
                    draw_str(vis,(20,20), 'Have motion object!')
                    break

            self.pre_frame = gray2
        
        ret, jpeg = cv2.imencode('.jpg', vis)
        return jpeg.tostring()
