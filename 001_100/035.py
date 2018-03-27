'''
Circular primes
Problem 35 

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def eladuosai(n): # get the primes
    l = list(range(1,n+1))
    l[0] = 0
    for i in range(2,n+1):
        if l[i-1] != 0 :
            for j in range(i*2,n+1,i):
                l[j-1] = 0
    result = [x for x in l if x != 0]
    return result

def even_judge(n):
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            return True
    return False

PRIMES = eladuosai(1000000)

count = 1

for n, prime in enumerate(PRIMES):
    strPrime = str(prime)
    if even_judge(prime):
        PRIMES[n] = 0
        continue
    for i in range(0,len(strPrime)):
        newPrime = strPrime[i:len(strPrime)] + strPrime[0:i]
        if int(newPrime) not in PRIMES:
            PRIMES[n] = 0
            break
    if prime == PRIMES[n]:
        count += 1

print count
