def Adder(array1, array2,size):
        array3 = []

        for x in range(size):
            for j in range(len(array1[x])):
                    mytemplist = []
                    val1=array1[x][j]
                    val2=array2[x][j]
                    print("Val 1 is"+str(val1)+"and val 2 is "+str(val2))
                    mytemplist.append(val1+val2)
                   # print("array3 added element becomes"+str(array3[x][j]))
            array3.append(mytemplist)

        for i in range(size):
            for j in range(len(array3[i])):
                print(array3[i][j])






size = int(input("Enter the No of Rows"))
print("Enter the elements of Array 1 by space  & Press ENTER to fill next Row\n")
array1 = []
for x in range(size):
    array1.append([  int(y) for y in input("Enter Element for Row"+str(x+1)+":-").split()])

print("Array 1 is :\n")
for i in range(size):
    print(array1[i])
array2=[]
print("Enter the elements of Array 2 & Press ENTER to fill next Row\n")
for x in range(size):
    array2.append([int (y) for y in input("Enter Element for Row"+str(x+1)+":-").split()])
print("Array 2 is :\n")
for i in range(size):
    print(array2[i])


print("Returned Array is ")
print(Adder(array1,array2,size))


