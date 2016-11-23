from display.FullscreenCanvas import FullscreenCanvas
from display.PulsingCircle import PulsingCircle
from display.ImageStreamDisplay import ImageStreamDisplay


# TODO: make all classes extend Object
class Application:
    def __init__(self, root, cameraImageStream, transformedImageStream):
        self.root = root
        windowSize = getWindowSize(root)
        self.canvas = FullscreenCanvas(root, windowSize)

        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, cameraImageStream, windowSize))
        self.canvas.addDrawableChild(ImageStreamDisplay(self.canvas, transformedImageStream, windowSize))
        #self.canvas.addDrawableChild(PulsingCircle(self.canvas, (50,50)))

        root.bind('<Return>', transformedImageStream.initiateFrameTransformation)

def getWindowSize(root):
    root.update()
    return root.winfo_width(), root.winfo_height()
