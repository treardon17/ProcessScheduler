class StatsManager:
    def __init__(self):
        self.accumulatedTime = 0
        self.avgThroughputTime = 0
        self.avgTurnaroundTime = 0
        self.avgWaitTime = 0
        self.avgResponseTime = 0
        self.avgContextSwitch = 0
        self.processorUtilization = 0
        self.speedupOverMultipleCPUs = 0
