import cv2
import config
from helpers import resizeRawImage

class CameraImageProvider:
    def __init__(self):
        self.cap = cv2.VideoCapture(5)
        try:
            self.getRawImage()
        except:
            raise EnvironmentError('No camera on this id, available ids: ' + str(getCameraIdsList()))

    def getRawImage(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

def getCameraIdsList():
    resList = []
    for cameraId in range(0, 10):
        cap = cv2.VideoCapture(cameraId)
        ret, _ = cap.read()
        if ret:
            resList.append(cameraId)
            cap.release()
    return resList