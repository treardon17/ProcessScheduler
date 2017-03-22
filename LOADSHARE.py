from AlgorithmBase import *
import time
import pdb

class LoadShare(AlgorithmBase):
    def __init__(self, filename, numCores):
        self.numCores = numCores
        # initialize the parent class
        AlgorithmBase.__init__(self, filename)

    def run(self):
        time = 0
        # initialize the cores
        for core in range(self.numCores):
            self.runningProcesses[core] = -1

        while len(self.readyQueue) > 0:
            for coreID in range(self.numCores):
                if len(self.readyQueue) > 0:
                    # assign a process ID to a core
                    #   this removes the first item of the readyQueue
                    #   and places it into the runningProcesses table
                    process = self.processTable[self.readyQueue[0]]
                    if self.runningProcesses[coreID] == -1 and time >= process.processStart:
                        self.runningProcesses[coreID] = self.readyQueue.pop(0)

            for (coreID, processID) in self.runningProcesses.items():
                if processID != -1:
                    process = self.processTable[processID]
                    process.step(time)
                    if process.state is ProcessState.complete:
                        self.runningProcesses[coreID] = -1
                        self.stats.addProcessToStats(process,time*self.numCores)

            time += 1
            self.updateProcesses(time)