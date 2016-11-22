from AsyncTransformator import AsyncTransformator
from helpers import DelayedTask
import config


class TransformedImageStream:
    def __init__(self, root, cameraImageStream, transformationApplier):
        self.cameraImageStream = cameraImageStream
        self.transformationApplier = transformationApplier
        self.transformationDeleter = DelayedTask(root, config.TRANSFORMATION_DISPLAY_TIME, self.forgetTransformation)
        self.transformedFrame = None
        self.asyncTransformator = None

    def getNextFrame(self):
        self.updateTransformation()
        return self.transformedFrame

    def initiateFrameTransformation(self, event):
        if self.isShowingTransformation() and not self.isTransformationProcessing():
            self.transformCurrentFrame()

    def isShowingTransformation(self):
        return self.transformedFrame is None

    def transformCurrentFrame(self):
        self.forgetTransformation()
        frame = self.cameraImageStream.getNextFrame()
        self.asyncTransformator = AsyncTransformator(self.transformationApplier, frame)
        self.transformationDeleter.run()

    def hasTransformedFrameWaiting(self):
        return self.isTransformationProcessing() and self.asyncTransformator.isFinished()

    def isTransformationProcessing(self):
        return self.asyncTransformator is not None

    def forgetTransformation(self):
        self.transformedFrame = None

    def updateTransformation(self):
        if self.hasTransformedFrameWaiting():
            self.transformedFrame = self.asyncTransformator.getTransformedFrame()
            self.asyncTransformator = None
