import time
import numpy as np
import matplotlib.pyplot as plt
######bubble sort#########
def BubbleSort(array):
    n=len(array)-1
    while n >=1:
        i=0
        while i <n:
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
            i=i+1
        n=n-1
sorts=[
    {
        "name":"Bubble sort",
        "sort":lambda arr:BubbleSort(arr)
    }
]
elements=np.array([i*1000 for i in range(1,5)])
plt.xlabel('list length')
plt.ylabel('Time complexity')
elements=np.array([i*1000 for i in range(1,5)])
plt.xlabel('list length')
plt.ylabel('Time complexity')
for sort in sorts:
    times=list()
    start_all=time.time()
    for i in range(1,5):
        start=time.time()
        a=np.random.randint(1000,size=i*1000)
        sort["name"]
        end=time.time()
        times.append(end-start)
    end_all=time.time()
    print(sort["name"],"Sorted Elements in",end_all-start_all,"s")
    plt.plot(elements,times,label=sort["name"])
plt.grid()
plt.legend()
plt.show()