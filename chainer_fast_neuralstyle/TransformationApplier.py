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
    def transform(self, image, modelPath):
        self.loadModelFromPath(modelPath)
        return generate(self.loadModelFromPath(modelPath), image, config.GPU_UNIT)

    def loadModelFromPath(self, modelPath):
        model = FastStyleNet()
        print "start loading model: ", modelPath
        serializers.load_npz(modelPath, model)
        if config.GPU_UNIT >= 0:
            cuda.get_device(config.GPU_UNIT).use() #assuming only one gpu
            model.to_gpu()
        return model
