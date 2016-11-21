import Tkinter as tk
from Application import Application
from CameraImageProvider import CameraImageProvider
from TransformationProvider import TransformationProvider
import config
import Mocks
from facebook_upload import fb
from chainer_fast_neuralstyle.TransformationApplier import TransformationApplier


transformationApplier = Mocks.TransformationApplierMock(1) if config.MOCK_TRANSFORMATION_APPLIER \
                        else TransformationApplier()

afterTransformationAction = Mocks.afterTransformationActionMock if config.MOCK_FACEBOOK_UPLOAD \
                            else afterTransformationAction = fb.upload_file

cameraImageProvider = CameraImageProvider()
transformationProvider = TransformationProvider(cameraImageProvider, transformationApplier)

root = tk.Tk()
root.attributes("-fullscreen",True)
app = Application(root, cameraImageProvider, transformationProvider, afterTransformationAction)
root.mainloop()