try:
    x=-int(input("Enter x"))
    y=int(input("Enter y"))
    z=x/y
except:
    print("Exception occured")
else:
    print(z)
finally:
    print("This is finally block AND this must be executed...")
