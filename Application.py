from display.FullscreenCanvas import FullscreenCanvas
from display.ImageCircleAnimation import ImageCircleAnimation
from display.ImageStreamDisplay import ImageStreamDisplay
from initialization import transformationApplier, afterTransformationAction
from CameraImageStream import CameraImageStream
from TransformedImageStream import TransformedImageStream


class Application(object):
    def __init__(self, root):
        self.root = root
        windowSize, windowCenter = _getWindowParameters(root)
        self.canvas = FullscreenCanvas(root, windowSize)

        actionWithNotify = lambda x : self.notifyTransformationFinish(x)
        cameraImageStream = CameraImageStream()
        self.transformedImageStream = TransformedImageStream(root, cameraImageStream, transformationApplier, actionWithNotify)

        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, cameraImageStream, windowSize))
        self.transformationDisplay = ImageStreamDisplay(self.canvas, self.transformedImageStream, windowSize)
        self.canvas.addDrawableChild(self.transformationDisplay)
        self.processingAnimation = ImageCircleAnimation(self.canvas, windowCenter)
        self.processingAnimation.hide()
        self.canvas.addDrawableChild(self.processingAnimation)

        root.bind('<Return>', self.initiateFrameTransformation)

    def notifyTransformationFinish(self, imageRaw):
        self.processingAnimation.hide()
        afterTransformationAction(imageRaw)

    def initiateFrameTransformation(self, event):
        if self.transformedImageStream.initiateFrameTransformation(event):
            self.processingAnimation.show()



def _getWindowParameters(root):
    root.update()
    windowSize = root.winfo_width(), root.winfo_height()
    width, height = windowSize
    windowCenter = (width/2, height/2)
    return windowSize, windowCenter
