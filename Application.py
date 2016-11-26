from display.FullscreenCanvas import FullscreenCanvas
from display.ImageCircleAnimation import ImageCircleAnimation
from display.ImageStreamDisplay import ImageStreamDisplay
from initialization import initializeImageStreams


class Application(object):
    def __init__(self, root):
        self.root = root
        windowSize = _getWindowSize(root)
        width, height = windowSize
        windowCenter = (width/2, height/2)
        self.canvas = FullscreenCanvas(root, windowSize)

        cameraImageStream, transformedImageStream = initializeImageStreams(root)
        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, cameraImageStream, windowSize))
        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, transformedImageStream, windowSize))
        self.canvas.addDrawableChild(ImageCircleAnimation(self.canvas, windowCenter))

        root.bind('<Return>', transformedImageStream.initiateFrameTransformation)

def _getWindowSize(root):
    root.update()
    return root.winfo_width(), root.winfo_height()
