def sum_of_numbers(n):
    if n==0:
        return 0
    digit=n%10
    return digit+sum_of_numbers(n//10)
print(sum_of_numbers(1234))