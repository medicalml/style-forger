import Tkinter as tk
from Application import Application
from CameraImageProvider import CameraImageProvider
from TransformationProvider import TransformationProvider

from chainer_fast_neuralstyle.TransformationApplier import TransformationApplier
transformationApplier = TransformationApplier()

cameraImageProvider = CameraImageProvider()
transformationProvider = TransformationProvider(cameraImageProvider, transformationApplier)

root = tk.Tk()
root.attributes("-fullscreen",True)
app = Application(root, cameraImageProvider, transformationProvider)
root.mainloop()