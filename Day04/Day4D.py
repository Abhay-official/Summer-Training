fo = open(r'C:\Python\abc.txt', 'w')
count = 0
while count < 5:
    str1 = input("Enter text: ")
    fo.write(str1 + '\n')
    count = count + 1
fo.close()
print('Work done')
