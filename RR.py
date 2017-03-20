from AlgorithmBase import *
import time
import pdb

class RR(AlgorithmBase):
    def __init__(self, filename, quantum):
        #initialize the parent class
        AlgorithmBase.__init__(self, filename)
        self.quantum = quantum
        self.run()
        self.stats.printStats()

    def run(self):
        time = 0
        processIndex = 0
        while len(self.readyQueue) > 0:
            currProcess = self.readyQueue[processIndex]
            theProcess = self.processTable[currProcess]
            # print currProcess
            qCount = 0
            # run the process for the quantum, unless it is complete, then exit
            while (qCount < self.quantum and theProcess.state is not ProcessState.complete):
                # we only want to run the process when the process is supposed to start
                if time >= theProcess.processStart:
                    # increment the process progress
                    theProcess.step(time)
                    # increment the quantum
                    qCount += 1
                # increment the time step
                time += 1

            # if the process is terminated, remove it from the readyQueue.
            #   this will prevent the infinite loop
            if theProcess.state is ProcessState.complete:
                self.readyQueue.pop(processIndex)
                # since we removed an item from the readyQueue, we need to
                #   reset the index so one doesn't get skipped
                processIndex -= 1
                # the process finished, so add it to the stats
                self.stats.addProcessToStats(theProcess, time)

            # if we've processed everything, stop.
            #   if we've reached the end of our queue, reset the index to zero,
            #   otherwise increment the current process
            if processIndex == len(self.readyQueue) - 1:
                processIndex = 0
            else:
                processIndex += 1

rr = RR('program1.txt', 5)
