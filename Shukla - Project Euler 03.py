'''Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
   What is the largest prime factor of the number 600851475143?'''

num_of_interest = 600851475143

for i in xrange(2, int(num_of_interest**0.5)+1):
    if num_of_interest % i == 0:
        if i != num_of_interest:
            num_of_interest = num_of_interest / i
        else:
            print num_of_interest