import PCB

class StatsManager:
    def __init__(self):
        self.numCores = 0
        self.numProcesses = 0
        self.accumulatedTime = 0
        self.accumulatedThroughputTime = 0
        self.accumulatedTurnaroundTime = 0
        self.accumulatedWaitTime = 0
        self.accumulatedResponseTime = 0
        self.accumulatedContextSwitch = 0
        self.accumulatedExecutionTime = 0
        self.processorUtilization = 0

    def addProcessToStats(self, process, currentTimeStep, numCores):
        self.numCores = numCores
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
        self.accumulatedTime = accumulatedTime + 1

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
        if self.accumulatedTime > 0:
            return float(self.getExecutionTime())/float(self.accumulatedTime)
        else:
            return -1

    def getExecutionTime(self):
        if self.numCores > 0:
            return float(self.accumulatedExecutionTime)/float(self.numCores)
        else:
            return -1

    def getThroughputTime(self):
        if self.accumulatedTime > 0:
            return float(self.numProcesses)/self.accumulatedTime
        else:
            return -1

    def getStatsString(self):
        stats_string = "*** \n"
        # stats_string += "Number of processes:       " + str(self.numProcesses) + "\n"
        # stats_string += "Accumulated Time:          " + str(self.accumulatedTime) + "\n"
        stats_string += "Average Wait Time:         " + str(self.getAvgWaitTime()) + "\n"
        stats_string += "Average Response Time:     " + str(self.getAvgResponseTime()) + "\n"
        stats_string += "Average Turnaround Time:   " + str(self.getAvgTurnaroundTime()) + "\n"
        # stats_string += "Throughput Time:           " + str(self.getThroughputTime()) + "\n"
        # stats_string += "Total Execution Time:      " + str(self.getExecutionTime()) + "\n"
        # stats_string += "Average Execution Time:    " + str(self.getAvgExecutionTime()) + "\n"
        # stats_string += "Processor Utilization:     " + str(self.getProcessorUtilization()) + "\n"
        stats_string += "***"
        return stats_string

    def printStats(self):
        print self.getStatsString()
