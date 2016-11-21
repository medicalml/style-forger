from display_helpers import boundingBoxSquare
from Animation import Animation
import config
from math import cos

class PulsingCircle(Animation):
    cycleDuration = 1000
    circleBaseSize = 100
    sizeDifference = 30
    def __init__(self, canvas, circleCenter):
        Animation.__init__(self, canvas, self.drawCommand, PulsingCircle.cycleDuration)
        self.circleCenter = circleCenter

    def drawCommand(self,
                    phase): # floating point value between 0 and 1
        self.canvas.create_oval(
            boundingBoxSquare(self.circleCenter, self.calculateCircleSize(phase)),
            fill=config.PRIMARY_COLOR,
            outline="")

    def calculateCircleSize(self, phase):
        return self.applyTimingFunction(phase, PulsingCircle.sizeDifference) + PulsingCircle.circleBaseSize

    def applyTimingFunction(self, phase, variableProperty):
        phaseFraction = cos((phase* 2.0)  - 1.0)
        return phaseFraction * variableProperty
