from Drawable import Drawable

class Animation(Drawable):
    def __init__(self, canvas, drawCommand, cycleDuration):
        super(Animation, self).__init__()
        self.canvas = canvas
        self.drawCommand = drawCommand
        self.cycleDuration = cycleDuration
        self.currentCycleTime = 0

    def draw(self, timePassed):
        self.updateCurrentCycleTime(timePassed)
        self.drawCommand(self.calculatePhase())

    def updateCurrentCycleTime(self, timePassed):
        newCycleTime = self.currentCycleTime+timePassed
        self.currentCycleTime =  newCycleTime % self.cycleDuration

    def calculatePhase(self):
        return float(self.currentCycleTime) / float(self.cycleDuration) #floating point value between 0 and 1
