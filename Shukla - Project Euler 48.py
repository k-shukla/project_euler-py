'''Problem 48: The series, 1^1 + 2^2 + 3^3 + [...] + 10^10 = 10405071317.
   Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + [...] + 1000^1000.'''

running_sum = 0
for x in xrange(1, 1000):
    running_sum += x**x

running_str = str(running_sum)[::-1]
last_ten_rev = running_str[0:10]
last_ten = last_ten_rev[::-1]

print last_ten