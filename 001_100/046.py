'''
Goldbach's other conjecture
Problem 46 

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

PRIMES = eladuosai(1000000)

i = 9
Flag = True
while Flag:
    if i in PRIMES:
        i += 2
        continue
    for j in PRIMES:
        if j >= i:
            break
        k = (i - j) / 2
        if not gmpy2.is_square(k):
            Flag = False
        else:
            Flag = True
            break
    i += 2

print i-2