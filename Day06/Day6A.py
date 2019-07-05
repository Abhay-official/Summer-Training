x=[11,8,5,21,9,11,6,9,21,8,7]
print(x)
y=[]
for i in x:
    if i not in y:
        y.append(i)

print(y)
