'''def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
x=fact(3)
print(x)        

'''
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)

