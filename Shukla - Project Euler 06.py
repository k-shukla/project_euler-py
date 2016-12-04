# -*- coding: utf-8 -*-

'''Problem 6: The sum of the squares of the
   first ten natural numbers is
   1^2 + 2^2 + [...] + 10^2 = 385. The square
   of the sum of the first ten natural numbers
   is (1 + 2 + [...] + 10)^2 = 55^2 = 3025.
   Hence the difference between the sum of the
   squares of the first ten natural numbers and
   the square of the sum is 3025 − 385 = 2640.

   Find the difference between the sum of the
   squares of the first one hundred natural
   numbers and the square of the sum.'''

import math

sum_of_squares = 100*(101)*(201)/6
square_of_sum = math.pow(100*(101)/2,2)

print int(abs(sum_of_squares - square_of_sum))