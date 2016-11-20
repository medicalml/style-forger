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

        self.isJobRunning = True
        self.execute()

    def execute(self):
        if self.isJobRunning:
            self.staticMethod(*self.methodArgs)
            self.tkRoot.after(self.delay,
                                  self.execute)

    def stop(self):
        self.isJobRunning = False
