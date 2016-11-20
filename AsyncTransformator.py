from multiprocessing.pool import ThreadPool, TimeoutError

class AsyncTransformator():
    def __init__(self, transformationApplier, imageArray):
        self.pool = ThreadPool(processes=1)
        self.asyncResult = self.pool.apply_async(transformationApplier.transform,
                                                 (transformationApplier, imageArray))
        self.transformedFrame = None

    def isFinished(self):
        return self.asyncResult.ready()

    def getTransformedFrame(self):
        try:
            return self.asyncResult.get(timeout=0.5) #in seconds (?)
        except TimeoutError:
            print("AsyncTransformation timed-out, ask with isFinished first to avoid blocking main thread")
            raise #rethrow
