import cv2
import config
from helpers import resizeRawImage

class CameraImageProvider:
    def __init__(self, displaySize):
        self.cap = cv2.VideoCapture(config.CAMERA_ID)
        self.displaySize = displaySize

    def getDisplayPhotoImage(self):
        self.lastFrame = resizeRawImage(self.getRawImage(), self.displaySize)
        return self.lastFrame

    def getRawImage(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
