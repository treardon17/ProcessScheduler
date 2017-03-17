    #TODO Implementation of the FCFS algorithm
class  FCFS(self, filename):
    def __init__(self):
        #create an object to keep track of stats
        fcfsStats = StatsManager()
        #create a list of PCBs
        pcbs = FileIO.generatePCBsFromFile(filename)
        #put the IDs of the PCB in the readyQueue
        #and store the IDs and PCBs in the process table
        for pcb in pcbs:
            self.readyQueue.put(pcb.ID)
            self.processTable[pcb.ID] = pcb

            #TODO ITEM
            #FCFS ALGORITHM WILL GO HERE

            self.statsDict['fcfs'].append(fcfsStats)
            #zero out all of the global queues and dictionaries
            self.processTable.clear()
            self.runningProcesses.clear()
            self.readyQueue.clear()
