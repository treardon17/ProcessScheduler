
#This is the start to the PCB and what the PCB values should have
class PCB:

    def __init__ (self, ID, burst):

        #getting the PCB.ID from the .txt file
        self.ID = ID
        #getting the PCB.burst from the .txt file
        self.burst = burst

        #The rest of these will be set later, so leave uninitialized
        self.priority = -1
        self.state = -1
        self.accumulatedTime = 0
        self.wait = 0
        self.response = 0

    #this should output string values of everything rather than pointer values
    def __str__ (self):
        return str(self.ID, self.burst, self.priority, self.accumulatedTime, self.wait, self.response)
