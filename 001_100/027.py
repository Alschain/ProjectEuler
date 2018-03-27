'''
Quadratic primes
Problem 27

https://projecteuler.net/problem=27
'''

import gmpy2
def is_prime(n):
    for i in range(2, gmpy2.isqrt(n)):
        if n % i == 0:
            return False
    
    return True

def eladuosai(n): # get the primes
    l = list(range(1,n+1))
    l[0] = 0
    for i in range(2,n+1):
        if l[i-1] != 0 :
            for j in range(i*2,n+1,i):
                l[j-1] = 0
    result = [x for x in l if x != 0]
    return result

Bs = eladuosai(1000)
PRIMES = eladuosai(2000)

greatest = 0
result = 0
for b in Bs:
    for i in PRIMES:
        a = i - b - 1
        if a < -999 or a > 999:
            continue
        k = 0
        while True:
            inputN = k * k + k * a + b
            if inputN < 0 or not is_prime(input):
                if k > greatest:
                    greatest = k
                    result = a * b
                break
            k += 1

print result