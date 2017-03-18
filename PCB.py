import time
import pdb

#Class to define constant values for processor state
class ProcessState:
    ready = 'READY'
    running = 'RUNNING'
    complete = 'COMPLETE'

#This is the start to the PCB and what the PCB values should have
class PCB:

    def __init__ (self, ID, burst, processStart):
        #getting the PCB.ID from the .txt file
        self.ID = ID
        #getting the PCB.burst from the .txt file
        self.burst = burst
        self.processStart = processStart
        #The rest of these will be set later, so leave uninitialized
        self.priority = -1
        self.state = ProcessState.ready
        self.accumulatedTime = 0
        self.waitTime = -processStart
        self.response = 0

        #the process is waiting
        self.wait()

    #this should output string values of everything rather than pointer values
    def __str__ (self):
        return str(self.ID, self.burst, self.priority, self.accumulatedTime, self.wait, self.response)

    def wait(self):
        #set the state to ready because it's not running anymore (yet)
        self.state = ProcessState.ready
        #keep track of the time we start waiting
        self.startTime = time.time()

    def run(self):
        #the process is now running
        self.state = ProcessState.running
        #get the current time it started running
        self.waitTime += (time.time() - self.startTime)

    def terminate(self):
        self.state = ProcessState.complete
        self.end = time.time()
        #TODO set the wait time/run time
