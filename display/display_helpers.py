import sys
import time


def boundingBoxSquare(center, size):
    x, y = center
    return (
        x-size, # x of top-right corner
        y-size,  # y of top-right corner
        x+size, # x of top-right corner
        y+size)  # y of top-right corner

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