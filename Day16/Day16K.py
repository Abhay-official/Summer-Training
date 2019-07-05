import numpy as np
import matplotlib.pyplot as plt

objects=('Python','C++','Java','Perl','Scala','Lisp')
x_pos=np.arange(len(objects))
performance=[10,3,6,8,2,7]

plt.bar(x_pos,performance,align='center')

plt.ylabel('Usage')
plt.title('Programming Language Usage')

plt.show()
