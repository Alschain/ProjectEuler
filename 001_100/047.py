'''
Distinct primes factors
Problem 47 

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

from sympy.ntheory import factorint


start = 2
while True:
    if len(factorint(start)) != 4:
        start += 1
        continue
    if len(factorint(start + 1)) != 4:
        start += 2
        continue
    if len(factorint(start + 2)) != 4:
        start += 3
        continue
    if len(factorint(start + 3)) != 4:
        start += 4
        continue
    print start
    break