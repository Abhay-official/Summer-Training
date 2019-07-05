d1 = {1 : 'one', 2 : 'two'}
print(d1.values())
print(d1.keys())
d1.clear()
print(d1)
d1 = {1 : 'one', 2 : 'two'}
d2 = d1.copy()
print(id(d1))
print(id(d2))
print(d1.get(1))
print(d1.get(2))
print(d1.get('one'))
print(d1.get(33))
print(d1.items())
print(d1.keys())
print(d1)
print('After popping: ', d1.pop(1))
print(d1)
print(d1.pop(2))
print(d1)
print('After popping: ', d1.pop(2, 100))

d1 = {1 : 'one', 2 : 'two'}
print(d1.popitem())
print(d1)
d1 = {1 : 'one', 2 : 'two'}
print(d1)
d1.get(5)
x = d1.get(5)
print(x)
print(d1.get(2))
print(d1)
print(d1.pop(2))
print(d1)
d1 = {1 : 'one', 2 : 'two'}
print(d1.pop(1))
print(d1)
d1 = {1 : 'one', 2 : 'two'}
a = dict(one = 1, two = 2, three = 3)
print('a: ', a)
b = {'one' : 1, 'two' : 2, 'three' : 3}
print('b: ', b)
c = dict(zip(['one', 'two', 'three'], [10, 20, 30]))
print('content is: ', c)
print(dict([('two', 2), ('one', 1), ('three', 3)]))
print(dict({'three' : 3, 'one' : 1, 'two' : 2 }))

d = dict({'three' : 3, 'one' : 1, 'two' : 2})
print(d)
e = dict([('two', 2), ('one', 1), ('three' , 3)])
print(e)
print(a == b == c == d == e)
print(len(a))
print(d['two'])
a = dict(one = 1, two = 2, three = 3)
f = {}
print(f.fromkeys(a))

