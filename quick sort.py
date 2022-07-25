import time
import numpy as np
import matplotlib.pyplot as plt
def partition(tempList,low,high):
    i=low-1
    pivot=tempList[high]
    for j in range(low, high):
        if tempList[j]<=pivot:
            i+=1
            tempList[i],tempList[j]=tempList[j],tempList[i]
    tempList[i+1],tempList[high]=tempList[high],tempList[i+1]
    return (i+1)
def quicksort(tempList,low,high):
    if low<high:
        pi=partition(tempList,low,high)
        quicksort(tempList,low,pi-1)
        quicksort(tempList,pi+1,high)
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('Time complexity')
times=list()
for i in range(1,10):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    quicksort(a,0,len(a)-1)
    end=time.time()
    times.append(end-start)
    print("quick sort sorted ",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="Merge sort")
plt.grid()
plt.legend()
plt.show()