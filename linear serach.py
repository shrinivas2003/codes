import time
import numpy as np
import matplotlib.pyplot as plt
def linear_search(A,x):
    for i in range(0,len(A)):
        if A[i]==x:
            print("search is success at position",i)
            return
    print("search is not success")
elements=np.array([i*1000 for i in range(1,40)])

plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,40):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    linear_search(a,1)
    end=time.time()
    times.append(end-start)
    print("time taken for linear search",i*1000,"elements is",end-start,"s")
plt.plot(elements,times,label="linear search")
plt.grid()
plt.legend()
plt.show()