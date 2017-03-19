from AlgorithmBase import *
import time

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
            print process
            # run the process until it is complete
            theProcess.run(time)
            while theProcess.state is not ProcessState.complete:
                #increment the process progress
                theProcess.step(time)
                #increment the time step
                time += 1
            # the process finished, so add it to the stats
            self.stats.addProcessToStats(theProcess)

fcfs = FCFS('program3.txt')
