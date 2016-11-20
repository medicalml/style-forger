from FullscreenCanvas import FullscreenCanvas
from RecurringTask import RecurringTask


class Application():
    def __init__(self, root, cameraImageProvider, transformationProvider):
        self.root = root
        self.canvas = FullscreenCanvas(root)
        self.imgTransformed = None

        self.cameraImageProvider = cameraImageProvider
        self.transformationProvider = transformationProvider
        self.cameraLookupTask = self.createCameraLookup()

        root.bind('<Return>', self.transformationProvider.initiateFrameTransformation)

    def createCameraLookup(self):
        cameraLookupTask = RecurringTask(self.root, 50, self.updateCameraLookup)
        return cameraLookupTask

    def updateCameraLookup(self):
        self.canvas.flush()
        self.canvas.displayImgArrayFullscreen(self.cameraImageProvider.getRawImage())
        if self.transformationProvider.hasTransformedFrameWaiting():
            self.imgTransformed = self.transformationProvider.getTransformedFrame()
        if self.imgTransformed is not None:
            self.canvas.displayImgArrayFullscreen(self.imgTransformed)
