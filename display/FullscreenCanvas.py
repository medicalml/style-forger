import Tkinter as tk
from helpers import RecurringTask
from display_helpers import  getPreciseTimeMs
import config


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
            command=self.redraw)

        self.pack()

    def addDrawableChild(self, drawable):
        self.drawableChildren.append(drawable)

    def removeDrawableChild(self, drawable):
        self.drawableChildren.remove(drawable)

    def redraw(self):
        newTime = getPreciseTimeMs()
        timePassed = newTime - self.lastDrawTime
        if timePassed >= FullscreenCanvas.minFrameDelay:
            self.lastDrawTime = newTime
            self.flush()
            self.drawChildren(timePassed)

            self.showFps(timePassed)

    def drawChildren(self, timePassed):
        for drawable in self.drawableChildren:
            drawable.draw(timePassed)

    def flush(self):
        self.delete("all")

    def resizeCanvasToFullscreen(self, windowWidth, windowHeight):
        self.update()
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()

    def showFps(self, timePassed):
        if config.CANVAS_SHOW_FPS:
            self.create_text(10, 10, anchor='nw',
                             fill='white',
                             font = ("Helvetica", 20),
                             text=str(1000 / timePassed))
