'''
Integer right triangles
Problem 39 

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import gmpy2
import numpy as np

result = [0 for i in range(0,1001)]

for a in range(1, 333):
    for b in range(a, 500):
        c2 = a*a + b*b
        c = gmpy2.isqrt(c2)
        if gmpy2.is_square(c2) and a + b + c <= 1000:
            result[a + b + c] += 1


print np.argmax(result)