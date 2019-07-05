x=int(input('Enter a number: '))
y=int(input('Enter a number: '))
try:
    res=x/y
except ZeroDivisionError as ob:
    print(ob)
else:
    print(x,'/',y,'=',res)
finally:
    print('Resource deallocated')

