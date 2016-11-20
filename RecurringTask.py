class RecurringTask:
    def __init__(self,
                 tkRoot,
                 delayInMs,
                 staticMethod,
                 *methodArgs):
        self.tkRoot = tkRoot
        self.staticMethod = staticMethod
        self.methodArgs = methodArgs
        self.delay = delayInMs
        self.isJobRunning = False

    def start(self):
        self.isJobRunning = True
        RecurringTask.execute(self)

    @staticmethod
    def execute(asyncJob):
        if asyncJob.isJobRunning:
            asyncJob.staticMethod(*asyncJob.methodArgs)
            asyncJob.tkRoot.after(asyncJob.delay,
                                  RecurringTask.execute,
                                  asyncJob)

    def stop(self):
        self.isJobRunning = False
