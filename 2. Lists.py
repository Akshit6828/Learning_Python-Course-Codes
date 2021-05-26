l1 = [1, 'Two', 3.00, True, False]
l2 = ['a', 'x', 'l', 'b', 'n','a']
print(l1)
print(l2.count('a'))
print(len(l1))
print(l1[1:])
l1.append('FOUR')
print(l1)
print(l1.pop())  # pops last element in the list and prints it. Here by default the index is -1.
print(l1)
l1.pop(2)  # pops at index 1 permamently...
l2.sort()  # sort is a ind of special inplace method which actualy doesnt returns anything..NOTE LIST SHOULD BE Either Numerics or Alphabetic for sorting
print("L2.sort returntype is {} and type(l2) = {} and type(l2.sort()) is {} ".format(l2.sort(), type(l2),
                                                                                     type(l2.sort())))
print(l1)
print(l2)

'''l1.sort()
#TypeError: '<' not supported between instances of 'str' and 'int'''

print(l2[-1] + "is the element at index -1 before reversing")
l2.reverse()  # It reverses the list
print(l2[-1] + "is the element at index -1 after reversing")

nestedlist1 = ['one', [2.1, 2.2, 2.3], 'three', [4, [4.1, 4.2, 4.3]]]
print(nestedlist1[1])  # [2.1, 2.2, 2.3]
print(nestedlist1[1][2])  # 2.3
print(nestedlist1[3][1][2])  # 4.3

# Stack calling of the nested list (here list containing the dictionary).
listofdict = [{'key1': 'val1', 'key2': 'val2'}, {'Bhupi': 150, 'Monty': 200}]
print(listofdict)
print(listofdict[1])
print(listofdict[1]['Bhupi'])
