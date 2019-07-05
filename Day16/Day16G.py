import numpy as np
a=np.array([(1,2,3),(3,4,5)])
print("a:\n",a)
print("Sum axis 0:",a.sum(axis=0))
print("Sum axis 1:",a.sum(axis=1))
