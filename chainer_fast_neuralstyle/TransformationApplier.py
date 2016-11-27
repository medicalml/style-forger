from chainer import serializers, cuda
from source.net import FastStyleNet
from source.generate import generate
import config

## TODO:
#  cant parse more than one at once because
#  instance is shared between threads
#  causing common model and ???
##

class TransformationApplier:
    def __init__(self, transferedArtStyles):
        self.model = FastStyleNet()
        self.modelPath = ""

    def transform(self, image, modelPath):
        self.loadModelFromPath(modelPath)
        return generate(self.model, image)


    def loadModelFromPath(self, modelPath):
        if self.modelPath != modelPath:
            self.modelPath = modelPath
            print "start loading model: ", modelPath
            serializers.load_npz(modelPath, self.model)
            if config.GPU_UNIT >= 0:
                cuda.get_device(config.GPU_UNIT).use() #assuming only one gpu
                self.model.to_gpu()
