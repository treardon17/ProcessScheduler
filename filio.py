import random
from PCB import *

class FileIO:

    #generates a file with a preformatted program that we can reuse later
    @staticmethod
    def generateRandomProgram(filename, numProcesses, maxLength):
        try:
            #create the file
            writeFile = open(filename, 'w+')
            currProcessCount = 0
            while currProcessCount < numProcesses:
                #we get a random process length (burst time) between 1 and 1000
                processLength = random.randrange(1, maxLength + 1)
                #we make a string with the processID on the left and the length
                #   on the right separated by a colon
                processString = str(currProcessCount) + ":" + str(processLength) + "\n"
                writeFile.write(processString)
                currProcessCount += 1
            writeFile.close()
        except IOError:
            print "Error creating/writing to file ", filename

    @staticmethod
    def generatePCBfromFile(filename):
        arr = []
        try:
            readfile = open(filename)
            for line in readfile:
                 ID, burst= line.split(":")
                 pcb = PCB(ID, burst)
                 arr.append(pcb)

        except IOError:
            print "Error reading from file ", filename
        return arr
