import numpy as np
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)

a=a.reshape(4,2)
print(a)

a=np.array([(1,2,3,4),(13,14,15,16)])
print(a[0,2])
print(a[1,2])
print(a[0:,3])
a=np.array([(1,2,3,4),(13,14,15,16),(21,22,23,24)])
print('out:',a[0:,3])
print(a[0:2,3])
a=np.linspace(1,3,5)
print(a)
a=np.linspace(1,3,10)
print(a)
