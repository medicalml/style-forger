import Tkinter as tk
import time
from helpers import RecurringTask
import config


def getPreciseTimeMs():
    return int(time.clock() * 1000.0)


class FullscreenCanvas(tk.Canvas):
    minFrameDelay = 1000 / config.CANVAS_MAX_FPS

    def __init__(self, root, windowSize):
        tk.Canvas.__init__(self, master=root, bg="white")
        self.windowSize = windowSize
        self.update()
        self.resizeCanvasToFullscreen(*self.windowSize)

        self.lastDrawTime = getPreciseTimeMs()
        self.drawableChildren = []

        self.task = RecurringTask(
            tkRoot=root,
            delayInMs=1,  # check on every mainloop run
            command=self.drawChildren)

        self.pack()

    def addDrawableChild(self, drawable):
        self.drawableChildren.append(drawable)

    def drawChildren(self):
        newTime = getPreciseTimeMs()
        timePassed = newTime - self.lastDrawTime
        if timePassed >= FullscreenCanvas.minFrameDelay:
            self.lastDrawTime = newTime
            self.flush()
            for drawable in self.drawableChildren:
                drawable.draw(timePassed)

    def flush(self):
        self.delete("all")

    def resizeCanvasToFullscreen(self, windowWidth, windowHeight):
        self.update()
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()
