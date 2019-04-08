import numpy as np
from random import sample
import random
import copy
import Perceptron as p
import VotedPerceptron as vp
import DataSet as ds


def holdoutValidation(dataset):
    x = dataset.x
    y = dataset.y
    size = dataset.size
    trainingSize = size / 100 * 80  # <-------------------------------------------------------- set size of training set
    randomList = sample(range(size), trainingSize)
    # sort in descending order to later remove the correct entries from the initial dataset
    randomList.sort(reverse=True)
    xTraining = np.empty(shape=(trainingSize, dataset.numAttributes))
    yTraining = np.empty(trainingSize)

    for i in xrange(trainingSize):
        xTraining[i] = x[randomList[i]]
        x = np.delete(x, randomList[i], 0)
        yTraining[i] = y[randomList[i]]
        y = np.delete(y, randomList[i], 0)

    xTest = x
    yTest = y

    trainingSet = ds.DataSet(xTraining, yTraining, trainingSize, dataset.numAttributes)
    testSet = ds.DataSet(xTest, yTest, size - trainingSize, dataset.numAttributes)

    test(trainingSet, testSet)


def kFoldCrossValidation(k, dataset):
    perceptronAccuracies = []
    votedPerceptronAccuracies = []
    x = dataset.x
    y = dataset.y
    size = dataset.size
    subDataSize = size / k
    # shuffle dataset
    randomx = copy.deepcopy(x)
    randomy = copy.deepcopy(y)
    randomList = random.sample(xrange(size), size)
    for i in xrange(0, size):
        randomx[i] = x[randomList[i]]
        randomy[i] = y[randomList[i]]
    x = randomx
    y = randomy
    for i in xrange(0, k):
        if i == k - 1:
            xtest = x[i * subDataSize:]
            ytest = y[i * subDataSize:]
            xtrain = x[0:i * subDataSize]
            ytrain = y[0:i * subDataSize]
        else:
            xtest = x[i * subDataSize:i * subDataSize + subDataSize]
            ytest = y[i * subDataSize:i * subDataSize + subDataSize]
            if i == 0:
                xtrain=x[i * subDataSize + subDataSize:]
                ytrain=y[i * subDataSize + subDataSize:]
            else:
                xtrain = x[:i * subDataSize]
                xtrain = np.concatenate((xtrain, x[i * subDataSize + subDataSize:]))
                ytrain = y[:i * subDataSize]
                ytrain = np.append(ytrain, y[i * subDataSize + subDataSize:])

        trainingSet = ds.DataSet(xtrain, ytrain, len(ytrain), dataset.numAttributes)
        testSet = ds.DataSet(xtest, ytest, len(ytest), dataset.numAttributes)
        perceptronAccuracy, votedPerceptronAccuracy = test(trainingSet, testSet)
        perceptronAccuracies.append(perceptronAccuracy)
        votedPerceptronAccuracies.append(votedPerceptronAccuracy)

    avgPerceptronAccuracy = round(sum(perceptronAccuracies) / k, 2)
    avgVotedPerceptronAccuracy = round(sum(votedPerceptronAccuracies) / k, 2)
    print("")
    print("Perceptron average accuracy: {}%.".format(avgPerceptronAccuracy))
    print("Voted perceptron average accuracy: {}%.".format(avgVotedPerceptronAccuracy))
    print("")
    print("")


def test(trainingSet, testSet):
    perceptron = p.Perceptron(trainingSet)
    perceptron.train(100)   # <--------------------------------------------------------- adjust max number of iterations
    votedPerceptron = vp.VotedPerceptron(trainingSet, 100)  # <--------------------------------- adjust number of epochs
    votedPerceptron.train()

    perceptronErrors = 0
    votedPerceptronErrors = 0
    perceptronConfusionMatrix = np.zeros(shape=(2, 2))
    votedPerceptronConfusionMatrix = np.zeros(shape=(2, 2))

    for i in xrange(testSet.size):
        perceptronPrediction = perceptron.predict(testSet.x[i])
        if perceptronPrediction != testSet.y[i]:
            perceptronErrors += 1
            if perceptronPrediction == 1:
                perceptronConfusionMatrix[1][0] += 1    # False positive
            else:
                perceptronConfusionMatrix[0][1] += 1    # False negative
        else:
            if perceptronPrediction == 1:
                perceptronConfusionMatrix[0][0] += 1    # True positive
            else:
                perceptronConfusionMatrix[1][1] += 1    # True negative

        votedPerceptronPrediction = votedPerceptron.predict(testSet.x[i])
        if votedPerceptronPrediction != testSet.y[i]:
            votedPerceptronErrors += 1
            if votedPerceptronPrediction == 1:
                votedPerceptronConfusionMatrix[1][0] += 1   # False positive
            else:
                votedPerceptronConfusionMatrix[0][1] += 1   # False negative
        else:
            if votedPerceptronPrediction == 1:
                votedPerceptronConfusionMatrix[0][0] += 1   # True positive
            else:
                votedPerceptronConfusionMatrix[1][1] += 1   # True negative

    perceptronAccuracy = round((testSet.size - perceptronErrors) / float(testSet.size) * 100, 2)
    votedPerceptronAccuracy = round((testSet.size - votedPerceptronErrors) / float(testSet.size) * 100, 2)

    print("Test set size: {}".format(testSet.size))
    print("Perceptron errors: {} | Accuracy: {}%.".format(perceptronErrors, perceptronAccuracy))
    print("Perceptron confusion matrix:")
    print(perceptronConfusionMatrix)
    print("Voted perceptron errors: {} | Accuracy: {}%.".format(votedPerceptronErrors, votedPerceptronAccuracy))
    print("Voted perceptron confusion matrix:")
    print(votedPerceptronConfusionMatrix)
    print("")
    return perceptronAccuracy, votedPerceptronAccuracy
