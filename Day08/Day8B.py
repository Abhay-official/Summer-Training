try:
    import abc1
except Exception as ob:
    print(ob)

x=int(input('Enter a number: '))
y=int(input('Enter a number: '))
try:
    res=x/y
except Exception as ob:
    print('Division by 0 is not allowed')

else:
    print(x,'/',y,'=',res)

print('Thanks')
