'''
Pentagon numbers
Problem 44 

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''

def check(num):
    i = 1
    while True:
        checkNum = i * (3 * i - 1) / 2
        if checkNum == num:
            return True
        if checkNum > num:
            return False
        i += 1

import sys

for i in range(1, 5000):
    a = i * (3 * i - 1) / 2
    for j in range(1, i):
        b = j * (3 * j - 1) / 2
        # print a, b
        if check(a - b) and check(a + b):
            print a, b, a - b
            sys.exit(0)