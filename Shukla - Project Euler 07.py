'''Problem 7: By listing the first six prime numbers:
   2, 3, 5, 7, 11, and 13, we can see that the 6th
   prime is 13. What is the 10001st prime number?'''

prime_list = []
sieve_net = []
i = 2
while len(prime_list) < 10001:
    if i not in sieve_net:
        prime_list.append(i)
        for j in xrange(min(i**2, 114319), 114319, i):   #This relies on the bound of the nth prime as p_n < n log n + n log log n. Directly putting this formula into the recursion doesn't work. Instead, for n = 10001, this apparently gives 114319.
            sieve_net.append(j)
    i += 1
prime_list.sort()
prime_list.reverse()
    
print prime_list[0]