from AsyncTransformator import AsyncTransformator
from helpers import DelayedTask


class TransformedImageStream:
    instance = None  # has to be a singleton, TkInter key listeners only accept static mathods

    def __init__(self, root, cameraImageStream, transformationApplier):
        TransformedImageStream.instance = self
        self.cameraImageStream = cameraImageStream
        self.transformationApplier = transformationApplier
        self.transformationDeleter = DelayedTask(root, 2000, self.forgetTransformation)  # TODO: extract time to config
        self.transformedFrame = None
        self.asyncTransformator = None

    def getNextFrame(self):
        self.updateTransformation()
        return self.transformedFrame

    @staticmethod
    def initiateFrameTransformation(event):
        self = TransformedImageStream.instance
        assert self is not None
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
