import Tkinter as tk
from CameraImageProvider import CameraImageProvider
from RecurringTask import RecurringTask
from TransformationProvider import TransformationProvider
from helpers import resizeRawImage

class ApplicationCanvas(tk.Canvas):
    def __init__(self, root):
        tk.Canvas.__init__(self, master=root, bg="white")
        windowHeight, windowWidth = self.getWindowSize()
        self.windowSize = windowHeight, windowWidth
        self.windowCenter = (windowWidth/2, windowHeight/2)
        self.resizeCanvasToFullscreen(windowHeight, windowWidth)

        self.imgTransformed = None

        self.cameraImageProvider = CameraImageProvider()
        self.transformationProvider = TransformationProvider(self.cameraImageProvider)
        self.cameraLookupTask = self.createCameraLookup()

        root.bind('<Return>', self.transformationProvider.initiateFrameTransformation)

        self.pack()

    def createCameraLookup(self):
        cameraLookupTask = RecurringTask(self.master, 50, ApplicationCanvas.updateCameraLookup, self)
        cameraLookupTask.start()
        return cameraLookupTask

    @staticmethod
    def updateCameraLookup(self):
        self.img = resizeRawImage(self.cameraImageProvider.getRawImage(), self.windowSize)
        self.create_image(self.windowCenter, image = self.img)
        if self.transformationProvider.hasTransformedFrameWaiting():
            self.imgTransformed = resizeRawImage(self.transformationProvider.getTransformedFrame(), self.windowSize)
        if self.imgTransformed is not None:
            self.create_image(self.windowCenter, image = self.imgTransformed)

    def resizeCanvasToFullscreen(self, windowHeight, windowWidth):
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()

    def getWindowSize(self):
        self.update()
        windowWidth, windowHeight = (self.master.winfo_width(), self.master.winfo_height())
        return windowHeight, windowWidth

