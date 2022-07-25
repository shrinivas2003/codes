from heapq import merge
import time
import numpy as np
import matplotlib.pyplot as plt
def mergesort(array):
    if len(array)>1:
        mid=int(len(array)/2)
        L=array[:mid]
        R=array[:mid]
        mergesort(L)
        mergesort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j< len(R):
            if L[i]<=R[j]:
                array[k]=L[i]
                i=i+1
                k=k+1
            elif L[i]>R[j]:
                array[k]=R[j]
                j=j+1
                k=k+1
            while i<len(L):
                array[k]=L[i]
                k=k+1
                i=i+1
            while j<len(R):
                array[k]=R[j]
                k=k+1
                j=j+1
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('Time complexity')
times=list()
for i in range(1,10):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    mergesort(a)
    end=time.time()
    times.append(end-start)
    print("Merge sort sorted ",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="Merge sort")
plt.grid()
plt.legend()
plt.show()