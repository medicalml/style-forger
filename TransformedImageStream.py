from AsyncTransformator import AsyncTransformator
from helpers import DelayedTask
import config


class TransformedImageStream:
    def __init__(self, root, cameraImageStream, transformationApplier):
        self.cameraImageStream = cameraImageStream
        self.transformationApplier = transformationApplier
        self.transformationDeleter = DelayedTask(root, config.TRANSFORMATION_DISPLAY_TIME, self.forgetTransformation)
        self.asyncTransformator = AsyncTransformator(self.transformationApplier)
        self.transformedFrame = None

    def getNextFrame(self):
        self.updateTransformation()
        return self.transformedFrame

    def initiateFrameTransformation(self, event):
        if self.isShowingTransformation() and not self.asyncTransformator.isRunning():
            self.startTransformationJob(self.cameraImageStream.getNextFrame())

    def isShowingTransformation(self):
        return self.transformedFrame is None

    def startTransformationJob(self, frame):
        self.asyncTransformator.startParallelTransformation(frame)
        self.transformationDeleter.run()

    def forgetTransformation(self):
        self.transformedFrame = None

    def updateTransformation(self):
        if self.asyncTransformator.hasAwaitingResult():
            self.transformedFrame = self.asyncTransformator.getTransformedFrame()
