from __future__ import division #for / to return float by default
from PIL import Image, ImageTk


def resizeRawImage(imageRaw, size, cover = True):
    image = Image.fromarray(imageRaw)
    return resizeImage(image, size, cover)

def resizeImage(image, size, cover = True):
    newSize = size if not cover else calculateSizeToCover(image.size, size)
    resized = image.resize(newSize, resample=Image.LANCZOS)
    return ImageTk.PhotoImage(resized)

def calculateSizeToCover(srcSize, maxSize):
    srcWidth, srcHeight = srcSize
    maxWidth, maxHeight = maxSize

    ratio = max(maxWidth / srcWidth, maxHeight / srcHeight)
    return int(srcWidth*ratio), int(srcHeight*ratio)

class DelayedTask(object):
    def __init__(self,
                 tkRoot,
                 delayInMs,
                 command,
                 *commandArgs):
        self.tkRoot = tkRoot
        self.command = command
        self.commandArgs = commandArgs
        self.delay = delayInMs
        self.job = None

    def run(self):
        self.cancel()
        self.job = self.tkRoot.after(
            self.delay,
            self.execute)

    def execute(self):
        self.command(*self.commandArgs)
        self.job = None

    def cancel(self):
        if self.job is not None:
            self.tkRoot.after_cancel(self.job)
            self.job = None

class RecurringTask(object):
    def __init__(self,
                 tkRoot,
                 delayInMs,
                 command,
                 *commandArgs):
        self.tkRoot = tkRoot
        self.command = command
        self.commandArgs = commandArgs
        self.delay = delayInMs

        self.execute()

    def execute(self):
        self.command(*self.commandArgs)
        self.tkRoot.after(self.delay,
                          self.execute)

