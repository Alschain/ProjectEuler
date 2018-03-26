'''
10001st prime
Problem 7 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
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

primes = eladuosai(1000000)

print primes[10000]