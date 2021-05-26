#NOTE: WE CAN EVEN USE SEMI COLON IF WE WANT....
#range(initial, last-1)
'''for i in range(0,10):
    if(i==2):
        continue
    elif i==4:
        pass
    elif i==6:
        break;
    print(i)'''

for i in range(25,10,-2):
    print(f'i is {i}')
#Use of sep(Seperator) and end togeather
print('akshit','mangotra', sep='', end='@')
print('gmail.com')

#TUPLE UNWRAPPING
list1=[(1,2),(3,4),(5,6)]
dict1={"k1":"val1","k2":"val2","k3":"val3"}
for a,b in list1 :
    print(a)

#NOTE:- 1. for i in dict1 only prints values..
#       2.for i in dict1.items() prints (key,value) as tuple. So that's why we can use tuple unwrapping in dict1.items()
for a,b in dict1.items() :
    print(b)



# while | while-else loop
x=0;
while x<5:
    print(x,'is ',sep="-")
    x+=1
else:
    print("X is Greater than 5")

