import numpy as np


class Perceptron:
    def __init__(self, dataSet, b=0, l_rate=0.01):
        self.dataSet = dataSet
        self.w = np.zeros(self.dataSet.numAttributes)
        self.b = b
        self.l_rate = l_rate

    def train(self, maxIterations):
        numErrors = 1
        iterations = 0

        while numErrors != 0 and iterations < maxIterations:
            numErrors = 0
            for i in xrange(self.dataSet.size):
                prediction = self.predict(self.dataSet.x[i])
                if prediction != self.dataSet.y[i]:
                    error = self.dataSet.y[i] - prediction
                    self.b += self.l_rate * error
                    for j in xrange(self.dataSet.numAttributes):
                        self.w[j] += self.l_rate * error * self.dataSet.x[i][j]
                    numErrors += 1
            iterations += 1

    def predict(self, x):
        prediction = np.sign(np.dot(x, self.w) + self.b)
        if prediction == 0:
            return 1
        return prediction
