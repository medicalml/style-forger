import Tkinter as tk
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