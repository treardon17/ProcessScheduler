from AlgorithmBase import *
import time
import math
import pdb

class HRRN(AlgorithmBase):
    def __init__(self, filename):
        #initialize the parent class
        AlgorithmBase.__init__(self, filename)

    def reSortQueue(self, time):
        processList = []
        # for all the processes in the readyQueue
        for processID in self.readyQueue:
            # calculate the RR for each process before we put it into the queue
            self.processTable[processID].calculateRR()
            # append the pcb in the process table based on that ID
            processList.append(self.processTable[processID])
        # sort the list based on the calculated response ratio
        #   where the biggest ratio has priority
        processList.sort(key=attrgetter('responseRatio'), reverse=True)
        # empty the readyQueue and fill it with the new order for processes
        self.readyQueue = []
        for pcb in processList:
            self.readyQueue.append(pcb.ID)

    def run(self):
        time = 0
        # this will never change, because we always remove the first
        #   process from the readyQueue
        processIndex = 0
        while len(self.readyQueue) > 0:
            self.reSortQueue(time)
            theProcess = self.processTable[self.readyQueue[processIndex]]

            while theProcess.state is not ProcessState.complete:
                # we don't want to start the process until it's actually
                #   supposed to start, so we loop the time until the clock
                #   is at the start time of the process
                if time >= theProcess.processStart:
                    # increment the process progress
                    theProcess.step(time)
                # increment the time step
                time += 1
                # update the wait times on all the processes
                self.updateProcesses(time)
            # the process is complete, so we remove it from the readyQueue
            self.readyQueue.pop(processIndex)
            # the process finished, so add it to the stats
            self.stats.addProcessToStats(theProcess, time)
