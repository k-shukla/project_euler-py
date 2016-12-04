# -*- coding: utf-8 -*-

'''Problem 4: A palindromic number reads the same both ways. The largest palindrome made from the
   product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product
   of two 3-digit numbers.'''

largest_generated_palindrome = 0
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        test_product = i*j
        if test_product > largest_generated_palindrome and str(test_product) == str(test_product)[::-1]:
            largest_generated_palindrome = test_product

print largest_generated_palindrome