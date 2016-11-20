from time import sleep
import cv2

class TransformationApplierMock:
    def __init__(self, sleepTime):
        self.sleepTime = sleepTime
        pass
    @staticmethod
    def transform(self, frame):
        sleep(self.sleepTime)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        return frame

def afterTransformationActionMock(imageRaw):
    print("afterTransformationActionMock: handling array with shape " + str(imageRaw.shape))