def printinfo(arg1,*vartuple):
    print("Output: ",arg1)
    print("Contents of variable length tuple is: ",end='')
    for var in vartuple:
        print(var,end=' ')
    print()
    return None

if __name__ == "__main__":
    printinfo(10)
    printinfo(70,60,50)
    printinfo(10,20,"AK","GOel",90)
