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
        # the entry point of the process
        self.processStart = processStart
        # The rest of these will be set later, so leave uninitialized
        self.priority = -1
        self.state = ProcessState.ready
        self.accumulatedTime = 0
        self.waitTime = 0
        self.executionTime = 0
        self.responseTime = 0
        # the current progress the process is at (should not exceed burst)
        self.currentTimeStep = 0
        # whether or not the process has started or not
        self.startedExecuting = False
        # the time the process was created (set in wait)
        self.creationTime = 0
        # the time the process was initially started
        self.startTime = 0
        # the last time the process started waiting
        self.lastWaitTime = 0
        # the last time the process was executing
        self.lastExecutionTime = 0
        # the process is waiting
        self.wait(processStart)

    def wait(self, time):
        if not self.startedExecuting:
            self.creationTime = time
        # set the state to ready because it's not running anymore (yet)
        self.state = ProcessState.ready
        # keep track of the last time we waited
        self.lastWaitTime = time

    def step(self, time):
        if self.currentTimeStep >= self.burstTime:
            self.terminate(time)
        else:
            #increment the current time step
            self.currentTimeStep += 1
            #increment the execution time
            self.executionTime += 1

    def run(self, time):
        if not self.startedExecuting:
            # keep track of the time we start waiting
            self.startTime = time
            # if we haven't seen the processor yet, we want to record
            #   the response time
            self.responseTime = time - self.creationTime
            self.startedExecuting = True

        # the process is now running
        self.state = ProcessState.running
        # get the current time it started running
        self.waitTime += (time - self.lastWaitTime)
        self.lastExecutionTime = time

    def terminate(self, time):
        self.wait(time)
        self.state = ProcessState.complete
        self.terminationTime = time
        self.accumulatedTime = self.terminationTime - self.creationTime

    # STATISTICS-------------------------------------------------
    def getTurnaroundTime(self):
        return self.waitTime + self.executionTime

    def getAccumulatedTime(self):
        return self.burstTime
        # if self.terminationTime:
        #     return self.terminationTime - self.creationTime
        # else:
        #     return self.currentTimeStep - self.creationTime

    def getWaitTime(self):
        return self.waitTime

    def getExecutionTime(self):
        return self.executionTime

    def getResponseTime(self):
        return self.responseTime
