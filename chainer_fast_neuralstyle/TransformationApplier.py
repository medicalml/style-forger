from chainer import serializers, cuda
from source.net import FastStyleNet
from source.generate import generate
import config

## TODO:
#  cant parse more than one at once because
#  instance is shared between threads
#  causing common model and ???
##

class TransformationApplier(object):
    def __init__(self):
        self.model = FastStyleNet()
        modelPath = 'chainer_fast_neuralstyle/kandinsky_e2_full512.model'
        print "start loading model: ", modelPath
        serializers.load_npz(modelPath, self.model)
        if config.GPU_UNIT >= 0:
            cuda.get_device(config.GPU_UNIT).use() #assuming only one core
            self.model.to_gpu()

    @staticmethod
    def transform(self, image):
        return generate(self.model, image, config.GPU_UNIT)
