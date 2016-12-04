'''Problem 20: Find the sum of the digits in the number 100!.'''

import math

awful_number = math.factorial(100)

def digit_sum(n):
    running_sum = 0
    while n > 0:
        last_digit = n % 10
        running_sum += last_digit
        n = (n-last_digit)/10
    return running_sum

print digit_sum(awful_number)