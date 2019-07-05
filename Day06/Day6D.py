x=[2,3,4,5]
y=[-1,2,-2,1]
z=[10,20,15,30,25,67]
print("x:",x)
print("y:",y)
print("z:",z)
res=[]
for i,j,k in zip(x,y,z):
    res.append(i+j+k)

print("res:",res)
