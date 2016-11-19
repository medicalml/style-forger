import cv2
import config
from PIL import Image, ImageTk

def resizeImage(image, size):
    resized = image.resize(size)
    return ImageTk.PhotoImage(resized)

class CameraImageProvider:
    def __init__(self, displaySize):
        self.cap = cv2.VideoCapture(config.CAMERA_ID)
        self.displaySize = displaySize

    def getDisplayPhotoImage(self):
        self.lastFrame = resizeImage(Image.fromarray(self.getImageRaw()), self.displaySize)
        return self.lastFrame

    def getImageRaw(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
