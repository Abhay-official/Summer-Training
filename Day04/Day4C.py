fo = open(r'C:\Python\abc.txt', 'w')
str1 = input("Enter text: ")

x = fo.write(str1)
print("No. of bytes written: ", x) 
fo.write("\nWe are using file handling")
fo.close()
print("Work done")
