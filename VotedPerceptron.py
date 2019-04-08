import numpy as np


class VotedPerceptron:
    def __init__(self, dataSet, t, b=0, l_rate=0.005):
        self.dataSet = dataSet
        self.t = t
        self.b = b
        self.l_rate = l_rate
        self.w = np.zeros(self.dataSet.numAttributes)
        self.v = []
        self.c = []
        self.bias = []

    def train(self):
        c = 1
        for epoch in xrange(self.t):
            for i in xrange(self.dataSet.size):
                prediction = np.sign(np.dot(self.w, self.dataSet.x[i]) + self.b)
                if prediction == 0:
                    prediction = 1
                if prediction != self.dataSet.y[i]:
                    self.w += (self.dataSet.y[i] * self.dataSet.x[i]) * self.l_rate
                    self.v.append(self.w)
                    self.c.append(c)
                    self.bias.append(self.b)
                    self.b += self.dataSet.y[i]
                    c = 1
                else:
                    c += 1

    def predict(self, x):
        p = 0
        for i in xrange(len(self.v)):
            prediction = np.sign(np.dot(self.v[i], x) + self.bias[i])
            p += self.c[i] * prediction
        result = np.sign(p)
        if result == 0:
            return 1
        return result


