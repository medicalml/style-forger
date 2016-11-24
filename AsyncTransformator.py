from multiprocessing.pool import ThreadPool, TimeoutError

class AsyncTransformator(object):
    def __init__(self, transformationApplier):
        self.pool = ThreadPool(processes=1)
        self.transformationApplier = transformationApplier
        self.transformationPromise = None

    def startParallelTransformation(self, frame):
        self.transformationPromise = self.pool.apply_async(self.transformationApplier.transform,
                                                           (self.transformationApplier, frame))

    def isRunning(self):
        return self.transformationPromise is not None

    def hasAwaitingResult(self):
        return self.isRunning() and self.transformationPromise.ready()

    def getTransformedFrame(self):
        try:
            result = self.transformationPromise.get(timeout=0.1) #in seconds (?)
            self.transformationPromise = None
            return result
        except TimeoutError:
            print("getTransformedFrame timed-out, ask with hasAwaitingResult first to avoid blocking main thread")
            raise #rethrow
        except:
            print("Error raised while transforming frame")
            raise #rethrow
