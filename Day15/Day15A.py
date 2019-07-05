import random
import math
import operator
def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]


def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=4
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)



def load_split_data(split,training_data=[],test_data=[]):
    for line in open("iris.txt","r"):
        temp=str_float(line[0:-1].split(","),4)
        if random.random()<=split:
            training_data.append(temp)
        else:
            test_data.append(temp)
    return(training_data, test_data)


def str_float(x,n):
    for i in range(n):
        x[i]=(float(x[i]))
    return(x)

def getAccuracy(testSet,predictions):
    correct=0
    for x in range(len(testSet)):
        if testSet[x][-1]==predictions[x]:
            correct+=1
    return(correct/float(len(testSet)))*100.0



def main():
    trainingSet=[]
    testSet=[]
    split=1
    trainingSet,_=load_split_data(split)
    sl=float(input('Enter saple length'))
    sw=float(input('Enter saple width'))
    pl=float(input('Enter petle l'))
    pw=float(input('Enter petle w'))
    testSet=[sl,sw,pl,pw,'']
    k=3
    neighbors=getNeighbors(trainingSet,testSet,k)
    result=getResponse(neighbors)
    print('>predicted='+str(result))
   
main()
