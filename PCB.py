class PCB:

    def __init__ (self, ID, burst):
        self.ID = ID
        self.burst = burst
        self.priority = -1
        self.state = -1
        self.accumulatedTime = 0
        self.wait = 0
        self.response = 0
