'''
Champernowne's constant
Problem 40 

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def dn(n):    #n < 100000000
    if n <= 0:
        return 0
    elif n < 10:
        return n
    elif n <= 189:
        return int(str(((n - 9 - 1) / 2 + 10))[(n - 9 - 1) % 2])
    elif n <= 2889:
        return int(str((n - 271 - 1) / 3 + 100)[(n - 189 - 1) % 3])
    elif n <= 38889:
        return int(str((n - 2889 - 1) / 4 + 1000)[(n - 2889 - 1) % 4])
    elif n <= 488889:
        return int(str((n - 38889 - 1) / 5 + 10000)[(n - 38889 - 1) % 5])
    elif n <= 5888889:
        return int(str((n - 488889 - 1) / 6 + 100000)[(n - 488889 - 1) % 6])
    else:
        return 0

print dn(1) , dn(10) , dn(100) , dn(1000) , dn(10000) , dn(100000) , dn(1000000)