import time
import numpy as np
import matplotlib.pyplot as plt
######selection sort######
def selectionSort(array):
    i=0
    while i<len(array):
        j=i
        k=i+1
        while k<len(array):
            if array[k]<array[j]:
                j=kk=k+1
        array[i],array[j]=array[j],array[i]
        i=i+1
sorts=[
    {
        "name":"Selection Sort",
        "sort":lambda arr:selectionSort(arr)
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