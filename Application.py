from FullscreenCanvas import FullscreenCanvas
from CameraImageProvider import CameraImageProvider
from RecurringTask import RecurringTask
from TransformationProvider import TransformationProvider
from helpers import resizeRawImage


class Application():
    def __init__(self, root):
        self.root = root
        self.canvas = FullscreenCanvas(root)
        self.imgTransformed = None

        self.cameraImageProvider = CameraImageProvider()
        self.transformationProvider = TransformationProvider(self.cameraImageProvider)
        self.cameraLookupTask = self.createCameraLookup()

        root.bind('<Return>', self.transformationProvider.initiateFrameTransformation)

    def createCameraLookup(self):
        cameraLookupTask = RecurringTask(self.root, 50, Application.updateCameraLookup, self)
        return cameraLookupTask

    def updateCameraLookup(self):
        self.canvas.flush()
        self.canvas.displayImgArrayFullscreen(self.cameraImageProvider.getRawImage())
        if self.transformationProvider.hasTransformedFrameWaiting():
            self.imgTransformed = self.transformationProvider.getTransformedFrame()
        if self.imgTransformed is not None:
            self.canvas.displayImgArrayFullscreen(self.imgTransformed)
