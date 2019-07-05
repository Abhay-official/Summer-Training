import random
import math
import sqlite3 as lite
import operator

def str_float(x):
    for i in range(0,len(x)-1):
        x[i] = float(x[i])
    return tuple(x)

def load_split_data(split,data1,data2):
    for line in open("iris.txt"):
        # print ( line[:-1].split(",") )
        temp = line[:-1].split(",") if line[-1]=="\n" else line.split(",")
        if random.random() <= split:
            data1.append(str_float(temp))
        else:
            data2.append(str_float(temp))

def euclideanDistance(instance1,instance2,length = 4):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x]-instance2[x],2)
    return math.sqrt(distance)

def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance[0],trainingSet[x])
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

data1 = []
data2 = []
load_split_data(0.8,data1,data2)
print(getNeighbors(data1,data2,5))
