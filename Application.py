from display.FullscreenCanvas import FullscreenCanvas
from display.PulsingCircle import PulsingCircle
from display.FullscreenImageStream import FullscreenImageStream


class Application:
    def __init__(self, root, cameraImageStream, transformedImageStream, afterTransformationAction):
        self.root = root
        windowSize = getWindowSize(root)
        self.canvas = FullscreenCanvas(root, windowSize)
        self.imgTransformed = None

        self.afterTransformationAction = afterTransformationAction

        self.canvas.addDrawableChild(FullscreenImageStream(self.canvas, cameraImageStream, windowSize))
        self.canvas.addDrawableChild(FullscreenImageStream(self.canvas, transformedImageStream, windowSize))
        self.canvas.addDrawableChild(PulsingCircle(self.canvas, (50,50)))

        root.bind('<Return>', transformedImageStream.initiateFrameTransformation)

def getWindowSize(root):
    root.update()
    return root.winfo_width(), root.winfo_height()
