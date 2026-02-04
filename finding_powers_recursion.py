def product_of_digits(n):
    if n == 0:                 
        return 1             

    digit = n % 10            
    return digit * product_of_digits(n // 10)

print(product_of_digits(234))
