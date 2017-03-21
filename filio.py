import random
from PCB import *

class FileIO:

    # generates a file with a preformatted program that we can reuse later
    @staticmethod
    def generateRandomProgram(filename, numProcesses, maxLength):
        try:
            # create the file
            writeFile = open(filename, 'w+')
            currProcessCount = 0
            while currProcessCount < numProcesses:
                # the time in which the process enters the queue
                processEntry = random.randrange(0, maxLength*currProcessCount + 1)
                # we get a random process length (burstTime) between 1 and 1000
                processLength = random.randrange(1, maxLength + 1)
                # we make a string with the processID on the left
                #   the length of the process in the middle
                #   and the process entry point on the right
                #   separated by a colon
                processString = str(currProcessCount) + ":" + str(processLength) + ":" + str(processEntry) + "\n"
                writeFile.write(processString)
                currProcessCount += 1
            writeFile.close()
        # if we had a problem
        except IOError:
            print "Error creating/writing to file ", filename

    # generates the PCBs from the given file
    @staticmethod
    def generatePCBsFromFile(filename):
        # array to be returned
        arr = []
        try:
            # open the file and read it line by line
            readfile = open(filename)
            for line in readfile:
                # split each line by the colon
                #   create a PCB object,
                #   then append it to the returned array
                ID, burst, processStart = line.split(":")
                pcb = PCB(int(ID), int(burst), int(processStart))
                arr.append(pcb)
        # if we had a problem
        except IOError:
            print "Error reading from file ", filename
        # return the array
        return arr

# FileIO.generateRandomProgram('program1.txt', 200, 200)
