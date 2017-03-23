from AlgorithmBase import *
import time
import pdb

class FCFS(AlgorithmBase):
    def __init__(self, filename):
        #initialize the parent class
        AlgorithmBase.__init__(self, filename)
        self.run()
        self.stats.printStats()

    def run(self):
        time = 0
        for process in self.readyQueue:
            theProcess = self.processTable[process]
            while theProcess.state is not ProcessState.complete:
                # we don't want to start the process until it's actually
                #   supposed to start, so we loop the time until the clock
                #   is at the start time of the process
                if time >= theProcess.processStart:
                    # increment the process progress
                    theProcess.step(time)
                # increment the time step
                time += 1
                # update the wait times for all the processes
                self.updateProcesses(time)
            # the process finished, so add it to the stats
            self.stats.addProcessToStats(theProcess, time, self.numCores)
