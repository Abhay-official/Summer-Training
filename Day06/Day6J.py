x=['python','java',89,99,93,7,11,'c++','ada']
def fun_str(a):
    if isinstance(a,str):
        return True
y=list(filter(fun_str,x))
z=list(filter(lambda a:isinstance(a,int),x))
p=list(filter(lambda a:isinstance(a,(int,float)),x))

print(y)
print(x)
print(p)
