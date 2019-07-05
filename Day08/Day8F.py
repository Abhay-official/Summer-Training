x=input('Enter a number: ')
y=input('Enter a number: ')
try:
    res=x+y
    print(res)
    res=x/y
    res=int(x)/int(y)
except ZeroDivisionError:
    print('Division by 0 not allowed.')
except ValueError:
    print('Strings are not allowed.please input integer only')
except TypeError:
    print('Division on strings not allowed')
except Exception as ob:
    print(ob)
else:
    print(x,'/',y,'=',res)
finally:
    print('Resource deallocated')

