from __future__ import division #for / to return float by default
from PIL import ImageTk

def resizeImage(image, size, cover = True):
    newSize = size if not cover else calculateSizeToCover(image.size, size)
    resized = image.resize(newSize)
    return ImageTk.PhotoImage(resized)

def calculateSizeToCover(srcSize, maxSize):
    srcWidth, srcHeight = srcSize
    maxWidth, maxHeight = maxSize

    ratio = max(maxWidth / srcWidth, maxHeight / srcHeight)
    return int(srcWidth*ratio), int(srcHeight*ratio)
