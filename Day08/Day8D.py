try:
    x=int(input('Enter a number: '))
    y=int(input('Enter a number: '))
except ValueError as ob:
    print(ob)
else:
    try:
        res=x/y
    except ZeroDivisionError as ob:
        print(ob)
    else:
        print(x,'/',y,'=',res)

print('Thanks')

