from AsyncTransformator import AsyncTransformator

class TransformationProvider:
    instance = None

    def __init__(self, cameraImageProvider, transformationApplier):
        TransformationProvider.instance = self
        self.cameraImageProvider = cameraImageProvider
        self.transformationApplier = transformationApplier
        self.resetTransformationState()

    @staticmethod
    def initiateFrameTransformation(event):
        self = TransformationProvider.instance
        assert self is not None
        if not self.isProcessing():
            self.transformCurrentFrame()

    def transformCurrentFrame(self):
        self.resetTransformationState()
        frame = self.cameraImageProvider.getNextFrame()
        self.asyncTransformator = AsyncTransformator(self.transformationApplier, frame)

    def isProcessing(self):
        return self.asyncTransformator is not None

    def hasTransformedFrameWaiting(self):
        return self.asyncTransformator.isFinished() if self.isProcessing() else False

    def getTransformedFrame(self):
        if self.isProcessing():
            frame = self.asyncTransformator.getTransformedFrame()
            self.resetTransformationState()
            return frame
        else:
            raise Exception(
                "No frame waiting, check with hasTransformedFrameWaiting first to avoid blocking main thread")

    def resetTransformationState(self):
        self.transformedFrame = None
        self.asyncTransformator = None
