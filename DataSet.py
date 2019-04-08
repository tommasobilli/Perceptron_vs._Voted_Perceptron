import numpy as np


class DataSet:
    def __init__(self, x=None, y=None, size=0, numAttributes=0, filename=""):
        self.x = x
        self.y = y
        self.size = size
        self.numAttributes = numAttributes
        self.filename = filename
        if filename != "":
            self.populate(filename)

    def populate(self, filename):
        numLines = 0
        with open(filename) as f:
            for line in f:
                numLines += 1
            f.seek(0)
            line = f.readline()
            f.seek(0)
            numCols = len(line.split(","))
            self.x = np.empty(shape=(numLines, numCols - 1))
            self.y = np.empty(numLines)
            self.size = numLines
            self.numAttributes = numCols - 1
            k = 0
            with open(filename):
                for line in f:
                    item = line.split(",")
                    for i in xrange((numCols - 1)):
                        self.x[k, i] = float(item[i])
                    if float(item[numCols - 1]) == 1:
                        self.y[k] = 1
                    else:
                        self.y[k] = -1
                    k += 1
