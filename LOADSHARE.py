from AlgorithmBase import *

class LoadShare(AlgorithmBase):
    def __init__(self, filename, numCores):
        # initialize the parent class
        AlgorithmBase.__init__(self, filename)
        self.numCores = numCores
        self.run()
        self.stats.printStats()

    def run(self):
        time = 0
        # initialize the cores
        for core in range(self.numCores):
            # the core will be set to -1 if no process is currently running in it
            self.runningProcesses[core] = -1
        # run until the readyQueue is empty
        while len(self.readyQueue) > 0:
            # for the number of cores
            for coreID in range(self.numCores):
                # index out of bounds checking
                if len(self.readyQueue) > 0:
                    # assign a process ID to a core
                    #   this removes the first item of the readyQueue
                    #   and places it into the runningProcesses table
                    process = self.processTable[self.readyQueue[0]]
                    # if the core has nothing in it and the process start time is less than
                    #   or equal to the current time
                    if self.runningProcesses[coreID] == -1 and time >= process.processStart:
                        # remove the first item from the readyQueue and assign it to a core
                        self.runningProcesses[coreID] = self.readyQueue.pop(0)
            # for the number of cores we have running, get the coreID and the processID
            for (coreID, processID) in self.runningProcesses.items():
                # only execute this if the processID is valid
                if processID != -1:
                    # get the process from the process table
                    process = self.processTable[processID]
                    # update the process's progress
                    process.step(time)
                    # if the process is complete
                    if process.state is ProcessState.complete:
                        # clear the process from the core
                        self.runningProcesses[coreID] = -1
                        # save the statistics
                        self.stats.addProcessToStats(process, time, self.numCores)
            # increment the time
            time += 1
            # update the wait times of all the non-running/non-terminated processes
            self.updateProcesses(time)
