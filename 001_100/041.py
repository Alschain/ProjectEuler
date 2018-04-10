'''
Pandigital prime
Problem 41 

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import gmpy2

def judge_prime(n):
    if n % 2 == 0 or n == 1:
        return False
    
    for i in range(3, gmpy2.isqrt(n)):
        if n % i == 0:
            return False
    
    return True

def judge_pandigital(n):
    strN = str(n)
    tempSet = set()
    for i in strN:
        tempSet.add(int(i))
    if len(tempSet) == len(strN) and sum(tempSet) == (len(strN) * (len(strN) + 1 ) / 2) and 0 not in tempSet:
        return True
    return False


for i in range(987654321, 0, -1):
    if not judge_pandigital(i):
        continue
    if judge_prime(i):
        print i
        break