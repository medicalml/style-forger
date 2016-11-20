import cv2
import config
from helpers import resizeRawImage

class CameraImageProvider:
    def __init__(self):
        self.cap = cv2.VideoCapture(config.CAMERA_ID)

    def getRawImage(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
