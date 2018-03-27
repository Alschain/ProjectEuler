'''
Digit factorials
Problem 34 

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import gmpy2

def digit_fac(n):
    n = str(n)
    temp = 0
    for i in range(len(n)):
        temp += gmpy2.fac(int(n[i]))
    return temp

result = 0
for i in range(10, 2540160):# 7 * fac(9)
    if i == digit_fac(i):
        result += i

print result