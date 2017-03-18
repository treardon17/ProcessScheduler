import time

# Class to define constant values for processor state


class ProcessState:
    ready = 'READY'
    running = 'RUNNING'
    complete = 'COMPLETE'


# This is the start to the PCB and what the PCB values should have


class PCB:

    def __init__ (self, ID, burstTime, processStart):
        # getting the PCB.ID from the .txt file
        self.ID = ID
        # getting the PCB.burstTime from the .txt file
        self.burstTime = burstTime
        self.processStart = processStart
        # The rest of these will be set later, so leave uninitialized
        self.priority = -1
        self.state = ProcessState.ready
        self.accumulatedTime = 0
        self.waitTime = 0
        self.executionTime = 0
        self.responseTime = 0
        self.startedExecuting = False

        # the time the process was created
        self.creationTime = 0
        # the time the process was initially started
        self.startTime = 0
        # the last time the process started waiting
        self.lastWaitTime = 0
        # the last time the process was executing
        self.lastExecutionTime = 0
        # the process is waiting
        self.wait()

    def wait(self):
        currTime = time.time()
        if not self.startedExecuting:
            self.creationTime = time.time()
        # set the state to ready because it's not running anymore (yet)
        self.state = ProcessState.ready
        # keep track of the last time we waited
        self.lastWaitTime = currTime
        # keep track of the total amount of time we've been executing
        #   only increment the execution time if we've actually executed before
        if self.lastExecutionTime > 0:
            self.executionTime += currTime - self.lastExecutionTime

    def run(self):
        currTime = time.time()
        if not self.startedExecuting:
            # keep track of the time we start waiting
            self.startTime = currTime
            # if we haven't seen the processor yet, we want to record
            #   the response time
            self.responseTime = currTime - self.creationTime
            self.startedExecuting = True

        # the process is now running
        self.state = ProcessState.running
        # get the current time it started running
        self.waitTime += (currTime - self.lastWaitTime)
        self.lastExecutionTime = currTime

    def terminate(self):
        currTime = time.time()
        self.wait()
        self.state = ProcessState.complete
        self.terminationTime = currTime
        self.accumulatedTime = self.terminationTime - self.creationTime

    # STATISTICS-------------------------------------------------
    def getTurnaroundTime(self):
        return self.waitTime + self.executionTime

    def getAccumulatedTime(self):
        if self.terminationTime:
            return self.terminationTime - self.creationTime
        else:
            return time.time() - self.creationTime

    def getWaitTime(self):
        return self.waitTime

    def getExecutionTime(self):
        return self.executionTime

    def getResponseTime(self):
        return self.responseTime
