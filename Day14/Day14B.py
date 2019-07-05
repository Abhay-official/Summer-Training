import math
data1=[5.1,3.5,1.4,0.2,'Iris-setosa']
data2=[5.4,3.9,1.7,0.4,'Iris-setosa']
def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

res=euclideanDistance(data1,data2,4)
print(res)
