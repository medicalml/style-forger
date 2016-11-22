from Animation import Animation
from helpers import resizeRawImage


class ImageStreamDisplay:
    def __init__(self, canvas, imageProvider, imageSize):
        self.canvas = canvas
        self.imageProvider = imageProvider
        self.imageSize = imageSize
        self.imageCenter = calculateImageCenter(*imageSize)
        self.currentPhoto = None

    def draw(self, timePassed):
        rawImage = self.imageProvider.getNextFrame()
        if rawImage is not None:
            self.currentPhoto = resizeRawImage(rawImage, self.imageSize)
            self.canvas.create_image(self.imageCenter, image=self.currentPhoto)

def calculateImageCenter(windowWidth, windowHeight):
    return windowWidth/2, windowHeight/2