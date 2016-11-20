import Tkinter as tk
from CameraImageProvider import CameraImageProvider
from RecurringTask import RecurringTask
from TransformationProvider import TransformationProvider

class ApplicationCanvas(tk.Canvas):
    def __init__(self, root):
        tk.Canvas.__init__(self, master=root, bg="white")
        windowHeight, windowWidth = self.getWindowSize()
        self.windowCenter = (windowWidth/2, windowHeight/2)
        self.resizeCanvasToFullscreen(windowHeight, windowWidth)

        self.cameraImageProvider = CameraImageProvider((windowWidth, windowHeight))
        self.cameraLookupTask = self.createCameraLookup()
        self.transformationProvider = TransformationProvider(self.cameraImageProvider)

        root.bind('<Return>', self.transformationProvider.initiateFrameTransformation)

        self.pack()

    def createCameraLookup(self):
        cameraLookupTask = RecurringTask(self.master, 50, ApplicationCanvas.updateCameraLookup, self)
        cameraLookupTask.start()
        return cameraLookupTask

    @staticmethod
    def updateCameraLookup(app):
        a = app.cameraImageProvider.getDisplayPhotoImage()
        app.create_image(app.windowCenter, image = a)

    @staticmethod
    def startTransformationJob(event):
        print "job started"

    def resizeCanvasToFullscreen(self, windowHeight, windowWidth):
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()

    def getWindowSize(self):
        self.update()
        windowWidth, windowHeight = (self.master.winfo_width(), self.master.winfo_height())
        return windowHeight, windowWidth

