from helpers import resizeRawImage
from display.Drawable import Drawable


class ImageStreamDisplay(Drawable):
    def __init__(self, canvas, imageProvider, imageSize):
        super(ImageStreamDisplay, self).__init__()
        self.canvas = canvas
        self.imageProvider = imageProvider
        self.imageSize = imageSize
        self.imageCenter = calculateImageCenter(*imageSize)
        self.currentRawImage = None
        self.currentPhoto = None

    def draw(self, timePassed):
        if not self._isHidden:
            newRawImage = self.imageProvider.getNextFrame()
            if newRawImage is not None:
                if not newRawImage is self.currentRawImage:  #compare object equality for performance on static stream
                    self.currentRawImage = newRawImage
                    self.currentPhoto = resizeRawImage(newRawImage, self.imageSize)
                self.canvas.create_image(self.imageCenter, image=self.currentPhoto)

def calculateImageCenter(windowWidth, windowHeight):
    return windowWidth/2, windowHeight/2
