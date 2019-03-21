from chainer import serializers, cuda
from chainer_fast_neuralstyle.source.net import FastStyleNet
from chainer_fast_neuralstyle.source.generate import generate
import config
from datetime import datetime
import skimage.io as sio

## TODO:
#  cant parse more than one at once because
#  instance is shared between threads
#  causing common model and ???
##

class TransformationApplier:
    def transform(self, image, modelPath):
        time = datetime.now().strftime("%Y-%m-%dT%H-%M-%S") 
        
        sio.imsave(f'{config.IMAGES_SAVE_PATH}/{time}_before.png', image)
        self.loadModelFromPath(modelPath)
        result = generate(self.loadModelFromPath(modelPath), image, config.GPU_UNIT)
        sio.imsave(f'{config.IMAGES_SAVE_PATH}/{time}_after.png', result)
        return result

    def loadModelFromPath(self, modelPath):
        model = FastStyleNet()
        print("start loading model: ", modelPath)
        serializers.load_npz(modelPath, model)
        if config.GPU_UNIT >= 0:
            cuda.get_device(config.GPU_UNIT).use() #assuming only one gpu
            model.to_gpu()
        return model
