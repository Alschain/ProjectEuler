'''
Non-abundant sums
Problem 23 

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import gmpy2
from gmpy2 import mpz

def factors(n):
    result = set()
    n = mpz(n)
    for i in range(1, gmpy2.isqrt(n) + 1):
        div, mod = divmod(n, i)
        if not mod:
            result |= {mpz(i), div}
    return result

ABUNDANT = []
CANS = set()

for i in range(1, 28124):
    if sum(factors(i)) > i * 2:
        ABUNDANT.append(i)

for i in range(len(ABUNDANT)):
    for j in range(len(ABUNDANT)):
        if ABUNDANT[i] + ABUNDANT[j] > 28123:
            continue
        CANS.add(ABUNDANT[i] + ABUNDANT[j])

myarray = [i for i in range(0,28124)]

for i in CANS:
    myarray[i] = 0

print sum(myarray)