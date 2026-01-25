#Write a python program to enter any number and calculate its factorial.
num=int(input("Enter a number: "))
factorial=1
for i in range(1,num+1):
    factorial = factorial*i
print("faactorial of",num,"is:",factorial) 