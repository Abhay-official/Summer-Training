x=input('Enter a number: ')
y=input('Enter a number: ')
try:
    res=int(x)/int(y)
except (ZeroDivisionError,ValueError,TypeError):
    print('Division by 0 not allowed or strings not allowed.\
Use integers only.')
except Exception as ob:
    print(ob)
else:
    print(x,'/',y,'=',res)
finally:
    print('Resource deallocated')
    print('Visit again at VIPS')

