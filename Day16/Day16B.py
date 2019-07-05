import numpy as np
import sys
S=list(range(1000))
print("Memory occupied by list :",sys.getsizeof(999)*len(S))

D=np.arange(1000)
print("Memory occupied by numpy Array:",D.itemsize*D.size)

