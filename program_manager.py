from multiprocessing import Queue
from filio import *
from PCB import *
from stats import *

class ProgramManager:
    def __init__(self):
        #this dictionary will hold the stats for each process function in a list
        self.statsDict = {'fcfs':[], 'rr':[], 'hrrn':[]}
