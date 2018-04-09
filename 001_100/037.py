'''
Truncatable primes
Problem 37 

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import gmpy2

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, gmpy2.isqrt(n) + 1):
        if n % i == 0:
            return False    
    return True

count = 0
start = 11
result = 0

while(True):
    strStart = str(start)
    length = len(strStart)
    myFlag = True
    if not is_prime(start):
        start += 1
        continue

    for i in range(1, length):
        if is_prime(int(strStart[i:length])) and is_prime(int(strStart[0:length - i])):
            continue
        else:
            myFlag = False
            break

    if myFlag:
        count += 1
        result += start
        print start
    start += 1
    
    if count == 11:
        break

print result