import PCB

class StatsManager:
    def __init__(self):
        self.numProcesses = 0
        self.accumulatedTime = 0
        self.accumulatedThroughputTime = 0
        self.accumulatedTurnaroundTime = 0
        self.accumulatedWaitTime = 0
        self.accumulatedResponseTime = 0
        self.accumulatedContextSwitch = 0
        self.accumulatedExecutionTime = 0
        self.processorUtilization = 0

    def addProcessToStats(self, process, currentTimeStep):
        self.numProcesses += 1
        self.accumulatedWaitTime += process.getWaitTime()
        self.accumulatedResponseTime += process.getResponseTime()
        self.accumulatedTurnaroundTime += process.getTurnaroundTime()
        self.accumulatedExecutionTime += process.getExecutionTime()
        # Accumulated time is the current time step because we don't want
        #   the processor to have 100% utilization statistics if there were
        #   gaps between processes.
        self.setAccumulatedTime(currentTimeStep)

    def setAccumulatedTime(self, accumulatedTime):
        self.accumulatedTime = accumulatedTime

    def getAvgWaitTime(self):
        if self.numProcesses > 0:
            return float(self.accumulatedWaitTime)/self.numProcesses
        else:
            return -1

    def getAvgResponseTime(self):
        if self.numProcesses > 0:
            return float(self.accumulatedResponseTime)/self.numProcesses
        else:
            return -1

    def getAvgTurnaroundTime(self):
        if self.numProcesses > 0:
            return float(self.accumulatedTurnaroundTime)/self.numProcesses
        else:
            return -1

    def getAvgExecutionTime(self):
        if self.numProcesses > 0:
            return float(self.accumulatedExecutionTime)/self.numProcesses
        else:
            return -1

    def getProcessorUtilization(self):
        return float(self.accumulatedExecutionTime)/float(self.accumulatedTime)

    def printStats(self):
        print "-----------------------------------------------"
        print "Number of processes: ", self.numProcesses
        print "Accumulated Time: ", self.accumulatedTime
        print "Average Wait Time: ", self.getAvgWaitTime()
        print "Average Response Time: ", self.getAvgResponseTime()
        print "Average Turnaround Time: ", self.getAvgTurnaroundTime()
        print "Total Execution Time: ", self.accumulatedExecutionTime
        print "Average Execution Time: ", self.getAvgExecutionTime()
        print "Processor Utilization: ", self.getProcessorUtilization()
