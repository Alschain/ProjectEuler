'''
Amicable numbers
Problem 21 

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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


myarray = [0 for i in range(0,10001)]
for i in range(1,10001):
    if myarray[i] != 0:
        continue

    di = sum(factors(i)) - i
    if di > 10000 or i == di:
        continue
    elif i == sum(factors(di)) - di:
        myarray[i] = i
        myarray[di] = di


print sum(myarray)