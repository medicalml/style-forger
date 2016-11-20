
class TransformationProvider:
    instance = None
    def __init__(self, cameraImageProvider):
        TransformationProvider.instance = self
        self.cameraImageProvider = cameraImageProvider

    @staticmethod
    def initiateFrameTransformation(event):
        self = TransformationProvider.instance
        assert self is not None
        print "abc"

    def transformCurrentFrame(self):
        frame = self.cameraImageProvider.getRawImage()