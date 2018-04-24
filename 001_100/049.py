'''
Prime permutations
Problem 49 

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from sympy import primerange

PRIMES = list(primerange(1000,9999))

def cal(n):
    strN = str(n)
    myset = set()
    for i in strN:
        myset.add(i)
    return myset


result = []
for i in range(len(PRIMES) - 1):
    for j in range(i + 1,len(PRIMES)):
        if (PRIMES[j] * 2 - PRIMES[i]) in PRIMES:
            a = cal(PRIMES[i])
            b = cal(PRIMES[j])
            c = cal(PRIMES[j]*2-PRIMES[i])
            myset = a.union(b).union(c)
            if len(myset) == len(a) == len(b) == len(c):
                result.append((PRIMES[i], PRIMES[j], PRIMES[j]*2-PRIMES[i]))

print result