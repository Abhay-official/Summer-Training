items=['egg','milk','butter','peanuts','oats','honey']
for i in enumerate(items):
    print(i,end=',')#tuples with index and element of iterator

print('a')
items=['cup','pen','book']
for i in enumerate(items,100):
    print(i,end=',')
    
