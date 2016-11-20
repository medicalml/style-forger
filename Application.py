from FullscreenCanvas import FullscreenCanvas
from helpers import RecurringTask, DelayedTask


class Application():
    def __init__(self, root, cameraImageProvider, transformationProvider):
        self.root = root
        self.canvas = FullscreenCanvas(root)
        self.imgTransformed = None

        self.cameraImageProvider = cameraImageProvider
        self.transformationProvider = transformationProvider
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
        self.canvas.displayImgArrayFullscreen(self.cameraImageProvider.getRawImage())
        if self.transformationProvider.hasTransformedFrameWaiting():
            self.imgTransformed = self.transformationProvider.getTransformedFrame()
            self.transformationDeleter.run()
        if self.imgTransformed is not None:
            self.canvas.displayImgArrayFullscreen(self.imgTransformed)
