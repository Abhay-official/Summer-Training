fo = open(r'C:\Python\abc.txt', 'w')
print("Name of file: ", fo.name)
print("Closed or not? ", fo.closed)
print("Opening mode: ", fo.mode)
fo.close()
print("Closed or not? ", fo.closed)


