import sys
import time


def boundingBoxSquare(center, size):
    x, y = center
    halfSize = size/2
    return (
        x-halfSize, # x of top-left corner
        y-halfSize,  # y of top-left corner
        x+halfSize, # x of bottom-right corner
        y+halfSize)  # y of bottom-right corner

# According to timeit.timeit sourcecode:
# On Windows, the best timer is time.clock
# On most other platforms the best timer is time.time
#
# Global in file to avoid checking platform on each execution
if sys.platform == 'win32':
    _default_timer = time.clock
else:
    _default_timer = time.time
def getPreciseTimeMs():
    return int(_default_timer() * 1000.0)