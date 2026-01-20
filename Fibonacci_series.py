#Fibonacci series: It is the sum of the previous two numbers 
n=int(input("Enter a number: "))
a=0
b=1
if(n<=0):
    print("Please enter a positive number: ")
elif (n==1):
    print(a)
else:
    print("Fibonacci series: ")
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
            