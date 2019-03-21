from time import sleep
import cv2

class TransformationApplierMock(object):
    def __init__(self, sleepTime):
        self.sleepTime = sleepTime
        pass

    def transform(self, frame, modelpath):
        sleep(self.sleepTime)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        return frame

def afterTransformationActionMock(imageRaw):
    cv2.imwrite('./test.png', imageRaw)
    print("afterTransformationActionMock: handling array with shape " + str(imageRaw.shape))
