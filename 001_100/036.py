'''
Double-base palindromes
Problem 36 

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def palindrome(n):
    return n == n[::-1]


result = 0
for i in range(1000000):
    strNum = str(i)
    strNumBin = bin(i)[2:]
    if palindrome(strNum) and palindrome(strNumBin):
        result += i
        print strNum, strNumBin

print result