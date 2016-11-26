from PIL.ImageTk import PhotoImage
from Animation import Animation
from PIL import Image
from display.display_helpers import cropCircleImage
from easing_functions import *


class ImageCircleAnimation(Animation):
    cycleDuration = 5000
    circleStartSize = 1
    sizeDifference = 500
    imagePath = "url.jpg"

    def __init__(self, canvas, imageCenter):
        Animation.__init__(self, canvas, self.drawCommand, ImageCircleAnimation.cycleDuration)
        self.imageCenter = imageCenter
        image = Image.open(ImageCircleAnimation.imagePath)
        self.croppedImageSource = cropCircleImage(image)
        self.easingFunction = easeOutElastic

    def drawCommand(self, phase):
        self.canvas.create_image(self.imageCenter, image=self.applyAnimation(phase))

    def calculateCircleSize(self, phase):
        sourceWidth, sourceHeight = self.croppedImageSource.size

        diameter = (self.easingFunction(phase) * ImageCircleAnimation.sizeDifference) + ImageCircleAnimation.circleStartSize

        resizeRatio = float(diameter) / min(sourceWidth, sourceHeight)
        return int(sourceWidth * resizeRatio), int(sourceHeight * resizeRatio)

    def applyAnimation(self, phase):
        sizeInPhase = self.calculateCircleSize(phase)
        self._displayPhotoRef = PhotoImage(self.croppedImageSource.resize(sizeInPhase))
        return self._displayPhotoRef

