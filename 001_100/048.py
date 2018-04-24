'''
Self powers
Problem 48 

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

import gmpy2

result = 0

for i in range(1,1001):
    temp = str(pow(gmpy2.mpz(i),i))
    print temp
    if len(temp) > 10:
        result += int(temp[-10:])
    else:
        result += int(temp)
print str(result)[-10:]