'''
Consecutive prime sum
Problem 50 

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from sympy import primerange

PRIMES = list(primerange(2,1000000))
PRIMES_SUM = []

PRIMES_SUM.append(PRIMES[0])
for i in range(1,len(PRIMES)):
    PRIMES_SUM.append(PRIMES_SUM[-1] + PRIMES[i])


num = 0
N = 0

from tqdm import tqdm
for i in tqdm(range(len(PRIMES_SUM) - 1, 0, -1)):
    for j in range(i - 1 - N , 0, -1):
        temp = PRIMES_SUM[i] - PRIMES_SUM[j]
        if temp > PRIMES[-1]:
            break
        if temp in PRIMES:
            if i - j + 1 > N:
                N = i - j + 1
                num = temp
print num,N