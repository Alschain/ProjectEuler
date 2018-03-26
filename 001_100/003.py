'''
Largest prime factor
Problem 3 

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import gmpy2

def eladuosai(n): # get the primes
    l = list(range(1,n+1))
    l[0] = 0
    for i in range(2,n+1):
        if l[i-1] != 0 :
            for j in range(i*2,n+1,i):
                l[j-1] = 0
    result = [x for x in l if x != 0]
    return result

primes = eladuosai(gmpy2.isqrt(600851475143))

for i in range(len(primes)-1 ,0 ,-1):
    if 600851475143 % primes[i] == 0:
        print primes[i]
        break