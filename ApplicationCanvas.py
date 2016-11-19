import Tkinter as tk
from CameraImageProvider import CameraImageProvider

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

        ApplicationCanvas.updateCameraLookup(self)
        self.pack()

    @staticmethod
    def updateCameraLookup(app):
        a = app.cameraImageProvider.getDisplayPhotoImage()
        app.create_image(app.windowCenter, image = a)
        app.master.after(50, ApplicationCanvas.updateCameraLookup, app)

