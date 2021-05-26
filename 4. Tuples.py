t1=(1,2,3,1,2,1,2,1,1,1,)
print(t1.count('1'))
print(t1.count(1))#Returns count of element 1 present else returns 0 as output
print(t1[-1])#indexing
print(t1[2:])#Slicing
print(t1.index(2))#prints 1st occurence index of 2
print(t1.index(2,3))#prints 1st occurence index of 2 starting searching from initial index=3
#t1[1]='NEW ELEMENT'=== error that tuple item doesnot support item assigment


#NESTED TUPLE...
t2=(1,2,[3,4,5])
t2[2][1]='NEW VAL'
print(t2)#Thus note here that if there is a list inside a tuple, we can alter the list but we cannot alter the tuple. ie we cannot assign a new list to the older one.

