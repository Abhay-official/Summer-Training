try:
    fh=open(r'c:\python\Python37-32\student.txt','r')
    fh.write('This is my test file for exception handling')
except Exception as ob:
    print(ob)
finally:
    print("Error: can't find file or read data")
    fh.close()
print('thanks')
