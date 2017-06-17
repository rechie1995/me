import cv2
import socket
import numpy as np 

class VideoCamera(object):
    HOST = '192.168.31.221'
    PORT = 10244

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def __del__(self):
        self.s.close()

    def recv_all(self, count):
        data = ''
        while count:
            newdata = self.s.recv(1024)
            print newdata
            if not newdata: return None
            data += newdata
            count = count - 1
        return data

    def get_frame(self):
        img = [1, 2, 3]
        imga = [ ]
        imgb = [ ]
        data = self.recv_all(900)
        for i in range(0, 480):
            for j in range(0, 640):
                img[0] = ord(data[((479 - i) * 640 + j) * 3])
                img[1] = ord(data[((479 - i) * 640 + j) * 3 + 1])
                img[2] = ord(data[((479 - i) * 640 + j) * 3 + 2])
                imga.append(img)
                img=[1,2,3]
            xx = np.array(imga)
            imgb.append(imga)
            imga = []


        pic = np.array(imgb)
        imgg = np.array(imgb)
        imgg = pic*255

        # success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', imgg)
        return jpeg.tostring()
