import Tkinter as tk

import config
from helpers import resizeRawImage


class FullscreenCanvas(tk.Canvas):
    def __init__(self, root):
        tk.Canvas.__init__(self, master=root, bg="white")

        windowHeight, windowWidth = self.getWindowSize()
        self.windowSize = windowHeight, windowWidth
        self.windowCenter = (windowWidth / 2, windowHeight / 2)
        self.resizeCanvasToFullscreen(windowHeight, windowWidth)

        self.displayedImagesRefs = []

        self.pack()

    def flush(self):
        self.displayedImagesRefs = []
        self.delete("all")

    def resizeCanvasToFullscreen(self, windowHeight, windowWidth):
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()

    def getWindowSize(self):
        self.update()
        windowWidth, windowHeight = (self.master.winfo_width(), self.master.winfo_height())
        return windowHeight, windowWidth

    def displayImgArrayFullscreen(self, img):
        photoImage = resizeRawImage(img, self.windowSize)
        self.displayedImagesRefs.append(photoImage)
        self.create_image(self.windowCenter, image=photoImage)

    def displayCircle(self, text=""):
        self.create_oval(self.boundingBoxSquare(self.windowCenter, self.calculateCircleSize()),
                         fill=config.PRIMARY_COLOR,
                         outline="")

    def calculateCircleSize(self):
        return int(min(self.windowSize) * config.CIRCLE_RATIO)

    def boundingBoxSquare(self, center, size):
        x, y = center
        return (
            x-size, # x of top-right corner
            y-size,  # y of top-right corner
            x+size, # x of top-right corner
            y+size)  # y of top-right corner