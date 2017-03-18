from AlgorithmBase import *
import time

class FCFS(AlgorithmBase):
    def __init__(self, filename):
        #initialize the parent class
        AlgorithmBase.__init__(self, filename)
        self.run()
        self.stats.printStats()

    def run(self):
        currProcess = 0
        for process in self.readyQueue:
            theProcess = self.processTable[process]
            theProcess.run()
            print currProcess
            time.sleep(theProcess.burstTime * 0.001)
            theProcess.terminate()
            self.stats.addProcessToStats(theProcess)
            currProcess += 1


fcfs = FCFS('program1.txt')
