s='Hello I Am!...'
print(s)
f_name=input("Enter Your First Name ")
m_name=input("Enter  your middle name ")
l_name=input("Enter your last name ")


#.format() method is STRING FORMATTING

s0="Your First Name is {} \nAnd\n Your Last Name is {}.".format(f_name,l_name)
s1="Hello {} {} ! Welcome to Learn Python from Scratch....".format(f_name,l_name)
print(s1)
s2="Hello {:10.6} {:10.5} ! Welcome to Learn Python from Scratch....".format(f_name,m_name,l_name)
#s2="Hello {:10.6} {2:10.5} ! Welcome to Learn Python from Scratch....".format(f_name,m_name,l_name)---error as  cannot switch from automatic field numbering to manual field specification
print(s2)
s3="Hello {f} {m} {l} ! Welcome to Learn Python from Scratch....".format(f=f_name,m=m_name,l=l_name)
print(s3)
s4="Hello {:10.6} {:10.5} ! Welcome to Learn Python from Scratch....".format(f_name,m_name,l_name)
print(s4)
s5="Hello {f:10.6} {m:10.5} {l:10.5} ! Welcome to Learn Python from Scratch....".format(f=f_name,m=m_name,l=l_name)
print(s5)
s6="Your First Name is {:10.6} \nAnd\n Your Last Name is {:10.6}.".format(f_name,l_name)
print(s6)
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))

# f-strings  method is STRING FORMATTING
name ="Akshit Mangotra"
age=21
print(f'Hello {name} your age is {age} years!')

