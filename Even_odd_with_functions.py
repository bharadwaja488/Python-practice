#Write a function that takes a list of numbers a nd return how many numbers are even andhow many are odd??
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return even_count,odd_count
result = count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Even count:",result[0])
print("odd count:",result[1])