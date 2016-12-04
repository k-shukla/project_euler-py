# -*- coding: utf-8 -*-

'''Problem 5: 520 is the smallest number that can be divided by
   each of the numbers from 1 to 10 without any remainder. What
   is the smallest positive number that is evenly divisible by
   all of the numbers from 1 to 20?'''

'''Note: This corresponds to the the product of all the primes
   from 1 to n, with the product of their maximum powers. So,
   for instance, the smallest positive number evenly divisible
   by all of the numbers from 1 to 20 is
   (2^4) × (3^2) × 5 × 7 × 9 × 11 × 13 × 17 × 19. For 2, since
   the maximum power of 2 less than 20 is 2^4 = 16, we have 2^4
   in this product. Conversely, since 5^2 = 25, we only have 5^1
   in this product.'''

import math

def sieve_of_eratosthenes(n):
    prime_list = []
    sieve_net = []
    for i in xrange(2, n+1):
        if i not in sieve_net:
            prime_list.append(i)
            for j in xrange(i**2, n+1, i):
                sieve_net.append(j)
    return [prime_list, sieve_net]

def minimal_prime_factorisation(k):
    minimal_prime_factorisation_list = []
    for l in sieve_of_eratosthenes(k)[0]:
        prime_power = int(math.floor(math.log(k, l)))
        minimal_prime_factorisation_list.extend([l]*prime_power)
        minimal_prime_factorisation_list.sort()
    return minimal_prime_factorisation_list

def min_lcm_min_PF(m):
    min_lcm_min_PF_m = 1
    for p in minimal_prime_factorisation(m):
        min_lcm_min_PF_m *= p
    return min_lcm_min_PF_m

print min_lcm_min_PF(20)