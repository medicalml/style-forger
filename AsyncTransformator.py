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
            result = self.asyncResult.get(timeout=0.1) #in seconds (?)

            self.pool.terminate()
            self.pool.join()
            return result

        except TimeoutError:
            print("AsyncTransformation timed-out, ask with isFinished first to avoid blocking main thread")
            raise #rethrow
