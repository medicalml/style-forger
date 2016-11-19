from threading import Thread
import numpy as np

class AsyncTransformation(Thread):
    def __init__(self, transformationApplier, imageArray, listener):
        Thread.__init__(self)
        imageTransformed = transformationApplier.transform(imageArray)
        listener.receiveReference(imageTransformed)

    def run(self):
        transformedImage = self.transformer.transform(self.imageRaw, self.modelPath)
        self.notifyFunction(self.notifyObject, transformedImage)