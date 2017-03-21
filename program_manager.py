import sys
from FCFS import FCFS
from HRRN import HRRN
from RR import RR

class ProgramManager:
    def __init__(self):
        # this dictionary will hold the stats for each process function in a list
        self.statsDict = {'fcfs':[], 'rr':[], 'hrrn':[]}

        if len(sys.argv) > 1:
            # get the file to read from (the second argument)
            filename = sys.argv[1]
            algorithm = sys.argv[0]
            program = None
            if algorithm is 'fcfs':
                program = FCFS(filename)
            elif algorithm is 'rr':
                program = RR(filename)
            elif algorithm is 'hrrn':
                program = HRRN(filename)

            self.statsDict[algorithm].append(program.stats)


program_manager = ProgramManager()