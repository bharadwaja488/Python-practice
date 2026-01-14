#swap 2 numbers without using 3rd value
a=int(input("Enter first number: "))
b=int(input("Enter second nummber: "))
a,b=b,a
print("After swapping:")
print("a=",a)
print("b=",b)