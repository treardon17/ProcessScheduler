import sys
from FCFS import FCFS
from HRRN import HRRN
from RR import RR

class ProgramManager:
    def __init__(self):
        # this dictionary will hold the stats for each process function in a list
        self.statsDict = {'fcfs':[], 'rr':[], 'hrrn':[]}

        file = 'program1.txt'

        print "FCFS--------------------"
        fcfs = FCFS(file)
        print "RR----------------------"
        rr = RR(file, 5)
        print "HRRN--------------------"
        hrrn = HRRN(file)

program_manager = ProgramManager()
