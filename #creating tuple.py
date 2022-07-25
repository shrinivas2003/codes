#creating tuple
t1=(0, )#A one item tuple(not an expression)
t2=(0,1,2,3)#A four items tuple
t3=0,1,2,3 #same as above without parenthesis
t3=('abc',('def','ghi'))
print(t1[0])
print(t3[1:3])#slice
print(len(t3))#length
tup=(1, "a","string", 1+2)
print(tup)