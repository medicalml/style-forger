from display.FullscreenCanvas import FullscreenCanvas
from display.ImageCircleAnimation import ImageCircleAnimation
from display.ImageStreamDisplay import ImageStreamDisplay
from initialization import transformationApplier, afterTransformationAction
from CameraImageStream import CameraImageStream
from TransformedImageStream import TransformedImageStream


class Application(object):
    def __init__(self, root, transferedArtStyles):
        self.root = root
        self.windowSize, self.windowCenter = _getWindowParameters(root)
        self.canvas = FullscreenCanvas(root, self.windowSize)

        actionWithNotify = lambda x : self.notifyTransformationFinish(x)
        cameraImageStream = CameraImageStream()
        self.transformedImageStream = TransformedImageStream(root, cameraImageStream, transformationApplier, actionWithNotify)

        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, cameraImageStream, self.windowSize))
        self.transformationDisplay = ImageStreamDisplay(self.canvas, self.transformedImageStream, self.windowSize)
        self.canvas.addDrawableChild(self.transformationDisplay)
        self.processingAnimation = None

        root.bind('<Return>', self.initiateFrameTransformation)

    def notifyTransformationFinish(self, imageRaw):
        self.canvas.removeDrawableChild(self.processingAnimation)
        afterTransformationAction(imageRaw)

    def initiateFrameTransformation(self, event):
        if self.transformedImageStream.initiateFrameTransformation(event):
            self.processingAnimation = ImageCircleAnimation(self.canvas, self.windowCenter)
            self.canvas.addDrawableChild(self.processingAnimation)

def _getWindowParameters(root):
    root.update()
    windowSize = root.winfo_width(), root.winfo_height()
    width, height = windowSize
    windowCenter = (width/2, height/2)
    return windowSize, windowCenter
