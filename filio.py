import random

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
            print "Error creating/writing to file", filename


FileIO.generateRandomProgram('program2.txt', 4000, 1000)
