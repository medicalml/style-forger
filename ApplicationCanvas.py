import Tkinter as tk
from CameraImageProvider import CameraImageProvider
from RecurringTask import RecurringTask
class ApplicationCanvas(tk.Canvas):
    def __init__(self, root):
        tk.Canvas.__init__(self, master=root, bg="white")
        self.update()
        windowWidth, windowHeight = (root.winfo_width(), root.winfo_height())
        self.windowCenter = (windowWidth/2, windowHeight/2)
        self["width"] = windowWidth
        self["height"] = windowHeight
        self.update()

        self.cameraImageProvider = CameraImageProvider((windowWidth, windowHeight))
        self.startDrawingCameraLookup()

        self.pack()

    def startDrawingCameraLookup(self):
        self.cameraLookupJob = RecurringTask(self.master, 50, ApplicationCanvas.updateCameraLookup, self)
        self.cameraLookupJob.start()
    @staticmethod
    def updateCameraLookup(app):
        a = app.cameraImageProvider.getDisplayPhotoImage()
        app.create_image(app.windowCenter, image = a)

    def __del__(self):
        self.cameraLookupJob.stop()
