from __future__ import print_function
import time

from PIL import Image, ImageFilter
from chainer import cuda, serializers
from net import *

def generate(model, _imageArray, _gpu = -1, _padding=50, _medianFilter=3):
    xp = np if _gpu < 0 else cuda.cupy
    
    start = time.time()
    image = _imageArray.astype(dtype=np.float32).transpose(2, 0, 1)
    print("Started transforming image")
    image = image.reshape((1,) + image.shape)
    if _padding > 0:
        image = np.pad(image, [[0, 0], [0, 0], [_padding, _padding], [_padding, _padding]], 'symmetric')
    image = xp.asarray(image)
    x = Variable(image)
    
    y = model(x)
    result = cuda.to_cpu(y.data)
    
    if _padding > 0:
        result = result[:, :, _padding:-_padding, _padding:-_padding]
    result = np.uint8(result[0].transpose((1, 2, 0)))

    if _medianFilter > 0:
        pilImage = Image.fromarray(result)
        pilImage = pilImage.filter(ImageFilter.MedianFilter(_medianFilter))
        result = np.array(pilImage, dtype=np.uint8)

    print('Transforming took ', time.time() - start, 'sec')
    return result
