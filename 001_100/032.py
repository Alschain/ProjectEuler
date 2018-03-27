'''
Pandigital products
Problem 32 

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

'''

def judge(a, b, c):
    myset = set()
    while a != 0:
        myset.add(a % 10)
        a = a / 10
    while b != 0:
        myset.add(b % 10)
        b = b / 10
    while c != 0:
        myset.add(c % 10)
        c = c / 10
    if len(myset) == 9 and sum(myset) == 45:
        return True
    return False


result = set()

for i in range(1, 10):
    for j in range(1000, 10000):
        product = i * j
        if product > 9999:
            continue
        if judge(i, j, product):
            result.add(product)

for i in range(10, 100):
    for j in range(100, 1000):
        product = i * j
        if product > 9999:
            continue
        if judge(i, j, product):
            result.add(product)

print sum(result)