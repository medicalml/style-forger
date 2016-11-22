from FullscreenCanvas import FullscreenCanvas
from helpers import RecurringTask, DelayedTask


class Application():
    def __init__(self, root, cameraImageStream, transformationProvider, afterTransformationAction):
        self.root = root
        self.canvas = FullscreenCanvas(root)
        self.imgTransformed = None

        self.cameraImageProvider = cameraImageStream
        self.transformationProvider = transformationProvider
        self.afterTransformationAction = afterTransformationAction
        self.cameraLookupTask = self.createCameraLookup()
        self.transformationDeleter = DelayedTask(root, 2000, self.forgetTransformation)

        root.bind('<Return>', self.transformationProvider.initiateFrameTransformation)

    def createCameraLookup(self):
        cameraLookupTask = RecurringTask(self.root, 50, self.updateCameraLookup)
        return cameraLookupTask

    def forgetTransformation(self):
        self.imgTransformed = None

    def updateCameraLookup(self):
        self.canvas.flush()
        self.canvas.displayImgArrayFullscreen(self.cameraImageProvider.getNextFrame())
        self.handleTransformationDisplay()

    def handleTransformationDisplay(self):
        self.fetchAwaitingTransformation()
        if self.transformationProvider.isProcessing():
            self.showLoadingAnimation()
        if self.imgTransformed is not None:
            self.canvas.displayImgArrayFullscreen(self.imgTransformed)

    def fetchAwaitingTransformation(self):
        if self.transformationProvider.hasTransformedFrameWaiting():
            self.imgTransformed = self.transformationProvider.getTransformedFrame()
            self.afterTransformationAction(self.imgTransformed.copy())
            self.transformationDeleter.run()

    def showLoadingAnimation(self):
        self.canvas.displayCircle()
