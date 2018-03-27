'''
Digit cancelling fractions
Problem 33 

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import gmpy2

DIGITS = ['1', '2', '3', '4', '5' ,'6' ,'7' ,'8' ,'9']

result = {}
for i in range(0, len(DIGITS)):
    for j in range(i + 1, len(DIGITS)):
        for k in range(j + 1, len(DIGITS)):
            A1 = int(DIGITS[i] + DIGITS[j])
            A2 = int(DIGITS[i] + DIGITS[k])
            A3 = int(DIGITS[j] + DIGITS[i])
            A4 = int(DIGITS[k] + DIGITS[i])
            A5 = int(DIGITS[j] + DIGITS[k])
            A6 = int(DIGITS[k] + DIGITS[j])

            comp_jk = 1.0 * int(DIGITS[j]) / int(DIGITS[k])
            comp_ik = 1.0 * int(DIGITS[i]) / int(DIGITS[k])
            comp_ij = 1.0 * int(DIGITS[i]) / int(DIGITS[j])

            if 1.0 * A1 / A2 == comp_jk:
                result[A1] = A2
            if 1.0 * A3 / A4 == comp_jk:
                result[A3] = A4
            if 1.0 * A1 / A4 == comp_jk:
                result[A1] = A4
            
            if 1.0 * A1 / A5 == comp_ik:
                result[A1] = A5
            if 1.0 * A3 / A5 == comp_ik:
                result[A3] = A5
            if 1.0 * A1 / A6 == comp_ik:
                result[A1] = A6
            
            if 1.0 * A2 / A6 == comp_ij:
                result[A2] = A6
            if 1.0 * A2 / A5 == comp_ij:
                result[A2] = A5
            if 1.0 * A4 / A6 == comp_ij:
                result[A4] = A6

numerator = 1
denominator = 1

for key in result.keys():
    numerator *= key
    denominator *= result[key]

print denominator / gmpy2.gcd(numerator, denominator)