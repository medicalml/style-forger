import Tkinter as tk
from Application import Application
from CameraImageStream import CameraImageStream
from TransformationProvider import TransformationProvider
import config
import Mocks
from facebook_upload import fb
from chainer_fast_neuralstyle.TransformationApplier import TransformationApplier

if config.MOCK_TRANSFORMATION_APPLIER:
    transformationApplier = Mocks.TransformationApplierMock(1)
else:
    transformationApplier = TransformationApplier()

if config.MOCK_FACEBOOK_UPLOAD:
    afterTransformationAction = Mocks.afterTransformationActionMock
else:
    afterTransformationAction = fb.upload_file

cameraImageStream = CameraImageStream()
transformationProvider = TransformationProvider(cameraImageStream, transformationApplier)

root = tk.Tk()
root.attributes("-fullscreen",True)
app = Application(root, cameraImageStream, transformationProvider, afterTransformationAction)
root.mainloop()