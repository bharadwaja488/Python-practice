def is_armstrong(number):
    original_number = number
    num_digits = len(str(number))
    total = 0
    while number > 0:
        digit = number % 10
        total = total + (digit ** num_digits)
        number = number // 10
    return total == original_number 
num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong number")
else:
    print("No an Armstrong number: ")