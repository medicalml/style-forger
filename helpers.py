from __future__ import division #for / to return float by default
from PIL import Image, ImageTk


def resizeRawImage(imageRaw, size, cover = True):
    image = Image.fromarray(imageRaw)
    return resizeImage(image, size, cover)

def resizeImage(image, size, cover = True):
    newSize = size if not cover else calculateSizeToCover(image.size, size)
    resized = image.resize(newSize)
    return ImageTk.PhotoImage(resized)

def calculateSizeToCover(srcSize, maxSize):
    srcWidth, srcHeight = srcSize
    maxWidth, maxHeight = maxSize

    ratio = max(maxWidth / srcWidth, maxHeight / srcHeight)
    return int(srcWidth*ratio), int(srcHeight*ratio)

class RecurringTask:
    def __init__(self,
                 tkRoot,
                 delayInMs,
                 staticMethod,
                 *methodArgs):
        self.tkRoot = tkRoot
        self.staticMethod = staticMethod
        self.methodArgs = methodArgs
        self.delay = delayInMs

        self.isJobRunning = True
        self.execute()

    def execute(self):
        if self.isJobRunning:
            self.staticMethod(*self.methodArgs)
            self.tkRoot.after(self.delay,
                              self.execute)

    def stop(self):
        self.isJobRunning = False
