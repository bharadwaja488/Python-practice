'''#Write a function to find the factorial of a number 
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return (fact)
print(factorial(5))'''

#write a function that takes a list and returns the sum of all elements
def sum_of_list(num):
    total=0
    for num in num:
        total=total+num
    return total
my_list=[1,2,3,4,5]
print(sum_of_list(my_list))

        