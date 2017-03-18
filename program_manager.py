from multiprocessing import Queue
from filio import *
from PCB import *
from stats import *

class ProgramManager:
    def __init__(self):
        #this dictionary will hold the stats for each process function in a list
        self.statsDict = {'fcfs':[], 'rr':[], 'hrrn':[]}
        #a dictionary of process IDs as keys and PCBs as values
        # self.processTable = {}
        #the queue of ready processes waiting to be run
        # self.readyQueue = Queue(maxsize=0)
        # the dictionary of running processes
        # self.runningProcesses = {}

    # #TODO Implementation of the FCFS algorithm
    # def FCFS(self, filename):
    #     #create an object to keep track of stats
    #     fcfsStats = StatsManager()
    #     #create a list of PCBs
    #     pcbs = FileIO.generatePCBsFromFile(filename)
    #     #put the IDs of the PCB in the readyQueue
    #     #   and store the IDs and PCBs in the process table
    #     for pcb in pcbs:
    #         self.readyQueue.put(pcb.ID)
    #         self.processTable[pcb.ID] = pcb
    #
    #     #TODO ITEM
    #     #FCFS ALGORITHM WILL GO HERE
    #
    #     self.statsDict['fcfs'].append(fcfsStats)
    #     #zero out all of the global queues and dictionaries
    #     self.processTable.clear()
    #     self.runningProcesses.clear()
    #     self.readyQueue.clear()
