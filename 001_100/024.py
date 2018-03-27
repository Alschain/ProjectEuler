'''
Lexicographic permutations
Problem 24 

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import gmpy2

NUMS = [i for i in range(0, 10)]

def get_ith(n):
    n = n - 1
    result = ''
    while n != 0:
        size = len(NUMS) - 1
        div, mod = divmod(n, gmpy2.fac(size))
        result += str(NUMS[div])
        n = mod
        del(NUMS[div])
    
    for i in range(len(NUMS)):
        result += str(NUMS[i])
    
    return result


print get_ith(1000000)