from PIL.ImageTk import PhotoImage

from Animation import Animation
from PIL import Image
from math import cos
from display.display_helpers import cropCircleImage


class ImageCircleAnimation(Animation):
    cycleDuration = 500
    circleMaxSize = 500
    sizeDifference = -30
    imagePath = "url.jpg"

    def __init__(self, canvas, imageCenter):
        Animation.__init__(self, canvas, self.drawCommand, ImageCircleAnimation.cycleDuration)
        self.imageCenter = imageCenter
        image = Image.open(ImageCircleAnimation.imagePath)
        self.croppedImageSource = cropCircleImage(image)

    def drawCommand(self, phase):
        self.canvas.create_image(self.imageCenter, image=self.applyAnimation(phase))

    def calculateCircleSize(self, phase):
        sourceWidth, sourceHeight = self.croppedImageSource.size
        diameter = self.applyEasingFunction(phase, ImageCircleAnimation.sizeDifference) + ImageCircleAnimation.circleMaxSize
        resizeRatio = float(diameter) / min(sourceWidth, sourceHeight)
        return int(sourceWidth * resizeRatio), int(sourceHeight * resizeRatio)

    def applyEasingFunction(self, phase, variableProperty):
        phaseFraction = cos((phase* 2.0)  - 1.0)
        return phaseFraction * variableProperty

    def applyAnimation(self, phase):
        sizeInPhase = self.calculateCircleSize(phase)
        self._displayPhotoRef = PhotoImage(self.croppedImageSource.resize(sizeInPhase))
        return self._displayPhotoRef
