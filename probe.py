def is_prime(number):
    i = 0
    sum = 0
    while i <= number:
        if i < 5:
            sum = sum + i
            i = i + 1
        elif i < 10:
            sum = sum + 3
            i = i + 1
        elif i == 10:
            return sum
print(is_prime(15))