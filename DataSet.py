import numpy as np
import os
from io import open

HTRU_2_txt = os.path.isfile('DataSets/HTRU_2.txt')
Phishing_Websites_txt = os.path.isfile('DataSets/Phishing_Websites.txt')


class DataSet:
    def __init__(self, x=None, y=None, size=0, numAttributes=0, filename=""):
        self.x = x
        self.y = y
        self.size = size
        self.numAttributes = numAttributes
        self.filename = filename
        if filename != "":
            if "HTRU_2" in filename:
                if HTRU_2_txt:
                    self.populate(filename='DataSets/HTRU_2.txt')
                else:
                    with open(filename, 'r', encoding='utf-8') as fin:
                        data = fin.read().splitlines(True)
                        with open('DataSets/HTRU_2.txt', 'w') as fout:
                            fout.writelines(data[11:17909])
                    self.populate(filename='DataSets/HTRU_2.txt')

            elif "Phishing_Websites" in filename or "Training Dataset" in filename:
                if Phishing_Websites_txt:
                    self.populate(filename='DataSets/Phishing_Websites.txt')
                else:
                    with open(filename, 'r') as fin:
                        data = fin.read().splitlines(True)
                        data[-1] = data[-1].strip()
                        with open('DataSets/Phishing_Websites.txt', 'w') as fout:
                            fout.writelines(data[36:11901])
                    self.populate(filename='DataSets/Phishing_Websites.txt')

            else:
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
