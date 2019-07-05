fo = open(r'C:\Python\student1.txt', 'r')

str1 = fo.read()
fo.close()

fo1 = open(r'C:\Python\student2.txt', 'w')
fo1.write(str1)
fo1.close()
print("Work done")
