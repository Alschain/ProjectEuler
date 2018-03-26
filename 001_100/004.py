'''
Largest palindrome product
Problem 4 

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import sys

def palindromic(n):
    n = str(n)
    return n == n[::-1]

result = 0

for i in range(999,99,-1):
    for j in range(999,99,-1):
        temp = i * j
        if palindromic(temp):
            if temp > result:
                result = temp

print result
            