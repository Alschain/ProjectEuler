'''

'''

'''
With Fermat's little theorem

for all positive interger a, a = 1 mod p

then 10^(p-1) = 1 mod p

let 10^(p-1) - 1 = kp

then 1 / p equals k / {9...9} (p-1)

so the recurring cycle length is p-1 or the divisor of p-1
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

def get_recurring_length(n):
    count = 1
    while True:
        if pow(10, count) % n == 1:
            return count
        count += 1
PRIMES = eladuosai(1000)

greatest = 1
result = 1

print PRIMES

for i in range(0, len(PRIMES)):
    length = get_recurring_length(PRIMES[i])
    if length > greatest:
        greatest = length
        result = i

print result