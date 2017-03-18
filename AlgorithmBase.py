from filio import *
from stats import *
from operator import attrgetter

class AlgorithmBase:
    def __init__(self, filename):
        self.processTable = {}
        # a dictionary of process IDs as keys and PCBs as values
        self.processTable = {}
        # the queue of ready processes waiting to be run
        self.readyQueue = []
        # the dictionary of running processes
        self.runningProcesses = {}
        #create an object to keep track of stats
        self.stats = StatsManager()
        #create a list of PCBs
        pcbs = FileIO.generatePCBsFromFile(filename)
        #sort on the processStart time
        pcbs.sort(key=attrgetter('processStart'))
        #put the IDs of the PCB in the readyQueue
        #and store the IDs and PCBs in the process table
        for pcb in pcbs:
            self.readyQueue.append(pcb.ID)
            self.processTable[pcb.ID] = pcb

    def cleanup(self):
        #zero out all of the global queues and dictionaries
        self.processTable.clear()
        self.runningProcesses.clear()
        self.readyQueue.clear()
