import sys
from FCFS import FCFS
from HRRN import HRRN
from RR import RR
from LOADSHARE import LoadShare

class ProgramManager:
    def __init__(self):
        # this dictionary will hold the stats for each process function in a list
        self.statsDict = {'fcfs': [], 'rr': [], 'hrrn': [], 'loadshare': []}
        self.files = ['program1.txt', 'program2.txt', 'program3.txt', 'program4.txt', 'program5.txt']
        self.FCFSRun()
        self.RRRun()
        self.HRRNRun()
        self.LOADSHARERun()
        print self.statsDict

    def FCFSRun(self):
        print "FCFS----------------------------------"
        for file in self.files:
            print file
            fcfs = FCFS(file)
            self.statsDict['fcfs'].append(fcfs.stats)

    def RRRun(self):
        print "RR------------------------------------"
        quantum = 1
        while quantum < 10:
            print "QUANTUM: ", quantum
            for file in self.files:
                print file
                rr = RR(file, quantum)
                self.statsDict['rr'].append(rr.stats)
            quantum += 2

    def HRRNRun(self):
        print "HRRN----------------------------------"
        for file in self.files:
            print file
            hrrn = HRRN(file)
            self.statsDict['hrrn'].append(hrrn.stats)

    def LOADSHARERun(self):
        print "LOADSHARE-----------------------------"
        cores = 2
        while cores < 12:
            print "CORES: ", cores
            for file in self.files:
                print file
                loadshare = LoadShare(file, cores)
                self.statsDict['loadshare'].append(loadshare.stats)
            cores += 2

program_manager = ProgramManager()