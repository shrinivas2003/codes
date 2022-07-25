import time
import numpy as np
import matplotlib.pyplot as plt
def binary_search_basic(arr,target):
    low,high=0,len(arr)
    while low<high:
        mid=(low+high)//2 #low +(high-low)//2 if cares about overflow
        if target<arr[mid]:
            high=mid
        elif target>arr[mid]:
            low=mid+1
        else:
            return mid
    return -1

elements=np.array([i*1000 for i in range(1,40)])
plt.xlabel('list length')
plt.ylabel('Time complexity')
times=list()
for i in range(1,40):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    binary_search_basic(a,1)
    end=time.time()
    times.append(end-start)
    print("time taken for binary search in",i*1000,"elements is",end-start,"s")
plt.plot(elements,times,label="Binary search")
plt.grid()
plt.legend()
plt.show()