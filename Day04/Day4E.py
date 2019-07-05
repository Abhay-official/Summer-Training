fo = open(r'C:\Python\abc.txt', 'w')

while True:
    str1 = input("Enter text: ")
    fo.write(str1 + '\n')
    choice = input("To exit type x: ")
    if choice == 'x' or choice == 'X':
        break
    else:
        continue
fo.close()
print('Work done')
