from time import sleep

from AsyncTransformator import AsyncTransformator


class TransformationApplierMock:
    def __init__(self):
        pass
    @staticmethod
    def transform(self, frame):
        sleep(1)
        return frame


class TransformationProvider:
    instance = None

    def __init__(self, cameraImageProvider):
        TransformationProvider.instance = self
        self.cameraImageProvider = cameraImageProvider
        self.resetTransformationState()
        self.transformationApplier = TransformationApplierMock()

    @staticmethod
    def initiateFrameTransformation(event):
        self = TransformationProvider.instance
        assert self is not None
        if not self.isTransformationInProgress():
            self.transformCurrentFrame()

    def transformCurrentFrame(self):
        self.resetTransformationState()
        frame = self.cameraImageProvider.getRawImage()
        self.asyncTransformator = AsyncTransformator(self.transformationApplier, frame)

    def isTransformationInProgress(self):
        return self.asyncTransformator is not None

    def hasTransformedFrameWaiting(self):
        return self.asyncTransformator.isFinished() if self.isTransformationInProgress() else False

    def getTransformedFrame(self):
        if self.isTransformationInProgress():
            frame = self.asyncTransformator.getTransformedFrame()
            self.resetTransformationState()
            return frame
        else:
            raise Exception(
                "No frame waiting, check with hasTransformedFrameWaiting first to avoid blocking main thread")

    def resetTransformationState(self):
        self.transformedFrame = None
        self.asyncTransformator = None
