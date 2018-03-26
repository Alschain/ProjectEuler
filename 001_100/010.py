'''
Summation of primes
Problem 10 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

primes = eladuosai(2000000)

print sum(primes)