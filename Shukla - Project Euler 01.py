# -*- coding: utf-8 -*-
'''Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The
   sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.'''

'''For the brute-force method, we simply do a loop and add the relevant terms to a running total.'''

running_sum = 0
for i in xrange(1000):
    if i % 3 == 0 or i % 5 == 0:
        running_sum += i

print running_sum

'''On the other hand, we can exploit the famous Gauss formula for the sum of all natural numbers from 1 to N, which
   is given by N × (N+1) / 2.0. We're interested in the sum of all multiples of 3 or 5 below 1000, which we
   recognise as 3 + 6 + 9 + [...] + 5 + 10 + 15 + [...]. Pulling out the common factors, this is simply
   3 × (1 + 2 + 3 + [...] + 999//3) + 5 × (1 + 2 + 3 + [...] + 999//5). (Note that this is up to 999//3 and 999//5
   rather than 1000//3 and 1000//5, since we're finding the sum of all the multiples of 3 or 5 *below* 1000.
   This, however, double-counts the sum 15 × (1 + 2 + 3 + [...] + 999//15), since both contain the sum
   15 + 30 + 45 + [...].'''

print (3 * (999//3 * (999//3 + 1) / 2)) + (5 * (999//5 * (999//5 + 1) / 2)) - (15 * (999//15 * (999//15 + 1) / 2))