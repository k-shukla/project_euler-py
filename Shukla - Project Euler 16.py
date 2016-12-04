'''Problem 16: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
   What is the sum of the digits of the number 2^1000?'''

awful_number = 2**1000

def digit_sum(n):
    running_sum = 0
    while n > 0:
        last_digit = n % 10
        running_sum += last_digit
        n = (n-last_digit)/10
    return running_sum

print digit_sum(awful_number)