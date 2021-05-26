d1 = {'k1': 'Val1', "key2": 200}
print(d1)
print(d1["key2"])
# Note that key is always a string


# NESTED DICTIONARIES
d2 = {'k1': 105, 'k2': [105, 106, 109], 'k3': {'innerkey': 1000},'k4':['a','b','c','d']}
print(d2)
print(d2['k2'])
print(d2['k2'][2])  # prints element at 2nd index of the list at key= k2..ALSO .upper() at int list causes error as no upper is there for int
print(d2['k3'])
print(d2['k3']['innerkey'])  # prints element at innerkey at k3
print(d2['k4'][2].upper())


d2['k0']='Value0'
print(d2)#Note that the new value added here gets added at the last of the dict.
d2['k1']="Value 1"
print("AFTER UPDATING THE VALUE OF K1 THE DICTIONARY BECAME:")
print(d2)