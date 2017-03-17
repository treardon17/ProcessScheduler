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
    def generatePCBsFromFile(filename):
        #array to be returned
        arr = []
        try:
            #open the file and read it line by line
            readfile = open(filename)
            for line in readfile:
                #split each line by the colon
                #   create a PCB object,
                #   then append it to the returned array
                ID, burst = line.split(":")
                pcb = PCB(ID, burst)
                arr.append(pcb)

        #if we had a problem
        except IOError:
            print "Error reading from file ", filename

        #return the array
        return arr

arr = FileIO.generatePCBsFromFile('program2.txt')
for item in arr:
    print item.state
