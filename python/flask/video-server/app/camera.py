import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('/home/rechie/Documents/live/mediaServer/01.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()