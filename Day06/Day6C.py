x=[2,3,4,5]
y=[-1,2,-2,1]
res=0.0
for i,j in zip(x,y):
    res+=(i-j)**2

print(res)
